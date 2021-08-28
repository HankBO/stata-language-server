## Syntax

`classutil drop instance` \[`instance` \[...\]\]

`classutil describe object` \[`, recurse newok`\]

`classutil dir` \[`pattern`\] \[`, all detail`\]

`classutil cdir` \[`pattern`\]

`classutil which classname` \[`, all`\]

where

`object`, `instance`, and `classname` may be specified with or without a
leading period.

`instance` and `object` are as defined in
[<strong>classman</strong>](http://www.stata.com/help.cgi?classman):
`object` is an `instance` or a `classname`.

`pattern` is as allowed with the `strmatch()` function: `*` means 0 or
more characters go here, and `?`<span options="1">{space 1}_means
exactly one character goes here.

Command `cutil` is a synonym for `classutil`.
