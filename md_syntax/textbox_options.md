## Syntax

Textboxes contain one or more lines of text. The appearance of textboxes
is controlled by the following options:

|                                          |                                            |
|------------------------------------------|--------------------------------------------|
| `textbox_options`                        | Description {p2line None}                  |
| `tstyle:(textboxstyle)`              | overall style                              |
| `orientation:(orientationstyle)`     | whether vertical or horizontal             |
| `size:(textsizestyle)`               | size of text                               |
| `color:(colorstyle)`                 | color and opacity of text                  |
| `justification:(justificationstyle)` | text left, centered, right-justified       |
| `alignment:(alignmentstyle)`         | text top, middle, bottom baseline          |
| `margin:(marginstyle)`               | margin from text to border                 |
| `linegap(relativesize)`              | space between lines                        |
| `width(relativesize)`                | width of textbox override                  |
| `height(relativesize)`               | height of textbox override                 |
| `box` or `nobox`                         | whether border is drawn around box         |
| `bcolor:(colorstyle)`                | color and opacity of background and border |
| `fcolor:(colorstyle)`                | color and opacity of background            |
| `lstyle:(linestyle)`                 | overall style of border                    |
| `lpattern:(linepatternstyle)`        | line pattern of border                     |
| `lwidth:(linewidthstyle)`            | thickness of border                        |
| `lcolor:(colorstyle)`                | color and opacity of border                |
| `lalign:(linealignmentstyle)`        | border alignment (inside, outside, center) |
| `bmargin:(marginstyle)`              | margin from border outwards                |
| `bexpand`                                | expand box in direction of text            |
| `placement:(compassdirstyle)`        | location of textbox override {p2line None} |

The above options invariably occur inside other options. For instance,
the syntax of `title()` (see
[<strong>[G-3]</strong> <em>title_options</em>](http://www.stata.com/help.cgi?title_options))
is

`title("string"` \[`"string"` \[...\]\] \[`, title_options`
`textbox_options`\]`)`

so any of the options above can appear inside the `title()` option:

`. graph` ... `,` ... `title("My title", color(green) box)` ...
