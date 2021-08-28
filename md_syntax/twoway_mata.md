## Syntax

\[`graph`\] `twoway plot` \[`plot` ...\] <span
class="command">\[`if`\] \[`in`\]_ \[`, twoway_options`\]

where the syntax of `plot` is

\[`(`\] `plottype mata_matrix_name` \[`column_names`\]...`, options`
\[`)`\] \[`||`\]

|                                                                                                         |                           |
|---------------------------------------------------------------------------------------------------------|---------------------------|
| `plottype`                                                                                              | Description {p2line None} |
| [<strong>scatter</strong>](http://www.stata.com/help.cgi?scatter)            | scatterplot               |
| [<strong>line</strong>](http://www.stata.com/help.cgi?line)                  | line plot                 |
| [<strong>connected</strong>](http://www.stata.com/help.cgi?twoway_connected) | connected-line plot       |

|                                                                                                       |                        |
|-------------------------------------------------------------------------------------------------------|------------------------|
| [<strong>area</strong>](http://www.stata.com/help.cgi?twoway_area)         | line plot with shading |
| [<strong>bar</strong>](http://www.stata.com/help.cgi?twoway_bar)           | bar plot               |
| [<strong>spike</strong>](http://www.stata.com/help.cgi?twoway_spike)       | spike plot             |
| [<strong>dropline</strong>](http://www.stata.com/help.cgi?twoway_dropline) | dropline plot          |
| [<strong>dot</strong>](http://www.stata.com/help.cgi?twoway_dot)           | dot plot               |

|                                                                                                           |                                                 |
|-----------------------------------------------------------------------------------------------------------|-------------------------------------------------|
| [<strong>rarea</strong>](http://www.stata.com/help.cgi?twoway_rarea)           | range plot with area shading                    |
| [<strong>rbar</strong>](http://www.stata.com/help.cgi?twoway_rbar)             | range plot with bars                            |
| [<strong>rspike</strong>](http://www.stata.com/help.cgi?twoway_rspike)         | range plot with spikes                          |
| [<strong>rcap</strong>](http://www.stata.com/help.cgi?twoway_rcap)             | range plot with capped spikes                   |
| [<strong>rcapsym</strong>](http://www.stata.com/help.cgi?twoway_rcapsym)       | range plot with spikes capped with symbols      |
| [<strong>rscatter</strong>](http://www.stata.com/help.cgi?twoway_rscatter)     | range plot with markers                         |
| [<strong>rline</strong>](http://www.stata.com/help.cgi?twoway_rline)           | range plot with lines                           |
| [<strong>rconnected</strong>](http://www.stata.com/help.cgi?twoway_rconnected) | range plot with lines and markers {p2line None} |

`plot` may also be any syntax for plotting data from the current dataset
as documented in
[<strong>graph twoway</strong>](http://www.stata.com/help.cgi?graph%20twoway).
Multiple Mata matrix plots and data plots may be overlayed in a single
`graph twoway` command.

The leading `graph` is optional. If the first (or only) `plot` is
`scatter`, you may omit `twoway` as well, and then the syntax is

`scatter` ... \[`, scatter_options`\] \[ `|| plot` \[`plot`
\[...\]\]\]

and the same applies to `line`. The other `plottypes` must be preceded
by `twoway`.

Regardless of how the command is specified, `twoway_options` may be
specified among the `scatter_options`, `line_options`, etc., and they
will be treated just as if they were specified among the
`twoway_options` of the `graph twoway` command.
