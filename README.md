# Stata-Language-Server

> Write your Stata scripts more fluently!

## Description

An extension for [Stata](https://www.stata.com/) on VS Code. It provides codestyle checking, goto-definition, syntax tips and auto completion.

Developed based on [language server](https://microsoft.github.io/language-server-protocol/), depending on Third-party Python library [pygls](https://github.com/openlawlibrary/pygls).

> Note: Python(>=3.6) is required on local system before extension installing. Another extension [Stata Enhanced](https://marketplace.visualstudio.com/items?itemName=kylebarron.stata-enhanced) is recommanded for syntax highlight since Stata Language Server doesn't provide this feature.

## Supported Features

- Codestyle Checking

    When editing a stata do-file, the extension will check documents and show bad codestyle using wavy underlines.

    ![diagnostic](https://github.com/HankBO/stata-language-server/blob/develop/assets/img/diagnostics.gif)

- Syntax tips while hovering

    When hovering on a complete command, a markdown formatted Syntax Description will appear.

    > Note: Not available for 1.abbr. commands(eg: `g`, `gen`); 2.docstring included in another command's docstring(eg: `replace` belongs to `generate`)

    ![hover](https://github.com/HankBO/stata-language-server/blob/develop/assets/img/hover.gif)

    > Note: Docstring files of this extension are only for academic purpose. The original work copyright belongs to StataCorp LLC. See ThirdPartyNotices.txt for details.

- Goto Definition(`generate varname =`)

    Find and jump to the last `generate` place when right-click a variable name and click `Go to Definition`. Can match pattern like `g(enerate)`.

    ![gotoDefinition](https://github.com/HankBO/stata-language-server/blob/develop/assets/img/gotoDefinition.gif)

- Syntax auto completion

    Auto-Completion for most stata commands. Only support complete syntax(eg: `generate`, not `g(enerate)`).

    ![completion](https://github.com/HankBO/stata-language-server/blob/develop/assets/img/completion.gif)

## Requirements

- Python >= 3.6

## Settings

| Setting Name | Description | Default Value |
|---|---|---|
| `stataServer.setMaxLineLength` | Max line length for codestyle checking | `120` |
| `stataServer.setIndentSpace` | Indent spaces for codetyle checking | `4` |

## Release Notes

Refer to [CHANGELOG.md]

## Issues

Submit [issues] if you find any bug or have any suggestion.
