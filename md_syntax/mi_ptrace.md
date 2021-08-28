## Syntax

`mi ptrace describe` \[`using`\] `filename`

`mi ptrace use filename` \[`, use_options`\]

| use\_options |                          | Description                                   |
|--------------|--------------------------|-----------------------------------------------|
|              | `clear`                  | okay to replace existing data in memory       |
|              | `double`                 | load variables as doubles (default is floats) |
|              | `select(selections)` | what to load (default is all)                 |

where `selections` is a space-separated list of individual selections.
Individual selections are of the form

`b[yname,xname]v[yname,yname]`

where `yname`s and `xname`s are displayed by `mi ptrace describe`.
You may also specify

`b[#_y,#_x]v[#_y,#_y]`

where `#_y` and `#_x` are the variable numbers associated with `yname`
and `xname`, and those too are shown by `mi ptrace describe`.

For `b`, you may also specify `*` to mean all possible index elements.
For instance,

`b[*,*]`<span style="padding-left: 19.0rem;">_all elements of `b`

`b[yname,*]`<span style="padding-left: 19.0rem;">_row
corresponding to `yname`

`b[*,xname]`<span style="padding-left: 19.0rem;">_column
corresponding to `xname`

Similarly, `b[#_y,*]` and `b[*,#_x]` are allowed. The same is
allowed for `v`, and also, the second element can be specified as `<`,
`<=`, `=`, `>=`, or `>`. For instance,

`v[yname,=]`<span style="padding-left: 19.0rem;">_variance of
`yname`

`v[*,=]`<span style="padding-left: 19.0rem;">_all variances
(diagonal elements)

`v[*,<]`<span style="padding-left: 19.0rem;">_lower triangle

`v[*,<=]`<span style="padding-left: 19.0rem;">_lower triangle
and diagonal

`v[*,>=]`<span style="padding-left: 19.0rem;">_upper triangle
and diagonal

`v[*,>]`<span style="padding-left: 19.0rem;">_upper triangle

In `mi ptrace describe` and in `mi ptrace use`, `filename` must
be specified in quotes if it contains special characters or blanks.
`filename` is assumed to be `filename.stptrace` if the suffix is not
specified.
