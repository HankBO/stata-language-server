## Syntax

|                                |                                                           |
|--------------------------------|-----------------------------------------------------------|
| `ps_options`                   | Description {p2line None}                                 |
| `tmargin:(#)`              | top margin in inches                                      |
| `lmargin:(#)`              | left margin in inches                                     |
| `logo(on`\|`off)`              | whether to include Stata logo                             |
| `cmyk(on`\|`off)`              | whether to use CMYK rather than RGB colors                |
| `mag(#)`                   | magnification/shrinkage factor; default is 100            |
| `fontface:(fontname)`      | default font to use                                       |
| `fontfacesans(fontname)`   | font to use for text in `{c -(}stSans{c )-}` "font"       |
| `fontfaceserif(fontname)`  | font to use for text in `{c -(}stSerif{c )-}` "font"      |
| `fontfacemono(fontname)`   | font to use for text in `{c -(}stMono{c )-}` "font"       |
| `fontfacesymbol(fontname)` | font to use for text in `{c -(}stSymbol{c )-}` "font"     |
| `fontdir(directory)`       | (Unix only) directory in which TrueType fonts are stored  |
| `orientation:(portrait`\|      |                                                           |
| `landscape)`                   | whether vertical or horizontal                            |
| `pagesize:(letter`\|`legal`\|  |                                                           |
| `executive`\|`A4`\|`custom)`   | size of page                                              |
| `pageheight:(#)`           | inches; relevant only if `pagesize(custom)`               |
| `pagewidth:(#)`            | inches; relevant only if `pagesize(custom)` {p2line None} |

where `fontname` may be a valid font name or `default` to restore the
default setting and `directory` may be a valid directory or `default` to
restore the default setting.

Current default values may be listed by typing

`. graph set ps`

and default values may be set by typing

`. graph set ps name value`

where `name` is the name of a `ps_option`, omitting the parentheses.
