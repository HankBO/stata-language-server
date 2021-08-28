## Syntax

\[`graph`\] `twoway plot` _\[`if`\]
\[`in`\]_ \[`, twoway_options`\]

where the syntax of `plot` is

\[`(`\] `plottype`
[varlist](http://www.stata.com/help.cgi?varlist)
...`, options` \[`)`\] \[`||`\]

|                                                                                                         |                                    |
|---------------------------------------------------------------------------------------------------------|------------------------------------|
| `plottype`                                                                                              | Description {p2line None}          |
| [<strong>scatter</strong>](http://www.stata.com/help.cgi?scatter)            | scatterplot                        |
| [<strong>line</strong>](http://www.stata.com/help.cgi?line)                  | line plot                          |
| [<strong>connected</strong>](http://www.stata.com/help.cgi?twoway_connected) | connected-line plot                |
| [<strong>scatteri</strong>](http://www.stata.com/help.cgi?twoway_scatteri)   | `scatter` with immediate arguments |

|                                                                                                       |                        |
|-------------------------------------------------------------------------------------------------------|------------------------|
| [<strong>area</strong>](http://www.stata.com/help.cgi?twoway_area)         | line plot with shading |
| [<strong>bar</strong>](http://www.stata.com/help.cgi?twoway_bar)           | bar plot               |
| [<strong>spike</strong>](http://www.stata.com/help.cgi?twoway_spike)       | spike plot             |
| [<strong>dropline</strong>](http://www.stata.com/help.cgi?twoway_dropline) | dropline plot          |
| [<strong>dot</strong>](http://www.stata.com/help.cgi?twoway_dot)           | dot plot               |

|                                                                                                           |                                            |
|-----------------------------------------------------------------------------------------------------------|--------------------------------------------|
| [<strong>rarea</strong>](http://www.stata.com/help.cgi?twoway_rarea)           | range plot with area shading               |
| [<strong>rbar</strong>](http://www.stata.com/help.cgi?twoway_rbar)             | range plot with bars                       |
| [<strong>rspike</strong>](http://www.stata.com/help.cgi?twoway_rspike)         | range plot with spikes                     |
| [<strong>rcap</strong>](http://www.stata.com/help.cgi?twoway_rcap)             | range plot with capped spikes              |
| [<strong>rcapsym</strong>](http://www.stata.com/help.cgi?twoway_rcapsym)       | range plot with spikes capped with symbols |
| [<strong>rscatter</strong>](http://www.stata.com/help.cgi?twoway_rscatter)     | range plot with markers                    |
| [<strong>rline</strong>](http://www.stata.com/help.cgi?twoway_rline)           | range plot with lines                      |
| [<strong>rconnected</strong>](http://www.stata.com/help.cgi?twoway_rconnected) | range plot with lines and markers          |

|                                                                                                             |                                                        |
|-------------------------------------------------------------------------------------------------------------|--------------------------------------------------------|
| [<strong>pcspike</strong>](http://www.stata.com/help.cgi?twoway_pcspike)         | paired-coordinate plot with spikes                     |
| [<strong>pccapsym</strong>](http://www.stata.com/help.cgi?twoway_pccapsym)       | paired-coordinate plot with spikes capped with symbols |
| [<strong>pcarrow</strong>](http://www.stata.com/help.cgi?twoway_pcarrow)         | paired-coordinate plot with arrows                     |
| [<strong>pcbarrow</strong>](http://www.stata.com/help.cgi?twoway_pcbarrow)       | paired-coordinate plot with arrows having two heads    |
| [<strong>pcscatter</strong>](http://www.stata.com/help.cgi?twoway_pcscatter)     | paired-coordinate plot with markers                    |
| [<strong>pci</strong>](http://www.stata.com/help.cgi?twoway_pci)                 | `pcspike` with immediate arguments                     |
| [<strong>pcarrowi</strong>](http://www.stata.com/help.cgi?twoway_pcarrowi)       | `pcarrow` with immediate arguments                     |
| [<strong>tsline</strong>](http://www.stata.com/help.cgi?tsline)                  | time-series plot                                       |
| [<strong>tsrline</strong>](http://www.stata.com/help.cgi?tsrline)                | time-series range plot                                 |
| [<strong>contour</strong>](http://www.stata.com/help.cgi?twoway_contour)         | contour plot with filled areas                         |
| [<strong>contourline</strong>](http://www.stata.com/help.cgi?twoway_contourline) | contour lines plot                                     |
| [<strong>mband</strong>](http://www.stata.com/help.cgi?twoway_mband)             | median-band line plot                                  |
| [<strong>mspline</strong>](http://www.stata.com/help.cgi?twoway_mspline)         | spline line plot                                       |
| [<strong>lowess</strong>](http://www.stata.com/help.cgi?twoway_lowess)           | LOWESS line plot                                       |
| [<strong>lfit</strong>](http://www.stata.com/help.cgi?twoway_lfit)               | linear prediction plot                                 |
| [<strong>qfit</strong>](http://www.stata.com/help.cgi?twoway_qfit)               | quadratic prediction plot                              |
| [<strong>fpfit</strong>](http://www.stata.com/help.cgi?twoway_fpfit)             | fractional polynomial plot                             |
| [<strong>lfitci</strong>](http://www.stata.com/help.cgi?twoway_lfitci)           | linear prediction plot with CIs                        |
| [<strong>qfitci</strong>](http://www.stata.com/help.cgi?twoway_qfitci)           | quadratic prediction plot with CIs                     |
| [<strong>fpfitci</strong>](http://www.stata.com/help.cgi?twoway_fpfitci)         | fractional polynomial plot with CIs                    |
| [<strong>function</strong>](http://www.stata.com/help.cgi?twoway_function)       | line plot of function                                  |
| [<strong>histogram</strong>](http://www.stata.com/help.cgi?twoway_histogram)     | histogram plot                                         |
| [<strong>kdensity</strong>](http://www.stata.com/help.cgi?twoway_kdensity)       | kernel density plot                                    |
| [<strong>lpoly</strong>](http://www.stata.com/help.cgi?twoway_lpoly)             | local polynomial smooth plot                           |
| [<strong>lpolyci</strong>](http://www.stata.com/help.cgi?twoway_lpolyci)         | local polynomial smooth plot with CIs {p2line None}    |

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

## Syntax

If we want to graph y1 versus x and y2 versus x, the formal way to type
this is

    graph twoway (scatter y1 x) (scatter y2 x)

If we wanted y1 versus x plotted with solid circles and y2 versus x
plotted with hollow circles, formally we would type

    graph twoway (scatter y1 x, ms(O)) (scatter y2 x, ms(Oh))

If we wanted y1 versus x plotted with solid circles and wanted a line
graph for y2 versus x, formally we would type

    graph twoway (scatter y1 x, ms(O)) (line y2 x, sort)

The `sort` option is included under the assumption that the data are not
already sorted by x.

We have shown the formal way to type each of our requests, but few
people would type that. First, most users omit the `graph`:

    twoway (scatter y1 x) (scatter y2 x)
    twoway (scatter y1 x, ms(O)) (scatter y2 x, ms(Oh))
    twoway (scatter y1 x, ms(O)) (line y2 x, sort)

Second, most people use the `||`-separator notation rather than the
`()`-binding notation:

    twoway scatter y1 x || scatter y2 x
    twoway scatter y1 x, ms(O) || scatter y2 x, ms(Oh)
    twoway scatter y1 x, ms(O) || line y2 x, sort

Third, most people now omit the `twoway`:

    scatter y1 x || scatter y2 x
    scatter y1 x, ms(O) || scatter y2 x, ms(Oh)
    scatter y1 x, ms(O) || line y2 x, sort

And finally, most people quickly realize that `scatter` allows us to
plot more than one `y` variable against the same `x` variable:

    scatter y1 y2 x
    scatter y1 y2 x, ms(O Oh)
    scatter y1 x, ms(O) || line y2 x, sort

The third example did not change: in that example, we are combining a
scatterplot and a line plot. Actually, in this particular case, there is
a way we can combine that, too:

    scatter y1 y2 x, ms(O i) connect(. l)

That we can combine `scatter` and `line` just happens to be an oddity of
the examples we picked. It is important to understand that there is
nothing wrong with any of the above ways of typing our request, and
sometimes the wordier syntaxes are the only way to obtain what we want.
If we wanted to graph y1 versus x1 and y2 versus x2, the only way to
type that is

    scatter y1 x1 || scatter y2 x2

or to type the equivalent in one of the wordier syntaxes above it. We
have to do this because `scatter` (see
[<strong>[G-2]</strong> graph twoway scatter](http://www.stata.com/help.cgi?scatter))
draws a scatterplot against one `x` variable. Therefore, if we want two
different `x` variables, we need two different scatters.

In any case, we will often refer to the `graph twoway` command, even
though, when we give the command, we will seldom type the `graph`, and
mostly, we will not type the `twoway` either.
