## Syntax

Produce a codebook describing value labels

`labelbook` \[`lblname-list`\] \[`, labelbook_options`\]

Prefix numeric values to value labels

`numlabel` \[`lblname-list`\]`,` {`add`\|`remove`}
\[{it:numlabel\_options}\]

Make dataset containing value-label information

`uselabel` \[`lblname-list`\] \[`using filename`\] \[`, clear`
`var`\]

| labelbook\_options |             | Description                                                             |
|--------------------|-------------|-------------------------------------------------------------------------|
|                    | `alpha`     | alphabetize label mappings                                              |
|                    | `length(#)` | check if value labels are unique to length `#`; default is `length(12)` |
|                    | `list(#)`   | list maximum of `#` mappings; default is `list(32000)`                  |
|                    | `problems`  | describe potential problems in a summary report                         |
|                    | `detail`    | do not suppress detailed report on variables or value labels            |

<table id="numlabel_options" class="syntab">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">numlabel_options</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd" style="has_footnote">
<td>*</td>
<td><code class="command" data-options="a">add</code></td>
<td>prefix numeric values to value labels</td>
</tr>
<tr class="even" style="has_footnote">
<td>*</td>
<td><code class="command" data-options="r">remove</code></td>
<td>remove numeric values from value labels</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="m">mask(str)</code></td>
<td>mask for formatting numeric labels; default mask is "<var class="command">#</var><code class="command">.</code>"</td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command" data-options="force">force</code></td>
<td>force adding or removing of numeric labels</td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command" data-options="d">detail</code></td>
<td>provide details about value labels, where some labels are prefixed with numbers and others are not</td>
</tr>
</tbody><tfoot>
<tr class="even footnote">
<td colspan="3">* Either <code class="command">add</code> or <code class="command">remove</code> must be specified. <span data-options="menu">{marker menu}_<span>{nobreak None}_ <span>{title None:Menu}_ <span>{title None:labelbook}_ <span>{phang2 None}_ <strong>Data &gt; Data utilities &gt; Label utilities &gt; Produce codebook of value labels</strong> <span>{title None:numlabel}_ <span>{phang2 None}_ <strong>Data &gt; Data utilities &gt; Label utilities &gt; Prepend values to value labels</strong> <span>{title None:uselabel}_ <span>{phang2 None}_ <strong>Data &gt; Data utilities &gt; Label utilities &gt; Create dataset from value labels</strong> <span data-options="description">{marker description}_<span>{nobreak None}_ <span>{title None:Description}_ <span>{pstd None}_ <code class="command">labelbook</code> displays information for the value labels specified or, if no labels are specified, all the labels in the data. <span>{pstd None}_ For multilingual datasets (see [<strong>[D]</strong> label language](http://www.stata.com/help.cgi?label_language)), <code class="command">labelbook</code> lists the variables to which value labels are attached in all defined languages. <span>{pstd None}_ <code class="command">numlabel</code> prefixes numeric values to value labels. For example, a value mapping of <code class="command">2</code> -&gt; "<code class="command">catholic</code>" will be changed to <code class="command">2</code> -&gt; "<code class="command">2. catholic</code>". See option [<strong>mask()</strong>](#mask()) for the different formats. Stata commands that display the value labels also show the associated numeric values. Prefixes are removed with the <code class="command" data-options="remove">remove</code> option. <span>{pstd None}_ <code class="command">uselabel</code> is a programmer's command that reads the value-label information from the currently loaded dataset or from an optionally specified filename. <span>{pstd None}_ <code class="command">uselabel</code> creates a dataset in memory that contains only that value-label information. The new dataset has four variables named <code class="command" data-options="label">label</code>, <code class="command" data-options="lname">lname</code>, <code class="command" data-options="value">value</code>, and <code class="command" data-options="trunc">trunc</code>; is sorted by <code class="command" data-options="lname value">lname value</code>; and has 1 observation per mapping. Value labels can be longer than the maximum string length in Stata; see [<strong>limits</strong>](http://www.stata.com/help.cgi?limits). The new variable <code class="command" data-options="trunc">trunc</code> contains <code class="command">1</code> if the value label is truncated to fit in a string variable in the dataset created by <code class="command">uselabel</code>. <span>{pstd None}_ <code class="command">uselabel</code> complements <code class="command">label, save</code>, which produces a text file of the value labels in a format that allows easy editing of the value-label texts. <span>{pstd None}_ Specifying no list or <code class="command" data-options="_all">_all</code> is equivalent to specifying all value labels. Value-label names may not be abbreviated or specified with wildcards. <span data-options="linkspdf">{marker linkspdf}_<span>{nobreak None}_ <span>{title None:Links to PDF documentation}_ <a href="http://www.stata.com/manuals14/dlabelbookquickstart.pdf">Quick start</a> <a href="http://www.stata.com/manuals14/dlabelbookremarksandexamples.pdf">Remarks and examples</a> <span>{pstd None}_ The above sections are not included in this help file. <span data-options="options_labelbook">{marker options_labelbook}_<span>{nobreak None}_ <span>{title None:Options for labelbook}_ <span>{phang None}_ <code class="command" data-options="alpha">alpha</code> specifies that the list of value-label mappings be sorted alphabetically on label. The default is to sort the list on value. <span>{phang None}_ <code class="command" data-options="length(#)">length(#)</code> specifies the minimum length that <code class="command">labelbook</code> checks to determine whether shortened value labels are still unique. It defaults to <code class="command" data-options="12">12</code>, the width used by most Stata commands. <code class="command">labelbook</code> also reports whether value labels are unique at their full length. <span>{phang None}_ <code class="command" data-options="list(#)">list(#)</code> specifies the maximum number of value-label mappings to be listed. If a value label defines more mappings, a random subset of <var class="command">#</var> mappings is displayed. By default, <code class="command">labelbook</code> displays all mappings. <code class="command">list(0)</code> suppresses the listing of the value-label definitions. <span>{phang None}_ <code class="command">problems</code> specifies that a summary report be produced describing potential problems that were diagnosed:
1. Value label has gaps in mapped values (for example, values 0 and 2 are labeled, while 1 is not)</td>
</tr>
<tr class="odd footnote">
<td colspan="3">2. Value label strings contain leading or trailing blanks</td>
</tr>
<tr class="even footnote">
<td colspan="3">3. Value label contains duplicate labels, that is, there are different values that map into the same string.</td>
</tr>
<tr class="odd footnote">
<td colspan="3">4. Value label contains duplicate labels at length 12</td>
</tr>
<tr class="even footnote">
<td colspan="3">5. Value label contains numeric -&gt; numeric mappings</td>
</tr>
<tr class="odd footnote">
<td colspan="3">6. Value label contains numeric -&gt; null string mappings</td>
</tr>
<tr class="even footnote">
<td colspan="3">7. Value label is not used by variables</td>
</tr>
</tfoot>

</table>

See
[<strong>labelbook_problems</strong>](http://www.stata.com/help.cgi?labelbook_problems)
for a discussion of these problems and advice on overcoming them.

`detail` may be specified only with `problems`. It specifies that the
detailed report on the variables or value labels not be suppressed.
