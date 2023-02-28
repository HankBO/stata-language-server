"""Define Regex for codestyle checking."""
import re
from lsprotocol.types import DiagnosticSeverity

# Configures
MAX_LINE_LENGTH = 120
INDENT_SPACE = 4
ENABLECOMPLETION = True
ENABLEDOCSTRING = True
ENABLESTYLECHECKING = True

# Diagnostic Regex
STAR_COMMENTS = re.compile(r'^s*(\*)')
BLOCK_COMMENTS = frozenset(['/*', '*/'])
BLOCK_COMMENTS_BG = re.compile(r'.*?(/\*.*)')
BLOCK_COMMENTS_END = re.compile(r'(.*\*/).*')
INLINE_COMMENTS = frozenset(['//'])
INLINE_COMM_RE = re.compile(r'.*(//.*)')
STRING = re.compile(r'".*?"')
OPERATOR_REGEX = re.compile(r'(?:[^,\s])(\s*)(?:[-+*/|!<=>%&^]+)(\s*)')
WHITESPACE_AFTER_COMMA_REGEX = re.compile(r'[,](\s*)')
LOOP_START = re.compile(r'(^\s*)(?:foreach|forvalue).*\{')
LOOP_END = re.compile(r'(^\s*)\}\s*')
INDENT_REGEX = re.compile(r'([ \t]*)\S+')
EXTRANEOUS_WHITESPACE_REGEX = re.compile(r'[\[({] | [\]}),;]| :(?!=)')

# Diagnostic Messages
MAX_LINE_LENGTH_MESSAGE = "line too long"
OP_WHITESPACE_MESSAGE = "whitespace around operator should be 1"
COMMA_WHITESPACE_MESSAGE = "1 whitespace after ','"
INAP_INDENT_MESSAGE = "inappropriate indented line"

# Diagnostic Severity
MAX_LINE_LENGTH_SEVERITY = DiagnosticSeverity.Warning
OP_WHITESPACE_SEVERITY = DiagnosticSeverity.Warning
COMMA_WHITESPACE_SEVERITY = DiagnosticSeverity.Warning
INAP_INDENT_SEVERITY = DiagnosticSeverity.Warning
