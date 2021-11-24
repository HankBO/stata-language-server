import uuid

from pygls.protocol import LanguageServerProtocol
import server.utils as utils
from pygls.lsp.types.basic_structures import Diagnostic, DiagnosticSeverity
from pygls.lsp.types.workspace import (ConfigurationItem, ConfigurationParams,
     DidChangeTextDocumentParams, DidCloseTextDocumentParams, DidOpenTextDocumentParams)
from typing import Optional
import re
from pygls.lsp.methods import (COMPLETION, HOVER, DEFINITION, TEXT_DOCUMENT_DID_CHANGE,
                               TEXT_DOCUMENT_DID_CLOSE,
                               TEXT_DOCUMENT_PUBLISH_DIAGNOSTICS, TEXT_DOCUMENT_DID_OPEN,
                               WORKSPACE_CONFIGURATION)
from pygls.server import LanguageServer
from pygls.lsp.types import (CompletionList, CompletionParams, Location, DefinitionParams,
                             Hover, HoverParams, MessageType, Position, Range, Registration,
                             RegistrationParams, Unregistration, UnregistrationParams,
                             PublishDiagnosticsParams)
from server.constants import (MAX_LINE_LENGTH_MESSAGE, OPERATOR_REGEX, STRING, STAR_COMMENTS,
                              WHITESPACE_AFTER_COMMA_REGEX, OPERATOR_REGEX, BLOCK_COMMENTS_BG,
                              BLOCK_COMMENTS_END, INLINE_COMM_RE, LOOP_START, LOOP_END, INDENT_REGEX,
                              OP_WHITESPACE_MESSAGE, COMMA_WHITESPACE_MESSAGE, INAP_INDENT_MESSAGE,
                              MAX_LINE_LENGTH_SEVERITY, MAX_LINE_LENGTH, INDENT_SPACE,
                              OP_WHITESPACE_SEVERITY, COMMA_WHITESPACE_SEVERITY, INAP_INDENT_SEVERITY,
                              USECOMPLETION, USEDOCSTRING, USESTYLECHECKING)
COMLIST = utils.getComList()  # TODO: Optimize IO speed


class StataLanguageServerProtocol(LanguageServerProtocol):
    """
        Override some build-in fuctions.
        #TODO: Conditionally register fuction to features based on configures.
    """
    def __init__(self):
        super().__init__()


class StataLanguageServer(LanguageServer):
    CMD_REGISTER_COMPLETIONS = 'registerCompletions'
    CMD_REGISTER_HOVER = 'registerHover'
    CMD_REGISTER_DEFINITION = 'registerDefinition'
    CMD_GET_CONFIGURATION_CALLBACK = 'getConfigurationCallback'
    CMD_UNREGISTER_COMPLETIONS = 'unregisterCompletions'
    CMD_UNREGISTER_HOVER = 'unregisterHover'
    CMD_UNREGISTER_DEFINITION = 'unregisterDefinition'

    CONFIGURATION_SECTION = 'stataServer'

    def __init__(self, protocol_cls=StataLanguageServerProtocol):
        super().__init__()


stata_server = StataLanguageServer()
COMLIST = utils.getComList()  # TODO: Optimize IO speed


@stata_server.feature(TEXT_DOCUMENT_DID_CHANGE)
def did_change(ls, params: DidChangeTextDocumentParams):
    """Text document did change notification."""
    refresh_diagnostics(ls, params)


@stata_server.feature(TEXT_DOCUMENT_DID_CLOSE)
def did_close(server: StataLanguageServer, params: DidCloseTextDocumentParams):
    """Text document did close notification."""
    server.show_message_log('Do File Did Close')


@stata_server.feature(TEXT_DOCUMENT_DID_OPEN)
async def did_open(ls, params: DidOpenTextDocumentParams):
    """Text document did open notification."""
    ls.show_message_log('Do File Did Open')
    get_configuration_callback(ls)
    refresh_diagnostics(ls, params)


@stata_server.feature(COMPLETION)
def completions(params: Optional[CompletionParams] = None) -> CompletionList:
    """Return completion items."""
    return COMLIST


@stata_server.feature(HOVER)
def hover(ls, params: HoverParams):
    """Display Markdown documentation for the element under the cursor."""
    document = ls.workspace.get_document(params.text_document.uri)
    word = document.word_at_position(params.position)  # return start and end positions
    docstring = utils.getDocstringFromWord(word)
    return Hover(contents=docstring)


