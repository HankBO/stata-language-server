import os
from pygls.lsp.types import (CompletionItem, CompletionList,
                             CompletionItemKind, MarkupContent)


def getDocstringFromWord(word: str, doc_path: str = 'md_syntax') -> MarkupContent:

    try:
        with open(os.path.join(doc_path, word + ".md"), 'r') as f:
            docstring = f.read()
    except FileNotFoundError:
        docstring = ""
    return MarkupContent(
            kind = 'markdown',
            value = docstring
    )


def getComItemFromFilename(name: str, kind=CompletionItemKind.Keyword, doc_path: str = "") -> CompletionItem:

    comItem = CompletionItem(label=name, kind=kind, documentation=doc_path)
    return comItem


def getComList(doc_path: str = 'md_syntax') -> CompletionList:
    all_fn = os.listdir(doc_path)
    itemList = []
    for base_fn in all_fn:
        comItem = getComItemFromFilename(name=base_fn.split('.')[0], doc_path=doc_path)
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