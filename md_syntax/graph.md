## Syntax

`graph` ...

The commands that draw graphs are

|                                                                                                          |                                                        |
|----------------------------------------------------------------------------------------------------------|--------------------------------------------------------|
| Command                                                                                                  | Description {p2line None}                              |
| [<strong>graph twoway</strong>](http://www.stata.com/help.cgi?twoway)         | scatterplots, line plots, etc.                         |
| [<strong>graph matrix</strong>](http://www.stata.com/help.cgi?graph%20matrix) | scatterplot matrices                                   |
| [<strong>graph bar</strong>](http://www.stata.com/help.cgi?graph%20bar)       | bar charts                                             |
| [<strong>graph dot</strong>](http://www.stata.com/help.cgi?graph%20dot)       | dot charts                                             |
| [<strong>graph box</strong>](http://www.stata.com/help.cgi?graph%20box)       | box-and-whisker plots                                  |
| [<strong>graph pie</strong>](http://www.stata.com/help.cgi?graph%20pie)       | pie charts                                             |
| `other`                                                                                                  | more commands to draw statistical graphs {p2line None} |

The commands that save a previously drawn graph, redisplay previously
saved graphs, and combine graphs are

|                                                                                                            |                                                             |
|------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| Command                                                                                                    | Description {p2line None}                                   |
| [<strong>graph save</strong>](http://www.stata.com/help.cgi?graph%20save)       | save graph to disk                                          |
| [<strong>graph use</strong>](http://www.stata.com/help.cgi?graph%20use)         | redisplay graph stored on disk                              |
| [<strong>graph display</strong>](http://www.stata.com/help.cgi?graph%20display) | redisplay graph stored in memory                            |
| [<strong>graph combine</strong>](http://www.stata.com/help.cgi?graph%20combine) | combine multiple graphs                                     |
| [<strong>graph replay</strong>](http://www.stata.com/help.cgi?graph%20replay)   | redisplay graphs stored in memory and on disk {p2line None} |

The commands for printing a graph are

|                                                                                                              |                                                    |
|--------------------------------------------------------------------------------------------------------------|----------------------------------------------------|
| Command                                                                                                      | Description {p2line None}                          |
| [<strong>graph print</strong>](http://www.stata.com/help.cgi?graph%20print)       | print currently displayed graph                    |
| [<strong>set printcolor</strong>](http://www.stata.com/help.cgi?set%20printcolor) | set how colors are printed                         |
| [<strong>graph export</strong>](http://www.stata.com/help.cgi?graph%20export)     | export .gph file to PostScript, etc. {p2line None} |

The commands that deal with the graphs currently stored in memory are

|                                                                                                              |                                                                                                                                                                                 |
|--------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Command                                                                                                      | Description {p2line None}                                                                                                                                                       |
| [<strong>graph display</strong>](http://www.stata.com/help.cgi?graph%20display)   | display graph                                                                                                                                                                   |
| [<strong>graph dir</strong>](http://www.stata.com/help.cgi?graph%20dir)           | list names                                                                                                                                                                      |
| [<strong>graph describe</strong>](http://www.stata.com/help.cgi?graph%20describe) | describe contents                                                                                                                                                               |
| [<strong>graph rename</strong>](http://www.stata.com/help.cgi?graph%20rename)     | rename memory graph                                                                                                                                                             |
| [<strong>graph copy</strong>](http://www.stata.com/help.cgi?graph%20copy)         | copy memory graph to new name                                                                                                                                                   |
| [<strong>graph drop</strong>](http://www.stata.com/help.cgi?graph%20drop)         | discard graphs in memory                                                                                                                                                        |
| [<strong>graph close</strong>](http://www.stata.com/help.cgi?graph%20close)       | close Graph windows {p2line None} {pin None} Also see [<strong>[G-2]</strong> graph manipulation](http://www.stata.com/help.cgi?graph_manipulation). |

The commands that describe available schemes and allow you to identify
and set the default scheme are

|                                                                                                                 |                                                                                                                                                                |
|-----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Command                                                                                                         | Description {p2line None}                                                                                                                                      |
| [<strong>graph query, schemes</strong>](http://www.stata.com/help.cgi?graph%20query) | list available schemes                                                                                                                                         |
| [<strong>query graphics</strong>](http://www.stata.com/help.cgi?set%20scheme)        | identify default scheme                                                                                                                                        |
| [<strong>set scheme</strong>](http://www.stata.com/help.cgi?set%20scheme)            | set default scheme {p2line None} {pin None} Also see [<strong>[G-4]</strong> schemes intro](http://www.stata.com/help.cgi?schemes). |

The command that lists available styles is

|                                                                                                        |                                     |
|--------------------------------------------------------------------------------------------------------|-------------------------------------|
| Command                                                                                                | Description {p2line None}           |
| [<strong>graph query</strong>](http://www.stata.com/help.cgi?graph%20query) | list available styles {p2line None} |

The command for setting options for printing and exporting graphs is

|                                                                                                    |                                    |
|----------------------------------------------------------------------------------------------------|------------------------------------|
| Command                                                                                            | Description {p2line None}          |
| [<strong>graph set</strong>](http://www.stata.com/help.cgi?graph%20set) | set graphics options {p2line None} |

The command that allows you to draw graphs without displaying them is

|                                                                                                          |                                                |
|----------------------------------------------------------------------------------------------------------|------------------------------------------------|
| Command                                                                                                  | Description {p2line None}                      |
| [<strong>set graphics</strong>](http://www.stata.com/help.cgi?set%20graphics) | set whether graphs are displayed {p2line None} |
