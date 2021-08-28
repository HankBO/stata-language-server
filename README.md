# Stata-Language-Server

A [language server](https://microsoft.github.io/language-server-protocol/) for [Stata](https://www.stata.com/).

## Description

This plugin uses Markdown(GFM) format of Stata syntax(eg: replace.md) for syntax tips. Original Stata help files(.scml) are extracted and converted to markdown files using Python script([parse-smcl](https://github.com/sergiocorreia/parse-smcl)).
Only Paragraph `Syntax` in a help-file will be showed while hovering.

## Supported Features

- Syntax auto completion

    Auto-Completion for most stata commands. Only support complete syntax(eg: `generate`, not `g(enerate)`) now.

    ![completion](https://github.com/HankBO/stata-language-server/blob/develop/assets/img/completion.gif)

- Syntax tips while hovering

    When hovering on a complete command, a markdown formatted Syntax Description will appear.

    Note: 1.this feature is not available for uncomplete commands(eg: `g`, `gen`) now. 2.some commands have no own help files since they are included in other commands(eg: `replace` belongs to `generate`)

    ![hover](https://github.com/HankBO/stata-language-server/blob/develop/assets/img/hover.gif)

- Goto Definition(`generate varname =`)

    When right-click a variable name and click `Go to Definition`, this feature will find the last `generate` place before. It can match pattern like `g(enerate)`.

    ![gotoDefinition](https://github.com/HankBO/stata-language-server/blob/develop/assets/img/gotoDefinition.gif)

## Install Server Dependencies

- [pygls](https://github.com/openlawlibrary/pygls)(0.11.2)

## Future Plan

Following Features will be implemented:

- [ ] Codestyle diagnostics
- [ ] Brief commands completion(like `forval`)
- [ ] Docstring IO optimization, less file size

## Resources Referenced

- [Stata language support in Atom](https://github.com/kylebarron/language-stata)
