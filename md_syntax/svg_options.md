## Syntax

|                                |                                                                                                        |
|--------------------------------|--------------------------------------------------------------------------------------------------------|
| `svg_options`                  | Description {p2line None}                                                                              |
| `baselineshift:(on`\|`off)`    | whether to use SVG `baseline-shift` attribute for subscript or superscript; default is `off`           |
| `ignorefont(on`\|`off)`        | whether to ignore graph fonts used for text; default is `off`                                          |
| `bgfill(on`\|`off)`            | whether to ignore background fill; default is `on`                                                     |
| `nbsp(on`\|`off)`              | whether to use Unicode character for no-break space instead of spaces in some strings; default is `on` |
| `clipstroke(on`\|`off)`        | whether to use clipping paths to simulate stroke alignment; default is `on`                            |
| `scalestrokewidth(on`\|`off)`  | whether to manually scale stroke widths; default is `off`                                              |
| `verbose`                      | whether to output all default attributes and classes                                                   |
| `pathprefix(prefix)`           | prefix to use when naming SVG paths                                                                    |
| `width:(#px`\|`#in)`   | width of graph in pixels or inches                                                                     |
| `height:(#px`\|`#in)`  | height of graph in pixels or inches                                                                    |
| `fontface:(fontname)`      | default font to use                                                                                    |
| `fontfacesans(fontname)`   | font to use for text in `{c -(}stSans{c )-}` "font"                                                    |
| `fontfaceserif(fontname)`  | font to use for text in `{c -(}stSerif{c )-}` "font"                                                   |
| `fontfacemono(fontname)`   | font to use for text in `{c -(}stMono{c )-}` "font"                                                    |
| `fontfacesymbol(fontname)` | font to use for text in `{c -(}stSymbol{c )-}` "font" {p2line None}                                    |

where `fontname` may be a valid font name or `default` to restore the
default setting.

Current default values may be listed by typing

`. graph set svg`

and default values may be set by typing

`. graph set svg name value`

where `name` is the name of an `svg_option`, omitting the parentheses.
