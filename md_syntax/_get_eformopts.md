## Syntax

`_get_eformopts` \[`, eformopts(eform_options)`
`allowed:(allow_options)`\]

`_get_eformopts , soptions` \[`eformopts(options)`
`allowed:(allow_options)`\]

where `eform_options` is at most one of

`eform:(string) eform hr irr or rrr`

`allow_options` is either `__all__` or an option specification allowed
by the `syntax` command, such as

`hr IRr or RRr`

(`EForm` is implied) and `options` is any collection of options,
including `eform_options`.