@stata_server.feature(DEFINITION)
def goto_definition(ls, params: DefinitionParams):
    """
        Go to the last definition of a var: g(enerate) varname
    """
    uri = params.text_document.uri
    document = ls.workspace.get_document(uri)
    origin_pos = params.position  # start from 1
    origin_line = origin_pos.line  # start from 0
    origin_varname = document.word_at_position(origin_pos)
    lenOrigin = len(origin_varname)
    genPattern = '\\b(g(enerate|enerat|enera|ener|ene|en|e)?|egen)\\s+((byte|int|long|float|double|str[1-9]?[0-9]?[0-9]?[0-9]?|strL)\\s+)?([^=\\s]+)\\s*((==)|(=))'

    if origin_line > 0:
        searched_area = document.lines
        for i in range(origin_pos.line - 1, -1, -1):
            matchObj = re.match(genPattern, searched_area[i])
            if matchObj and matchObj.group(5) == origin_varname:
                targetLine = i
                targetStChar = searched_area[i].find(origin_varname)
                targetEndChar = targetStChar + lenOrigin
                target_range = Range(start=Position(line=targetLine,
                                                    character=targetStChar),
                                     end=Position(line=targetLine, character=targetEndChar))
                return Location(uri=uri, range=target_range)
    return None


def create_diagnostic(line: int, stIndex: int, enIndex: int,
                      msg: str, severity: DiagnosticSeverity) -> Diagnostic:
    """Create a Diagnostic"""
    range = Range(
        start=Position(line=line, character=stIndex),
        end=Position(line=line, character=enIndex)
    )
    diag = Diagnostic(
        range=range,
        message=msg,
        severity=severity
    )
    return diag


def inSkipTokens(start, end, skip_tokens: list) -> bool:
    """
        Check if start and end index(python) is in one of skip tokens
    """
    for token in skip_tokens:
        if start >= token[0] and end <= token[1]:
            return True
    return False


@stata_server.feature(TEXT_DOCUMENT_PUBLISH_DIAGNOSTICS)
def refresh_diagnostics(ls: StataLanguageServer, params):
    """
        Codestyle checking and publish diagnostics.
    """
    uri = ls.workspace.get_document(params.text_document.uri).uri
    doc = ls.workspace.get_document(uri)
    diagnostics = []

    LINE_STATE = {"isInComm": False, "loopLevel": 0}  # cross line state
    for lineno, line in enumerate(doc.lines):
        # Max line length
        if len(line) > MAX_LINE_LENGTH:
            diagnostics.append(create_diagnostic(lineno, MAX_LINE_LENGTH, MAX_LINE_LENGTH, MAX_LINE_LENGTH_MESSAGE, MAX_LINE_LENGTH_SEVERITY))
        skip_tokens = []

        # Comment block
        if LINE_STATE['isInComm'] is False:
            match = re.match(BLOCK_COMMENTS_BG, line)
            if match is None:
                pass
            elif match.group(1) == '':
                LINE_STATE['isInComm'] = True
                continue
            else:
                LINE_STATE['isInComm'] = True
                start, end = match.start(1), match.end(1)  # python index
                skip_tokens.append([start, end])
        else:
            match = re.match(BLOCK_COMMENTS_END, line)
            if match is None:
                continue
            elif match.group(1) == '':
                LINE_STATE['isInComm'] = False
                continue
            else:
                LINE_STATE['isInComm'] = False
                start, end = match.start(1), match.end(1)
                skip_tokens.append([start, end])

        # Star Comments
        if re.match(STAR_COMMENTS, line):
            continue

        # Inline Comment
        match = re.match(INLINE_COMM_RE, line)
        if match and match.group(1) != '':
            start, end = match.start(1), match.end(1)
            skip_tokens.append([start, end])

        # STRING
        for match in STRING.finditer(line):
            start, end = match.span()
            if not inSkipTokens(start, end, skip_tokens):
                skip_tokens.append([start, end])

        # Operator Checker
        for match in OPERATOR_REGEX.finditer(line):
            for sindex in range(1, 3):
                start, end = match.start(sindex), match.end(sindex)
                if not inSkipTokens(start, end, skip_tokens):
                    if end - start != 1:
                        diagnostics.append(
                            create_diagnostic(lineno, end, end, OP_WHITESPACE_MESSAGE, OP_WHITESPACE_SEVERITY))

        # Comma Checker
        for match in WHITESPACE_AFTER_COMMA_REGEX.finditer(line):
            start, end = match.start(1), match.end(1)
            if not inSkipTokens(start, end, skip_tokens):
                if end - start != 1:
                    diagnostics.append(
                            create_diagnostic(lineno, end, end, COMMA_WHITESPACE_MESSAGE, COMMA_WHITESPACE_SEVERITY))

        # Loop Indent Checker
        if re.match(LOOP_END, line) and LINE_STATE['loopLevel'] > 0:
            LINE_STATE['loopLevel'] -= 1

        match = re.match(INDENT_REGEX, line)
        if match:
            start, end = match.start(1), match.end(1)
            actual_space = end - start
            if actual_space != LINE_STATE['loopLevel'] * INDENT_SPACE:
                diagnostics.append(create_diagnostic(lineno, end, end, INAP_INDENT_MESSAGE, INAP_INDENT_SEVERITY))

        if re.match(LOOP_START, line):
            LINE_STATE['loopLevel'] += 1

    ls.publish_diagnostics(doc_uri=uri, diagnostics=diagnostics)


