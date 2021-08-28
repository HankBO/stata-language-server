## Syntax

: `mata matsave filename namelist` \[`, replace` \]

: `mata matuse filename` \[`, replace` \]

: `mata matdescribe filename`

where `namelist` is a list of matrix names as defined in
**[<strong>[M-3] namelists</strong>](http://www.stata.com/help.cgi?m3_namelists)**.

If `filename` is specified without a suffix, `.mmat` is assumed.

These commands are for use in Mata mode following Mata's colon prompt.
To use these commands from Stata's dot prompt, type

`mata: mata matsave`
