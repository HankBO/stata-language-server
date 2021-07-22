
import pytest
from mock import Mock
from pygls.types import (DidCloseTextDocumentParams, DidOpenTextDocumentParams,
                         TextDocumentIdentifier, TextDocumentItem)
from pygls.workspace import Document, Workspace

from ...server import completions


class FakeServer():
    """We don't need real server to unit test features."""

    def __init__(self):
        self.workspace = Workspace('', None)


fake_document_uri = 'file://fake_stata_code.txt'
fake_document_content = 'summarize female,detail // This is comment\nreplace female= 1\n'
fake_document = Document(fake_document_uri, fake_document_content)


server = FakeServer()
server.publish_diagnostics = Mock()
server.show_message = Mock()
server.show_message_log = Mock()
server.workspace.get_document = Mock(return_value=fake_document)


def _reset_mocks():
    server.publish_diagnostics.reset_mock()
    server.show_message.reset_mock()
    server.show_message_log.reset_mock()


def test_completions():
    completion_list = completions()
    labels = [i.label for i in completion_list.items]

    assert '"' in labels
    assert '[' in labels
    assert ']' in labels
    assert '{' in labels
    assert '}' in labels


