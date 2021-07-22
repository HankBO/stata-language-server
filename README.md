# Stata-Language-Server

A [language server](https://microsoft.github.io/language-server-protocol/) that provides 1. Auto completion; 2. Syntax tips while hovering for [Stata](https://www.stata.com/).

## Description

This plugin uses Markdown(GFM) format of Stata syntax(eg: replace.md) for syntax tips. Original Stata help files(.scml) are extracted and converted to markdown files using Python script([parse-smcl](https://github.com/sergiocorreia/parse-smcl)).
Only Paragraph `Syntax` will be showed while hovering.

## Dependencies

[pygls](https://github.com/openlawlibrary/pygls)

## Future Plan

Following Features will be implemented:
1. Codestyle Diagnostics
2. Goto Definition(`gen varname`)
