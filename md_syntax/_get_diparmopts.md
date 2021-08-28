## Syntax

`_get_diparmopts` \[`, diparmopts(diparm_options) execute bottom`
`plus global_diparm_options` \]

`_get_diparmopts , soptions` \[ `diparmopts(options) execute`
`bottom plus global_diparm_options` \]

where `options` is any collection of options (including
`diparm_options`), `diparm_options` contains one or more of

`diparm(diparm_args)`

`diparm_args` is either "`__sep__`" or anything allowed by the `_diparm`
(see
[<strong>[P]</strong> _diparm](http://www.stata.com/help.cgi?_diparm))
command (except the `level(#)` option), and `global_diparm_options` is
one or more of

`level(#) dof(#)`
