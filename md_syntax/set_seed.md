## Syntax

<span options="seed">{marker seed}_{nobreak None} `set seed #`

`set rngstate statecode`

`#` is any number between 0 and 2^31-1 (or 2,147,483,647).

`statecode` is a random-number state previously obtained from
[<strong>creturn</strong>](creturn##rngstate)
value `c(rngstate)`.
