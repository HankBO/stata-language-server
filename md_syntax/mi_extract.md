## Syntax

`mi extract #` \[`, options`\]{nobreak None}

where 0 &lt;= `#` &lt;= `M`

| Options |                                                                                                | Description                                     |
|---------|------------------------------------------------------------------------------------------------|-------------------------------------------------|
|         | `clear`                                                                                        | okay to replace unsaved data in memory          |
|         | `esample(`...`)`                                                                               | rarely specified option                         |
|         | `esample(`[varname](http://www.stata.com/help.cgi?varname)`)`       | ...syntax when `#` &gt; 0                       |
|         | `esample(`[varname](http://www.stata.com/help.cgi?varname) `#_e)` | ...syntax when `#` = 0; 1 &lt;= `#_e` &lt;= `M` |
