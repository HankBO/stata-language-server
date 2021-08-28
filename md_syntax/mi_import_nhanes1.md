## Syntax

`mi import nhanes1 name, required_options` \[`true_options`
`odd_options`\]

where `name` is the name of the flongsep data to be created.

| required\_options                                                                                                                                                                    |                                                                                     | Description                            |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|----------------------------------------|
|                                                                                                                                                                                      | `using(filenamelist)`                                                           | input filenames for `m`=1, `m`=2, ...  |
|                                                                                                                                                                                      | `id(`[varlist](http://www.stata.com/help.cgi?varlist)`)` | identifying variable(s)                |
|                                                                                                                                                                                      | `clear`                                                                             | okay to replace unsaved data in memory |
| Note: `use` the input file for `m`=0 before issuing `mi import nhanes1`. {synopthdr None:true\_options} {synoptline None} {synopt None}`uppercase`prefix and suffix in uppercase |                                                                                     |                                        |

<table class="syntab">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">odd_options</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td class="normal"></td>
<td><code class="command">nacode(</code><var class="command">#</var><code class="command">)</code></td>
<td>not applicable code; default is <code class="command">0</code></td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command">obscode(</code><var class="command">#</var><code class="command">)</code></td>
<td>observed code; default is <code class="command">1</code></td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command">impcode(</code><var class="command">#</var><code class="command">)</code></td>
<td>imputed code; default is <code class="command">2</code></td>
</tr>
<tr class="even">
<td class="normal"></td>
<td><code class="command">impprefix("</code><var class="command">string</var><code class="command">" "</code><var class="command">string</var><code class="command">")</code></td>
<td>variable prefix; default is <code class="command">"" ""</code></td>
</tr>
<tr class="odd">
<td class="normal"></td>
<td><code class="command">impsuffix("</code><var class="command">string</var><code class="command">" "</code><var class="command">string</var><code class="command">")</code></td>
<td>variable suffix; default is <code class="command">"if" "mi"</code></td>
</tr>
</tbody><tfoot>
<tr class="even footnote">
<td colspan="3">Note: The <var class="command">odd_options</var> are not specified unless you need to import data that are nhanes1-like but not really nhanes1 format. <span data-options="menu">{marker menu}_<span>{nobreak None}_ <span>{title None:Menu}_ <span>{phang None}_ <strong>Statistics &gt; Multiple imputation</strong> <span data-options="description">{marker description}_<span>{nobreak None}_ <span>{title None:Description}_
<code class="command">mi</code> <code class="command">import</code> <code class="command">nhanes1</code> imports data recorded in the format used by the National Health and Nutrition Examination Survey (NHANES) produced by the National Center for Health Statistics (NCHS) of the U.S. Centers for Disease Control and Prevention (CDC); see [<strong>"https://www.cdc.gov/nchs/data/nhanes/nhanes3/dna_secondary_data_analysis_guidelines.pdf"</strong>](https://www.cdc.gov/nchs/data/nhanes/nhanes3/dna_secondary_data_analysis_guidelines.pdf). <span data-options="linkspdf">{marker linkspdf}_<span>{nobreak None}_ <span>{title None:Links to PDF documentation}_ <a href="http://www.stata.com/manuals14/mimiimportnhanes1remarksandexamples.pdf">Remarks and examples</a> <span>{pstd None}_ The above sections are not included in this help file. <span data-options="options">{marker options}_<span>{nobreak None}_ <span>{title None:Options}_
<code class="command">using(</code><var class="command">filenamelist</var><code class="command">)</code> is required; it specifies the names of the <code class="command">.dta</code> datasets containing <var class="command">m</var>=1, <var class="command">m</var>=2, ..., <var class="command">m</var>=<var class="command">M</var>. The dataset corresponding to <var class="command">m</var>=0 is not specified; it is to be in memory at the time the <code class="command">mi</code> <code class="command">import</code> <code class="command">nhanes1</code> command is given.
The filenames might be specified as
<code class="command">using(nh1 nh2 nh3 nh4 nh5)</code>
which states that <var class="command">m</var>=1 is in file <code class="command">nh1.dta</code>, <var class="command">m</var>=2 is in file <code class="command">nh2.dta</code>, ..., and <var class="command">m</var>=5 is in file <code class="command">nh5.dta</code>. Also, <code class="command">{c -(}</code><var class="command">#</var><code class="command">-</code><var class="command">#</var><code class="command">{c )-}</code> is understood, so the files could just as well be specified as
<code class="command">using(nh{c -(}1-5{c )-})</code>
The braced numeric range may appear anywhere in the name, and thus
<code class="command">using(nh{c -(}1-5{c )-}imp)</code>
would mean that <code class="command">nh1imp.dta</code>, <code class="command">nh2imp.dta</code>, ..., <code class="command">nh5imp.dta</code> contain <var class="command">m</var>=1, <var class="command">m</var>=2, ..., <var class="command">m</var>=5.
Alternatively, a comma-separated list can appear inside the braces. Filenames <code class="command">nhfirstm.dta</code>, <code class="command">nhsecondm.dta</code>, ..., <code class="command">nhfifthm.dta</code> can be specified as
<code class="command">using(nh{c -(}first,second,third,fourth,fifth{c )-}m)</code>
Filenames can be specified with or without the <code class="command">.dta</code> suffix and must be enclosed in quotes if they contain special characters.
<code class="command">id(</code>[varlist](http://www.stata.com/help.cgi?varlist)<code class="command">)</code> is required and is usually specified as <code class="command">id(seqn)</code> or <code class="command">id(SEQN)</code> depending on whether your variable names are in lowercase or uppercase. <code class="command">id()</code> specifies the variable or variables that uniquely identify the observations in each dataset. Per the nhanes1 standard, the variable should be named <code class="command">seqn</code> or <code class="command">SEQN</code>.
<code class="command">uppercase</code> is optional; it specifies that the variable suffixes <code class="command">IF</code> and <code class="command">MI</code> of the nhanes1 standard are in uppercase. The default is lowercase. (More correctly, when generalizing beyond nhanes1 format, the <code class="command">uppercase</code> option specifies that all prefixes and suffixes are in uppercase.)
<code class="command">nacode(</code><var class="command">#</var><code class="command">)</code>, <code class="command">obscode(</code><var class="command">#</var><code class="command">)</code>, and <code class="command">impcode(</code><var class="command">#</var><code class="command">)</code> are optional and are never specified when reading true nhanes1 data. The defaults <code class="command">nacode(0)</code>, <code class="command">obscode(1)</code>, and <code class="command">impcode(2)</code> correspond to the nhanes1 definition. These options allow changing the codes for not applicable, observed, and imputed.
<code class="command">impprefix("</code><var class="command">string</var><code class="command">"</code> <code class="command">"</code><var class="command">string</var><code class="command">")</code> and <code class="command">impsuffix("</code><var class="command">string</var><code class="command">"</code> <code class="command">"</code><var class="command">string</var><code class="command">")</code> are optional and are never specified when reading true nhanes1 data. The defaults <code class="command">impprefix(""</code> <code class="command">"")</code> and <code class="command">impsuffix("if"</code> <code class="command">"mi")</code> correspond to the nhanes1 definition. These options allow setting different prefixes and suffixes.
<code class="command">clear</code> specifies that it is okay to replace the data in memory even if they have changed since they were saved to disk. Remember, <code class="command">mi</code> <code class="command">import</code> <code class="command">nhanes1</code> starts with the first of the NHANES data in memory and ends with <code class="command">mi</code> data in memory. <span data-options="remarks">{marker remarks}_<span>{nobreak None}_ <span>{title None:Remarks}_
Remarks are presented under the following headings: [<strong>Description of the nhanes1 format</strong>](#format) [<strong>Importing nhanes1 data</strong>](#example) <span data-options="format">{marker format}_<span>{nobreak None}_ <span>{title None:Description of the nhanes1 format}_
Nhanes1 is not really an official format; it is the format used for a particular dataset distributed by NCHS. Because there currently are no official or even informal standards for multiple-imputation data, perhaps the method used by the NCHS for NHANES will catch on, so we named it nhanes1. We included the 1 on the end of the name in case the format is modified.
Data in nhanes1 format consist of a collection of <var class="command">M</var>+1 separate files. The first file contains the original data. The remaining <var class="command">M</var> files contain the imputed values for <var class="command">m</var>=1, <var class="command">m</var>=2, ..., <var class="command">m</var>=<var class="command">M</var>.
The first file contains a variable named <code class="command">seqn</code> containing a sequence number. The file also contains other variables that comprise the nonimputed variables. Imputed variables, however, have their names suffixed with <code class="command">IF</code>, standing for imputation flag, and those variables contain 1s, 2s, and 0s. 1 means that the value of the variable in that observation was observed, 2 means that the value was missing, and 0 means not applicable. Think of 0 as being equivalent to hard missing. The value is not observed for good reason and therefore was not imputed.
The remaining <var class="command">M</var> files contain <code class="command">seqn</code> and the imputed variables themselves. In these files, unobserved values are imputed. This time, imputed variable names are suffixed with <code class="command">MI</code>.
Here is an example: . <code class="command">use http://www.stata-press.com/data/r15/nhorig</code> . <code class="command">list</code>
The above is the first of the <var class="command">M</var>+1 datasets. The <code class="command">seqn</code> variable is the sequence number. The <code class="command">a</code> variable is a regular variable; we know that because the name does not end in <code class="command">IF</code>. The <code class="command">b</code> and <code class="command">c</code> variables are imputed, and this dataset contains their imputation flags. Both variables are observed in the first observation and unobserved in the second.
Here is the corresponding dataset for <var class="command">m</var>=1: . <code class="command">use nh1</code> . <code class="command">list</code>
This dataset states that in <var class="command">m</var>=1, <code class="command">b</code> is equal to 2 and 4.5 and <code class="command">c</code> is equal to 3 and 8.5.
We are about to show you the dataset for <var class="command">m</var>=2. Even before looking at it, however, we know that 1) it will have two observations; 2) it will have the <code class="command">seqn</code> variable containing 1 and 2; 3) it will have two more variables named <code class="command">bMI</code> and <code class="command">cMI</code>; and 4) <code class="command">bMI</code> will be equal to 2 and <code class="command">cMI</code> will be equal to 3 in observations corresponding to <code class="command">seqn</code>=1. We know the last because in the first dataset, we learned that <code class="command">b</code> and <code class="command">c</code> were observed in <code class="command">seqn</code>=1. . <code class="command">use nh2</code> . <code class="command">list</code> <span data-options="example">{marker example}_<span>{nobreak None}_ <span>{title None:Importing nhanes1 data}_
The procedure to import nhanes1 data is this:
1. <strong>[<strong>use</strong>](http://www.stata.com/help.cgi?use)</strong> the dataset corresponding to <var class="command">m</var>=0.
2. Issue <code class="command">mi</code> <code class="command">import</code> <code class="command">nhanes1</code> <var class="command">name</var> ..., where <var class="command">name</var> is the name of the <code class="command">mi</code> flongsep datasets to be created.
3. Perform the checks outlined in <var class="command">Using mi import nhanes1, ice, flong, and flongsep</var> of <strong>[<strong>[MI] mi import</strong>](http://www.stata.com/help.cgi?mi_import)</strong>.
4. Use <strong>[<strong>mi convert</strong>](http://www.stata.com/help.cgi?mi_convert)</strong> to convert the data to a more convenient style such as wide, mlong, or flong.
To import the <code class="command">nhorig.dta</code>, <code class="command">nh1.dta</code>, and <code class="command">nh2.dta</code> datasets described in the section above, we will specify <code class="command">mi</code> <code class="command">import</code> <code class="command">nhanes1</code>'s <code class="command">uppercase</code> option because the suffixes were in uppercase. We type . <code class="command">use nhorig</code> . <code class="command">mi import nhanes1 mymi, using(nh1 nh2) id(seqn) uppercase</code>
The lack of any error message means that we have successfully converted nhanes1-format files <code class="command">nhorig.dta</code>, <code class="command">nh1.dta</code>, and <code class="command">nh2.dta</code> to <code class="command">mi</code> flongsep files <code class="command">mymi.dta</code>, <code class="command">_1_mymi.dta</code>, and <code class="command">_2_mymi.dta</code>.
We will now perform the checks outlined in <var class="command">Using mi import nhanes1, ice, flong, and flongsep</var> of <strong>[<strong>[MI] mi import</strong>](http://www.stata.com/help.cgi?mi_import)</strong>, which are to run <code class="command">mi</code> <code class="command">describe</code> and <code class="command">mi</code> <code class="command">varying</code> (see <strong>[<strong>[MI] mi describe</strong>](http://www.stata.com/help.cgi?mi_describe)</strong> and <strong>[<strong>[MI] mi varying</strong>](http://www.stata.com/help.cgi?mi_varying)</strong>) to verify that variables are registered correctly: . <code class="command">mi describe</code> . <code class="command">mi varying</code>
<code class="command">mi varying</code> reported no problems.
We finally convert to style flong, although in real life we would choose styles mlong or wide. We are choosing flong because it is more readable: . <code class="command">mi convert flong, clear</code> . <code class="command">list, separator(2)</code>
The flong data are in memory. We are done with the converted data in flongsep format, so we erase the files: . <code class="command">mi erase mymi</code></td>
</tr>
</tfoot>

</table>
