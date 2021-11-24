from abc import get_cache_token
from typing import Optional
from pygls.lsp.types.basic_structures import Location, Position, TextDocumentIdentifier, TextDocumentItem
from pygls.lsp.types.language_features import HoverParams, DefinitionParams
from pygls.lsp.types.workspace import DidOpenTextDocumentParams
import pytest
from mock import Mock
from pygls.lsp.types import TextDocumentIdentifier
from pygls.workspace import Document, Workspace

from server.server import (completions, get_configuration_callback, hover, goto_definition,
                           refresh_diagnostics)


class FakeServer():
    """Create fake server to unit test features."""
    publish_diagnostics = None
    show_message = None
    show_message_log = None
    get_configuration = None

    def __init__(self):
        self.workspace = Workspace('', None)


fake_document_uri = 'file://fake_dofile.do'
fake_document_content = 'gen x = 3\nreplace x =10\nsort x'
fake_doc_identifier = TextDocumentIdentifier(uri=fake_document_uri)
fake_document = Document(fake_document_uri, fake_document_content)
fake_hoverParams = HoverParams(text_document=fake_doc_identifier,
                               position=Position(line=2, character=1))
fake_defParams = DefinitionParams(text_document=fake_doc_identifier,

                                  position=Position(line=1, character=9))
fake_diagParams = DidOpenTextDocumentParams(
                  text_document=TextDocumentItem(
                        uri=fake_document_uri,
                        language_id='stata',
                        version='13',
                        text=fake_document_content
                  ))


server = FakeServer()
server.publish_diagnostics = Mock()
server.show_message = Mock()
server.show_message_log = Mock()
server.get_configuration = Mock()
server.workspace.get_document = Mock(return_value=fake_document)


def _reset_mocks():
    server.publish_diagnostics.reset_mock()
    server.show_message.reset_mock()
    server.show_message_log.reset_mock()


def test_completions():
    completion_list = completions()
    labels = [i.label for i in completion_list.items]

    assert 'nlist' in labels
    assert 'nlogit' in labels
    assert 'notes' in labels


def test_hover(server=server, fake_hoverParams=fake_hoverParams):
    result = hover(server, fake_hoverParams)
    docstring = result.contents.value
    assert '## Syntax\n\n`sort`' in docstring


def test_goto_definition(server=server, fake_defParams=fake_defParams):
    result = goto_definition(server, fake_defParams)
    assert isinstance(result, Location)
    assert 0 == result.range.start.line
    assert 4 == result.range.start.character


def test_refresh_diagnostics(server=server, fake_diagParams=fake_diagParams):
    _reset_mocks()
    expected_msg = "whitespace around operator should be 1"
    
    refresh_diagnostics(server, fake_diagParams)

    args = server.publish_diagnostics.call_args
    assert args[1]['diagnostics'][0].message == expected_msg
