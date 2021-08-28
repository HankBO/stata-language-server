## Syntax

Add estimation result currently in memory to model

`forecast estimates name` \[`, options`\]

`name` is the name of a stored estimation result; see
[<strong>[R] estimates store</strong>](http://www.stata.com/help.cgi?estimates%20store).

Add estimation result currently saved on disk to model

`forecast estimates using filename` \[`, number(#) options`\]

`filename` is an estimation results file created by `estimates save`;
see
[<strong>[R] estimates save</strong>](http://www.stata.com/help.cgi?estimates%20save).
If no file extension is specified, `.ster` is assumed.

| Options |                                      | Description                                                  |
|---------|--------------------------------------|--------------------------------------------------------------|
|         | `predict(p_options)`                 | call `predict` using `p_options`                             |
|         | `names(namelist`\[`, replace`\]`)` | use `namelist` for names of left-hand-side variables         |
|         | `advise`                             | advise whether estimation results can be dropped from memory |
