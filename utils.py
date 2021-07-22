
import os
from pygls.types import (CompletionItem, CompletionList,
                         CompletionItemKind, MarkupContent)


def getDocstringFromWord(word: str, doc_path: str = 'md_syntax') -> MarkupContent:
    # summarize
    # _
    try:
        with open(os.path.join(doc_path, word+".md"), 'r') as f:
            docstring = f.read()
    except FileNotFoundError:
            docstring = ""
    return MarkupContent(
            kind = 'markdown',
            value = docstring
    )

def getComItemFromFilename(fn: str, doc_path: str) -> CompletionItem:

    comItem = CompletionItem(
			    label = fn,
			    kind = CompletionItemKind.Method
                )
    return comItem

def getComList(doc_path: str='md_syntax', saveFile=False) -> CompletionList:
    all_fn = os.listdir(doc_path)
    itemList = []
    for base_fn in all_fn:
        comItem = getComItemFromFilename(base_fn.split('.')[0], doc_path)
        itemList.append(comItem)

    comList = CompletionList(False, itemList)
    if saveFile == True:
        with open('comlist.py', 'w') as f: # 
            f.write(str(comList))
    return comList

#getComList('md_syntax', saveFile=True)
