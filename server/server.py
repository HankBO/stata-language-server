import uuid
import utils
from typing import Optional
import re

from pygls.lsp.methods import (COMPLETION, HOVER, DEFINITION)
from pygls.server import LanguageServer
from pygls.lsp.types import (CompletionList, CompletionParams, Location, DefinitionParams,
                             Hover, HoverParams, MessageType, Position, Range, Registration,
                             RegistrationParams, Unregistration, UnregistrationParams)


class StataLanguageServer(LanguageServer):
    CMD_REGISTER_COMPLETIONS = 'registerCompletions'
    CMD_REGISTER_HOVER = 'registerHover'
    CMD_REGISTER_DEFINITION = 'registerDefinition'
    CMD_UNREGISTER_COMPLETIONS = 'unregisterCompletions'
    CMD_UNREGISTER_HOVER = 'unregisterHover'
    CMD_UNREGISTER_DEFINITION = 'unregisterDefinition'

    def __init__(self):
        super().__init__()


stata_server = StataLanguageServer()
COMLIST = utils.getComList()  # TODO: Optimize IO speed


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
    origin_pos = params.position  #  start from 1
    origin_line = origin_pos.line  #  start from 0
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


@stata_server.command(StataLanguageServer.CMD_REGISTER_COMPLETIONS)
async def register_completions(ls: StataLanguageServer, *args):
    """Register completions method on the client."""
    params = RegistrationParams(registrations=[Registration(id=str(uuid.uuid4()), method=COMPLETION,
                                             )])
    response = await ls.register_capability_async(params)
    if response is None:
        ls.show_message('Successfully registered completions method')
    else:
        ls.show_message('Error happened during completions registration.',
                        MessageType.Error)


@stata_server.command(StataLanguageServer.CMD_UNREGISTER_COMPLETIONS)
async def unregister_completions(ls: StataLanguageServer, *args):
    """Unregister completions method on the client."""
    params = UnregistrationParams(unregistrations=[Unregistration(id=str(uuid.uuid4()), method=COMPLETION)])
    response = await ls.unregister_capability_async(params)
    if response is None:
        ls.show_message('Successfully unregistered completions method')
    else:
        ls.show_message('Error happened during completions unregistration.',
                        MessageType.Error)


@stata_server.command(StataLanguageServer.CMD_REGISTER_HOVER)
async def register_hover(ls: StataLanguageServer, *args):
    """Register hover method on the client."""
    params = RegistrationParams(registrations=[Registration(id=str(uuid.uuid4()), method=HOVER)])
    response = await ls.register_capability_async(params)
    if response is None:
        ls.show_message('Successfully registered hover method')
    else:
        ls.show_message('Error happened during hover registration.',
                        MessageType.Error)


@stata_server.command(StataLanguageServer.CMD_UNREGISTER_HOVER)
async def unregister_hover(ls: StataLanguageServer, *args):
    """Unregister hover method on the client."""
    params = UnregistrationParams(unregistrations=[Unregistration(id=str(uuid.uuid4()), method=HOVER)])
    response = await ls.unregister_capability_async(params)
    if response is None:
        ls.show_message('Successfully unregistered hover method')
    else:
        ls.show_message('Error happened during hover unregistration.',
                        MessageType.Error)


@stata_server.command(StataLanguageServer.CMD_REGISTER_DEFINITION)
async def register_definition(ls: StataLanguageServer, *args):
    """Register definition method on the client."""
    params = RegistrationParams(registrations=[Registration(id=str(uuid.uuid4()),
                                                            method=DEFINITION)])
    response = await ls.register_capability_async(params)
    if response is None:
        ls.show_message('Successfully registered definition method')
    else:
        ls.show_message('Error happened during definition registration.',
                        MessageType.Error)


@stata_server.command(StataLanguageServer.CMD_UNREGISTER_DEFINITION)
async def unregister_definition(ls: StataLanguageServer, *args):
    """Unregister definition method on the client."""
    params = UnregistrationParams(unregistrations=[Unregistration(id=str(uuid.uuid4()),
                                                                  method=DEFINITION)])
    response = await ls.unregister_capability_async(params)
    if response is None:
        ls.show_message('Successfully unregistered definition method')
    else:
        ls.show_message('Error happened during definition unregistration.',
                        MessageType.Error)
