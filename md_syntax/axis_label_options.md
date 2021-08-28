## Syntax

`axis_label_options` are a subset of `axis_options`; see
[<strong>[G-3]</strong> <em>axis_options</em>](http://www.stata.com/help.cgi?axis_options).
`axis_label_options` control the placement and the look of ticks and
labels on an axis.

<table class="standard">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><var class="command">axis_label_options</var></td>
<td>Description <span>{p2line None}_</td>
</tr>
<tr class="even">
<td><span data-options="-(">{c -(}_<code class="command">y</code>|<code class="command">x</code>|<code class="command">t</code>|<code class="command">z</code><span data-options=")-">{c )-}_<code class="command">label:(</code><var class="command">rule_or_values</var><code class="command">)</code></td>
<td>major ticks plus labels</td>
</tr>
<tr class="odd">
<td><span data-options="-(">{c -(}_<code class="command">y</code>|<code class="command">x</code>|<code class="command">t</code>|<code class="command">z</code><span data-options=")-">{c )-}_<code class="command">tick:(</code><var class="command">rule_or_values</var><code class="command">)</code></td>
<td>major ticks only</td>
</tr>
<tr class="even">
<td><span data-options="-(">{c -(}_<code class="command">y</code>|<code class="command">x</code>|<code class="command">t</code>|<code class="command">z</code><span data-options=")-">{c )-}_<code class="command">mlabel:(</code><var class="command">rule_or_values</var><code class="command">)</code></td>
<td>minor ticks plus labels</td>
</tr>
<tr class="odd">
<td><span data-options="-(">{c -(}_<code class="command">y</code>|<code class="command">x</code>|<code class="command">t</code>|<code class="command">z</code><span data-options=")-">{c )-}_<code class="command">mtick:(</code><var class="command">rule_or_values</var><code class="command">)</code></td>
<td>minor ticks only <span>{p2line None}_
The above options are <var class="command">merged-explicit</var>; see [<strong>[G-4]</strong> concept:repeated options](http://www.stata.com/help.cgi?repeated_options).</td>
</tr>
</tbody>
</table>

where `rule_or_values` is defined as

\[`rule`\] \[`numlist` \[`"label"` \[`numlist` \[`"label"`
\[...\]\]\]\]\] \[`, suboptions`\]

Either `rule` or `numlist` must be specified, and both may be specified.

`rule`

Example<span style="padding-left: 13.0rem;">_Description

------------------------------------------------------------------------

`##`

`#6`{nobreak None}

approximately 6 nice values

`###`

`##10`{nobreak None}

10-1=9 values between major ticks;

allowed with `mlabel()` and `mtick()` only

`#(#)#`

`-4(.5)3`{nobreak None}

specified range: -4 to 3 in steps of .5

`minmax`

`minmax`{nobreak None}

minimum and maximum values

`none`

`none`{nobreak None}

label no values

`.`

`.`{nobreak None}

skip the rule

------------------------------------------------------------------------

where `numlist` is as described in
[<strong>[U]</strong> 11.1.8 numlist](http://www.stata.com/help.cgi?numlist).

`tlabel()`, `ttick()`, `tmlabel()`, and `tmtick()` also accept a
`datelist` and an extra type of `rule`

`rule`

Example<span style="padding-left: 18.0rem;">_Description

------------------------------------------------------------------------

`date(#)date`

`1999m1(1)1999m12`{nobreak None}

specified date range: each month

assuming the axis has the `%tm` format

------------------------------------------------------------------------

where `date` and `datelist` may contain dates, provided that the `t`
(time) axis has a date format; see
[<strong>[U]</strong> 11.1.9 datelist](http://www.stata.com/help.cgi?datelist).

<table class="standard">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><var class="command">suboptions</var></td>
<td>Description <span>{p2line None}_</td>
</tr>
<tr class="even">
<td><code class="command">axis:(</code><var class="command">#</var><code class="command">)</code></td>
<td>which axis, <code class="command">1</code>
<ul>
</ul>
<var class="command">#</var>
<ul>
</ul>
<code class="command">9</code></td>
</tr>
<tr class="odd">
<td><code class="command">add</code></td>
<td>combine options</td>
</tr>
<tr class="even">
<td>[<code class="command">no</code>]<code class="command">ticks</code></td>
<td>suppress ticks</td>
</tr>
<tr class="odd">
<td>[<code class="command">no</code>]<code class="command">labels</code></td>
<td>suppress labels</td>
</tr>
<tr class="even">
<td><code class="command">valuelabel</code></td>
<td>label values using first variable's value label</td>
</tr>
<tr class="odd">
<td><code class="command">format(</code>[<strong>%</strong><var class="command">fmt</var><strong></strong>](http://www.stata.com/help.cgi?format)<code class="command">)</code></td>
<td>format values per <code class="command">%</code><var class="command">fmt</var></td>
</tr>
<tr class="even">
<td><code class="command">angle(</code><var class="command">anglestyle</var><code class="command">)</code></td>
<td>angle the labels</td>
</tr>
<tr class="odd">
<td><code class="command">alternate</code></td>
<td>offset adjacent labels</td>
</tr>
<tr class="even">
<td><code class="command">norescale</code></td>
<td>do not rescale the axis</td>
</tr>
<tr class="odd">
<td><code class="command">tstyle:(</code><var class="command">tickstyle</var><code class="command">)</code></td>
<td>labels and ticks: overall style</td>
</tr>
<tr class="even">
<td><code class="command">labgap(</code><var class="command">relativesize</var><code class="command">)</code></td>
<td>labels: margin between tick and label</td>
</tr>
<tr class="odd">
<td><code class="command">labstyle(</code><var class="command">textstyle</var><code class="command">)</code></td>
<td>labels: overall style</td>
</tr>
<tr class="even">
<td><code class="command">labsize:(</code><var class="command">textsizestyle</var><code class="command">)</code></td>
<td>labels: size of text</td>
</tr>
<tr class="odd">
<td><code class="command">labcolor:(</code><var class="command">colorstyle</var><code class="command">)</code></td>
<td>labels: color and opacity of text</td>
</tr>
<tr class="even">
<td><code class="command">tlength:(</code><var class="command">relativesize</var><code class="command">)</code></td>
<td>ticks: length</td>
</tr>
<tr class="odd">
<td><code class="command">tposition:(</code><code class="command">outside</code>|<code class="command">crossing</code>|</td>
<td></td>
</tr>
<tr class="even">
<td data-options="14 37 39 2"><code class="command">inside:)</code></td>
<td>ticks: position/direction</td>
</tr>
<tr class="odd">
<td><code class="command">tlstyle:(</code><var class="command">linestyle</var><code class="command">)</code></td>
<td>ticks: linestyle of</td>
</tr>
<tr class="even">
<td><code class="command">tlwidth:(</code><var class="command">linewidthstyle</var><code class="command">)</code></td>
<td>ticks: thickness of line</td>
</tr>
<tr class="odd">
<td><code class="command">tlcolor:(</code><var class="command">colorstyle</var><code class="command">)</code></td>
<td>ticks: color and opacity of line</td>
</tr>
<tr class="even">
<td><code class="command">custom</code></td>
<td>tick- and label-rendition options apply only to these labels</td>
</tr>
<tr class="odd">
<td>[<code class="command">no</code>]<code class="command">grid</code></td>
<td>grid: include</td>
</tr>
<tr class="even">
<td>[<code class="command">no</code>]<code class="command">gmin</code></td>
<td>grid: grid line at minimum</td>
</tr>
<tr class="odd">
<td>[<code class="command">no</code>]<code class="command">gmax</code></td>
<td>grid: grid line at maximum</td>
</tr>
<tr class="even">
<td><code class="command">gstyle:(</code><var class="command">gridstyle</var><code class="command">)</code></td>
<td>grid: overall style</td>
</tr>
<tr class="odd">
<td>[<code class="command">no</code>]<code class="command">gextend</code></td>
<td>grid: extend into plot region margin</td>
</tr>
<tr class="even">
<td><code class="command">glstyle:(</code><var class="command">linestyle</var><code class="command">)</code></td>
<td>grid: linestyle of</td>
</tr>
<tr class="odd">
<td><code class="command">glwidth:(</code><var class="command">linewidthstyle</var><code class="command">)</code></td>
<td>grid: thickness of line</td>
</tr>
<tr class="even">
<td><code class="command">glcolor:(</code><var class="command">colorstyle</var><code class="command">)</code></td>
<td>grid: color and opacity of line</td>
</tr>
<tr class="odd">
<td><code class="command">glpattern(</code><var class="command">linepatternstyle</var><code class="command">)</code></td>
<td>grid: line pattern of line <span>{p2line None}_</td>
</tr>
</tbody>
</table>
