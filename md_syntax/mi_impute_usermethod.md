## Syntax

`mi impute usermethod userspec` \[`, options`\]

`usermethod` is the name of the method you would like to add to the
`mi impute` command. When naming an `mi impute` method, you should
follow the same convention as for naming the programs you add to Stata
-- do not pick "nice" names that may later be used by Stata's official
methods.

`userspec` is a specification of an imputation model as supported by the
user-defined method `usermethod`. It must include imputation variables
`ivars`. It may also include independent variables `indepvars`,
[<strong>weight</strong>](http://www.stata.com/help.cgi?weight)s,
and an
[<var class="command">if</var><strong></strong>](http://www.stata.com/help.cgi?if)
qualifier if those things are also supported by `usermethod`. The actual
syntax of `userspec` will be specific to `usermethod`. We encourage
users who are adding their own methods to `mi impute` to follow
[<strong>mi impute</strong>](http://www.stata.com/help.cgi?mi%20impute)'s
syntax or Stata's general
[<strong>syntax</strong>](http://www.stata.com/help.cgi?syntax)
when designing their methods.

| options                                                                                                                                                                                                |                  | Description                                                                                                            |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------|------------------------------------------------------------------------------------------------------------------------|
|                                                                                                                                                                                                        | `impute_options` | any option of [<strong>mi impute</strong>](mi_impute##impopts) except `noupdate` and `by()` |
|                                                                                                                                                                                                        | `orderasis`      | impute variables in the specified order                                                                                |
|                                                                                                                                                                                                        | `user_options`   | additional options supported by `usermethod`                                                                           |
| You must `mi set` your data before using `mi impute usermethod`; see [<strong>[MI]</strong> mi set](http://www.stata.com/help.cgi?mi_set).                              |                  |                                                                                                                        |
| You must `mi register` imputation variables as `imputed` before using `mi impute usermethod`; see [<strong>[MI]</strong> mi set](http://www.stata.com/help.cgi?mi_set). |                  |                                                                                                                        |
