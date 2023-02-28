import os
from lsprotocol.types import (CompletionItem, CompletionList,
                              CompletionItemKind, MarkupContent)
from functools import lru_cache
import json


@lru_cache(maxsize=64)
def getDocstringFromWord(word: str, doc_path: str = 'md_syntax') -> MarkupContent:

    try:
        with open(os.path.join(doc_path, word + ".md"), 'r') as f:
            docstring = f.read()
    except FileNotFoundError:
        docstring = ""
    return MarkupContent(
            kind='markdown',
            value=docstring
    )


def getComList(doc_path: str = 'commands.json') -> CompletionList:
    with open(doc_path, 'r') as jf:
        jstr = jf.read()
    cmd_list = json.loads(jstr)["syntax"]
    itemList = []
    for cmd in cmd_list:
        comItem = comItem = CompletionItem(label=cmd, kind=CompletionItemKind.Function)
        itemList.append(comItem)

    comList = CompletionList(is_incomplete=False, items=itemList)
    return comList


def convertJsonBool(string: str) -> bool:
    if string == 'true':
        return True
    elif string == 'false':
        return False
    else:
        raise ValueError