@stata_server.command(StataLanguageServer.CMD_GET_CONFIGURATION_CALLBACK)
def get_configuration_callback(ls: StataLanguageServer, *args):
    def _config_callback(config):
        global MAX_LINE_LENGTH, INDENT_SPACE, USECOMPLETION, USEDOCSTRING, USESTYLECHECKING
        try:
            MAX_LINE_LENGTH = int(eval(config[0].get('setMaxLineLength')))
            INDENT_SPACE = int(eval(config[0].get('setIndentSpace')))
            USECOMPLETION = utils.convertJsonBool(config[0].get('useCompletion'))
            USEDOCSTRING = utils.convertJsonBool(config[0].get('useDocstring'))
            USESTYLECHECKING = utils.convertJsonBool(config[0].get('useStyleChecking'))
        except Exception as e:
            ls.show_message_log(f'Error ocurred: {e}')        
    ls.get_configuration(ConfigurationParams(items=[
        ConfigurationItem(
            scope_uri='',
            section=StataLanguageServer.CONFIGURATION_SECTION
        )
    ]), _config_callback)


@stata_server.command(StataLanguageServer.CMD_REGISTER_COMPLETIONS)
async def register_completions(ls: StataLanguageServer, *args):
    """Register completions method on the client."""
    params = RegistrationParams(registrations=[Registration(
                    id=str(uuid.uuid4()),
                    method=COMPLETION,)])
    response = await ls.register_capability_async(params)
    if response is None:
        ls.show_message_log('Successfully registered completions method')
    else:
        ls.show_message_log('Error happened during completions registration.',
                        MessageType.Error)


@stata_server.command(StataLanguageServer.CMD_UNREGISTER_COMPLETIONS)
async def unregister_completions(ls: StataLanguageServer, *args):
    """Unregister completions method on the client."""
    params = UnregistrationParams(unregistrations=[Unregistration(id=str(uuid.uuid4()), method=COMPLETION)])
    response = await ls.unregister_capability_async(params)
    if response is None:
        ls.show_message_log('Successfully unregistered completions method')
    else:
        ls.show_message_log('Error happened during completions unregistration.',
                        MessageType.Error)


@stata_server.command(StataLanguageServer.CMD_REGISTER_HOVER)
async def register_hover(ls: StataLanguageServer, *args):
    """Register hover method on the client."""
    params = RegistrationParams(registrations=[Registration(id=str(uuid.uuid4()), method=HOVER)])
    response = await ls.register_capability_async(params)
    if response is None:
        ls.show_message_log('Successfully registered hover method')
    else:
        ls.show_message_log('Error happened during hover registration.',
                        MessageType.Error)


@stata_server.command(StataLanguageServer.CMD_UNREGISTER_HOVER)
async def unregister_hover(ls: StataLanguageServer, *args):
    """Unregister hover method on the client."""
    params = UnregistrationParams(unregistrations=[Unregistration(id=str(uuid.uuid4()), method=HOVER)])
    response = await ls.unregister_capability_async(params)
    if response is None:
        ls.show_message_log('Successfully unregistered hover method')
    else:
        ls.show_message_log('Error happened during hover unregistration.',
                        MessageType.Error)


@stata_server.command(StataLanguageServer.CMD_REGISTER_DEFINITION)
async def register_definition(ls: StataLanguageServer, *args):
    """Register definition method on the client."""
    params = RegistrationParams(registrations=[Registration(id=str(uuid.uuid4()),
                                                            method=DEFINITION)])
    response = await ls.register_capability_async(params)
    if response is None:
        ls.show_message_log('Successfully registered definition method')
    else:
        ls.show_message_log('Error happened during definition registration.',
                        MessageType.Error)


@stata_server.command(StataLanguageServer.CMD_UNREGISTER_DEFINITION)
async def unregister_definition(ls: StataLanguageServer, *args):
    """Unregister definition method on the client."""
    params = UnregistrationParams(unregistrations=[Unregistration(id=str(uuid.uuid4()),
                                                                  method=DEFINITION)])
    response = await ls.unregister_capability_async(params)
    if response is None:
        ls.show_message_log('Successfully unregistered definition method')
    else:
        ls.show_message_log('Error happened during definition unregistration.',
                        MessageType.Error)
