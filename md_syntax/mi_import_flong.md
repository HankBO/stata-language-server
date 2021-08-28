## Syntax

`mi import flong, required_options` \[`true_options`\]

| required\_options |                                                                                     | Description                     |
|-------------------|-------------------------------------------------------------------------------------|---------------------------------|
|                   | `m(`[varname](http://www.stata.com/help.cgi?varname)`)`  | name of variable containing `m` |
|                   | `id(`[varlist](http://www.stata.com/help.cgi?varlist)`)` | identifying variable(s)         |

| true\_options |                                                                                          | Description                            |
|---------------|------------------------------------------------------------------------------------------|----------------------------------------|
|               | `imputed(`[varlist](http://www.stata.com/help.cgi?varlist)`)` | imputed variables to be registered     |
|               | `passive(`[varlist](http://www.stata.com/help.cgi?varlist)`)` | passive variables to be registered     |
|               | `clear`                                                                                  | okay to replace unsaved data in memory |
