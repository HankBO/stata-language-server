## Syntax

`void`<span class="nowrap"> _ `timer_clear()`

`void`<span class="nowrap"> _ `timer_clear(real scalar t)`

`void`<span class="nowrap"> _ `timer_on(real scalar t)`

`void`<span class="nowrap"> _ `timer_off(real scalar t)`

`real rowvector timer_value(real scalar t)`

`void`<span class="nowrap"> _ `timer()`

`void`<span class="nowrap"> _ `timer(real t)`

`void`<span class="nowrap"> _ `timer(string scalar txt)`

`void`<span class="nowrap"> _ `timer(real t,`
`string scalar txt)`

`void`<span class="nowrap"> _ `timer(string scalar txt,`
`real t)`

where `t` is a timer number, 1 through 100.

For `timer()`, zero, one, or two arguments are allowed, and arguments
may be specified in any order. Argument `t` may be omitted, specified as
a `scalar`, or specified as a `vector`:

If `t` is omitted, all timers are reported.

If `t` is a `scalar`, the specified timer is reported (`timer(.)` is the
same as omitting `t`; all timers are reported).

If `t` is a `rowvector`, the specified timers are reported.

If `t` is a `colvector`, it must be 2 `x` 1, and the timers in the range
are reported.

For `timer_clear()`, `t` may be omitted or specified as a scalar:

If `t` is omitted, all timers are cleared.

If `t` is a `scalar`, the specified timer is cleared unless `t` is
specified as missing, in which case the result is the same as if `t` had
been omitted; all timers are cleared.

In the other functions, `t` is a scalar and may not contain missing
values.
