## Syntax

Set FRED key

`set fredkey key` \[`, permanently`\]

Import FRED data

`import fred series_list` \[`, options`\]

or

`import fred, serieslist(filename)` \[`options`\]

Describe series

`freddescribe series_list` \[`, detail realtime(start end)`\]

Search series

`fredsearch keyword_list` \[`,`
[<var class="command">search_options</var><strong></strong>](import%20fred##searchopts)\]

`key` is a valid API key, which is provided by the St. Louis Federal
Reserve and may be obtained from
[<strong>"https://research.stlouisfed.org/docs/api/api_key.html"</strong>](https://research.stlouisfed.org/docs/api/api_key.html).

`series_list` is a list of FRED codes, for example, `FEDFUNDS`.

`keyword_list` is a list of keywords.

| options                                                          |                                                                                                                                                                                                           | Description                                               |
|------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| \*                                                               | `serieslist(filename)`                                                                                                                                                                                    | specify series IDs using a file                           |
|                                                                  | `daterange(start end)`                                                                                                                                                                                    | restrict to only observations within specified date range |
|                                                                  | `aggregate(`[<var class="command">frequency</var><strong></strong>](#freq) \[`,` [<var class="command">method</var><strong></strong>](#method)\]`)` | specify the aggregation level and aggregation type        |
|                                                                  | `realtime(start end)`                                                                                                                                                                                     | import historical vintages between specified dates        |
|                                                                  | `vintage(datespec)`                                                                                                                                                                                       | import historical data by vintage dates                   |
|                                                                  | `nrobs`                                                                                                                                                                                                   | import only new and revised observations                  |
|                                                                  | `initial`                                                                                                                                                                                                 | import only first value for each observation in a series  |
|                                                                  | `long`                                                                                                                                                                                                    | import data in long format                                |
|                                                                  | `nosummary`                                                                                                                                                                                               | suppress summary table                                    |
|                                                                  | `clear`                                                                                                                                                                                                   | clear data in memory before importing FRED series         |
| \* `serieslist()` is required if `series_list` is not specified. |                                                                                                                                                                                                           |                                                           |
| `clear` does not appear in the dialog box.                       |                                                                                                                                                                                                           |                                                           |

If `start` and `end` are provided as dates, they must be daily dates
using notation of the form `31Jan2016`, `2016-01-31`, `2016/01/31`, or
`01/31/2016`.

`datespec` may be

`datedate_1date_2date_n_all`

| search\_options                               |                                                                                                                                                                                                        | Description                                        |
|-----------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------|
|                                               | `idonly`                                                                                                                                                                                               | require `keywords` to appear in series IDs only    |
|                                               | `tags(tag_list)`                                                                                                                                                                                       | search by `tag_list`                               |
|                                               | `taglist`                                                                                                                                                                                              | list tags present in current search results        |
|                                               | `sort(`[<var class="command">sortby</var><strong></strong>](#sortby)\[`,` [<var class="command">sortorder</var><strong></strong>](#sortorder)\]) | list matched series in order specified by `sortby` |
|                                               | `detail`                                                                                                                                                                                               | list full metainformation for each search result   |
|                                               | `saving(filename` \[`, replace`\]`)`                                                                                                                                                                 | save series information to `filename.dta`        |
| `saving()` does not appear in the dialog box. |                                                                                                                                                                                                        |                                                    |
