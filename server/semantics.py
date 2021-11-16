"""Define tokens for codestyle checking"""
from typing import Dict, List, Optional, Union
from pygls.lsp.types.language_features.semantic_tokens import (SemanticTokens, SemanticTokensLegend,
                                                               SemanticTokensOptions,
                                                               SemanticTokenTypes,
                                                               SemanticTokenModifiers)
import re


STAR_COMMENTS = re.compile(r'^s*(\*)')
BLOCK_COMMENTS = frozenset(['/*', '*/'])
BLOCK_COMMENTS_BG = re.compile(r'(.*?)/\*.*')
BLOCK_COMMENTS_END = re.compiel(r'.*\*/(.*)')
INLINE_COMMENTS = frozenset(['//'])
INLINE_COMM_RE = re.compile(r'(.*)//.*')
STRING = re.compile(r'(")\w*(")')


OPERATOR_REGEX = re.compile(r'(?:[^,\s])(\s*)(?:[-+*/|!<=>%&^]+)(\s*)')
# 1.不以, wh开头；2.任意空白符；3.运算符号；4.任意空白符
WHITESPACE_AFTER_COMMA_REGEX = re.compile(r'[,;:](\s*)')
LOOP_START = re.compile(r'(^\s*)(?:foreach|forvalue).*\{')
LOOP_END = re.compile(r'(^\s*)\}')
"""
//: r'//[^\n]*'
/* */: r'/\*' -> r'(\\*/\\s+\\*[^\\n]*)|(\\*/(?!\\*))'
*: r'^s*(\*)' -> r'(?=\n)'
///: /// -> \n

Statement: 
ForLoop:

Operators: =, ==
"""

INDENT_REGEX = re.compile(r'([ \t]*)')
EXTRANEOUS_WHITESPACE_REGEX = re.compile(r'[\[({] | [\]}),;]| :(?!=)')
STARTSWITH_INDENT_STATEMENT_REGEX = re.compile(
    r'^\s*({0})\b'.format('|'.join(s.replace(' ', r'\s+') for s in (
        'forvalue', 'foreach',
    )))
)

text = "gen x = 1  // generate variable\n// this is a comment"


def _is_one_line(lines, line_idx):
    """
        Check if a physical line is a logical independent line
        of previous line.
        Logical independent Line:
        1. Not in comment block
        2. Not ends up with '///'
        Return: is_one_line: Bool,
                is_end: Bool,
    """
    pass


def _parseText(text: str) -> SemanticTokens:
    """
        Using absolute position to represent SemanticTokens:
        { line: 2, startChar:  5, length: 3, tokenType: 0, tokenModifiers: 3 },
        { line: 2, startChar: 10, length: 4, tokenType: 1, tokenModifiers: 0 },
        { line: 5, startChar:  2, length: 7, tokenType: 2, tokenModifiers: 0 }
        SemanticTokens {
            data: [  2,5,3,0,3,  0,5,4,1,0,  3,2,7,2,0 ]
            result_id: str
        }
        if id provided, client will include last id, decrease computation.
    """
    # Initialize assistant vars
    result = []
    lines = re.split(r'\r\n|\r|\n', text, flags=re.M)
    lnum = parenlev = continued = 0
    contiline = None
    indents = [0]

    # get attrs: indent_char, indent_level, previous_indent_level
    for i in range(len(lines)):
        line = lines[i]
        lnum += 1
        pos, max = 0, len(line)

        if parenlev == 0 and not continued:  # new statement

        else:  # continued statement

        tokenData = _parseTextToken(line[openOffset, closeOffset])

    return result


def _parseTextToken(word: str) -> List(int):
    pass


def _encodeTokenType(tokenType: str) -> int:
    pass


def indentation(indent_char, indent_level, previous_indent_level):
    pass


if __name__ == '__main__':
    print(_parseText(text))
