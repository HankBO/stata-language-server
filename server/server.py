
import asyncio
import time
import uuid
import utils

from pygls.features import (COMPLETION, TEXT_DOCUMENT_DID_CHANGE,
                            TEXT_DOCUMENT_DID_CLOSE, TEXT_DOCUMENT_DID_OPEN,
                            HOVER, DEFINITION)
from pygls.server import LanguageServer
from pygls.types import (CompletionItem, CompletionList, CompletionParams,
                         CompletionItemKind, MarkupContent,
                         TextDocumentPositionParams, Hover, HoverParams,
                         ConfigurationItem, ConfigurationParams, Diagnostic,
                         DidChangeTextDocumentParams,
                         DidCloseTextDocumentParams, DidOpenTextDocumentParams,
                         MessageType, Position, Range, Registration,
                         RegistrationParams, Unregistration,
                         UnregistrationParams)

COUNT_DOWN_START_IN_SECONDS = 10
COUNT_DOWN_SLEEP_IN_SECONDS = 1

class StataLanguageServer(LanguageServer):
    CMD_COUNT_DOWN_BLOCKING = 'countDownBlocking'
    CMD_COUNT_DOWN_NON_BLOCKING = 'countDownNonBlocking'
    CMD_REGISTER_COMPLETIONS = 'registerCompletions'
    CMD_REGISTER_HOVER = 'registerHover'
    CMD_SHOW_CONFIGURATION_ASYNC = 'showConfigurationAsync'
    CMD_SHOW_CONFIGURATION_CALLBACK = 'showConfigurationCallback'
    CMD_SHOW_CONFIGURATION_THREAD = 'showConfigurationThread'
    CMD_UNREGISTER_COMPLETIONS = 'unregisterCompletions'
    CMD_UNREGISTER_HOVER = 'unregisterHover'

    CONFIGURATION_SECTION = 'stataServer'

    def __init__(self):
        super().__init__()

stata_server = StataLanguageServer()


COMLIST = utils.getComList()
@stata_server.feature(COMPLETION)
def completions(ls, params: CompletionParams = None):
    """Returns completion items."""
    return COMLIST

@stata_server.feature(HOVER)
def hover(ls, params: HoverParams = None):
    """Displays Markdown documentation for the element under the cursor."""
    document = ls.workspace.get_document(params.textDocument.uri)
    word = document.word_at_position(params.position) # return start and end persitions
    docstring = utils.getDocstringFromWord(word)
    return Hover(docstring)

"""
@stata_server.feature(DEFINITION)
def goto_definition(ls, params: DefinitionParams = None):
    document = ls.workspace.get_document(params.textDocument.uri)
    word = document.word_at_position(params.position)

    # is_definition(): find the last 'word' in: g(enerate) [type] var =
    # keep if var == word
    # return the end, not the first definition
    # def_location = ''
    return LocationLink()
"""

@stata_server.command(StataLanguageServer.CMD_COUNT_DOWN_BLOCKING)
def count_down_10_seconds_blocking(ls, *args):
    """Starts counting down and showing message synchronously.
    It will `block` the main thread, which can be tested by trying to show
    completion items.
    """
    for i in range(COUNT_DOWN_START_IN_SECONDS):
        ls.show_message('Counting down... {}'
                        .format(COUNT_DOWN_START_IN_SECONDS - i))
        time.sleep(COUNT_DOWN_SLEEP_IN_SECONDS)


@stata_server.command(StataLanguageServer.CMD_COUNT_DOWN_NON_BLOCKING)
async def count_down_10_seconds_non_blocking(ls, *args):
    """Starts counting down and showing message asynchronously.
    It won't `block` the main thread, which can be tested by trying to show
    completion items.
    """
    for i in range(COUNT_DOWN_START_IN_SECONDS):
        ls.show_message('Counting down... {}'
                        .format(COUNT_DOWN_START_IN_SECONDS - i))
        await asyncio.sleep(COUNT_DOWN_SLEEP_IN_SECONDS)


@stata_server.feature(TEXT_DOCUMENT_DID_CHANGE)
def did_change(ls, params: DidChangeTextDocumentParams):
    """Text document did change notification."""


@stata_server.feature(TEXT_DOCUMENT_DID_CLOSE)
def did_close(server: StataLanguageServer, params: DidCloseTextDocumentParams):
    """Text document did close notification."""
    server.show_message('Text Document Did Close')


@stata_server.feature(TEXT_DOCUMENT_DID_OPEN)
async def did_open(ls, params: DidOpenTextDocumentParams):
    """Text document did open notification."""
    ls.show_message('Text Document Did Open')


@stata_server.command(StataLanguageServer.CMD_REGISTER_COMPLETIONS)
async def register_completions(ls: StataLanguageServer, *args):
    """Register completions method on the client."""
    params = RegistrationParams([Registration(str(uuid.uuid4()), COMPLETION,
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
    params = UnregistrationParams([Unregistration(str(uuid.uuid4()), COMPLETION)])
    response = await ls.unregister_capability_async(params)
    if response is None:
        ls.show_message('Successfully unregistered completions method')
    else:
        ls.show_message('Error happened during completions unregistration.',
                        MessageType.Error)


@stata_server.command(StataLanguageServer.CMD_REGISTER_HOVER)
async def register_hover(ls: StataLanguageServer, *args):
    """Register hover method on the client."""
    params = RegistrationParams([Registration(str(uuid.uuid4()), HOVER,
                                             )])
    response = await ls.register_capability_async(params)
    if response is None:
        ls.show_message('Successfully registered hover method')
    else:
        ls.show_message('Error happened during hover registration.',
                        MessageType.Error)

@stata_server.command(StataLanguageServer.CMD_UNREGISTER_HOVER)
async def unregister_hover(ls: StataLanguageServer, *args):
    """Unregister hover method on the client."""
    params = UnregistrationParams([Unregistration(str(uuid.uuid4()), HOVER)])
    response = await ls.unregister_capability_async(params)
    if response is None:
        ls.show_message('Successfully unregistered hover method')
    else:
        ls.show_message('Error happened during hover unregistration.',
                        MessageType.Error)