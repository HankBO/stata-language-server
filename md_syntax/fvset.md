## Syntax

Declare base settings

`fvset base base_spec`
[varlist](http://www.stata.com/help.cgi?varlist)

Declare design settings

`fvset design design_spec`
[varlist](http://www.stata.com/help.cgi?varlist)

Clear the current settings

`fvset clear`
[varlist](http://www.stata.com/help.cgi?varlist)

Report the current settings

`fvset report`
\[[varlist](http://www.stata.com/help.cgi?varlist)\]
\[`, base(base_spec) design(design_spec)`\]

| base\_spec |            | Description                     |
|------------|------------|---------------------------------|
|            | `default`  | default base                    |
|            | `first`    | lowest level value; the default |
|            | `last`     | highest level value             |
|            | `frequent` | most frequent level value       |
|            | `none`     | no base                         |
|            | `#`        | nonnegative integer value       |

| design\_spec |              | Description                                                 |
|--------------|--------------|-------------------------------------------------------------|
|              | `default`    | default design                                              |
|              | `asbalanced` | accumulate using 1/k, k = number of levels                  |
|              | `asobserved` | accumulate using observed relative frequencies; the default |
