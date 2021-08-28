## Syntax

<span class="nowrap"> _ `S = solvenl_init()`

`(varies)`<span class="nowrap"> _
[<strong>solvenl_init_type(</strong><var class="command">S</var> [<strong>,</strong> <span data-options="-(">{c -(}_<strong>"fixedpoint"</strong> | <strong>"zero"</strong><span data-options=")-">{c )-}_]<strong>)</strong>](#init_type)

`(varies)`<span class="nowrap"> _
[<strong>solvenl_init_startingvals(</strong><var class="command">S</var> [<strong>,</strong> <var class="command">real colvector ivals</var>]<strong>)</strong>](#init_startingvals)

`(varies)`<span class="nowrap"> _
[<strong>solvenl_init_numeq(</strong><var class="command">S</var> [<strong>,</strong> <var class="command">real scalar nvars</var>]<strong>)</strong>](#init_numeq)

`(varies)`<span class="nowrap"> _
[<strong>solvenl_init_technique(</strong><var class="command">S</var> [<strong>,</strong> <strong>"</strong><var class="command">technique</var><strong>"</strong>]<strong>)</strong>](#init_technique)

`(varies)`<span class="nowrap"> _
[<strong>solvenl_init_conv_iterchng(</strong><var class="command">S</var> [<strong>,</strong> <var class="command">real scalar itol</var>]<strong>)</strong>](#init_conv_iterchng)

`(varies)`<span class="nowrap"> _
[<strong>solvenl_init_conv_nearzero(</strong><var class="command">S</var> [<strong>,</strong> <var class="command">real scalar ztol</var>]<strong>)</strong>](#init_conv_nearzero)

`(varies)`<span class="nowrap"> _
[<strong>solvenl_init_conv_maxiter(</strong><var class="command">S</var> [<strong>,</strong> <var class="command">real scalar maxiter</var>]<strong>)</strong>](#init_conv_maxiter)

`(varies)`<span class="nowrap"> _
[<strong>solvenl_init_evaluator(</strong><var class="command">S</var> [<strong>,</strong> <strong>&amp;</strong><var class="command">evaluator</var><strong>()</strong>]<strong>)</strong>](#init_evaluator)

`(varies)`<span class="nowrap"> _
[<strong>solvenl_init_argument(</strong><var class="command">S</var><strong>,</strong> <var class="command">real scalar k</var> [<strong>,</strong> <var class="command">X</var>]<strong>)</strong>](#init_argument)

`(varies)`<span class="nowrap"> _
[<strong>solvenl_init_narguments(</strong><var class="command">S</var> [<strong>,</strong> <var class="command">real scalar K</var>]<strong>)</strong>](#init_narguments)

`(varies)`<span class="nowrap"> _
[<strong>solvenl_init_damping(</strong><var class="command">S</var> [<strong>,</strong> <var class="command">real scalar damp</var>]<strong>)</strong>](#init_damping)

`(varies)`<span class="nowrap"> _
[<strong>solvenl_init_iter_log(</strong><var class="command">S</var> [<strong>,</strong> <span data-options="-(">{c -(}_<strong>"on"</strong> | <strong>"off"</strong><span data-options=")-">{c )-}_]<strong>)</strong>](#init_iter_log)

`(varies)`<span class="nowrap"> _
[<strong>solvenl_init_iter_dot(</strong><var class="command">S</var> [<strong>,</strong> <span data-options="-(">{c -(}_<strong>"on"</strong> | <strong>"off"</strong><span data-options=")-">{c )-}_]<strong>)</strong>](#init_iter_dot)

`(varies)`<span class="nowrap"> _
[<strong>solvenl_init_iter_dot_indent(</strong><var class="command">S</var> [<strong>,</strong> <var class="command">real scalar indent</var>]<strong>)</strong>](#init_iter_dot_indent)

`real colvector`<span class="nowrap"> _
[<strong>solvenl_solve(</strong><var class="command">S</var><strong>)</strong>](#solve)

`real scalar`<span class="nowrap"> _
[<strong>_solvenl_solve(</strong><var class="command">S</var><strong>)</strong>](#_solve)

`real scalar`<span class="nowrap"> _
[<strong>solvenl_result_converged(</strong><var class="command">S</var><strong>)</strong>](#result_converged)

`real scalar`<span class="nowrap"> _
[<strong>solvenl_result_conv_iter(</strong><var class="command">S</var><strong>)</strong>](#result_conv_iter)

`real scalar`<span class="nowrap"> _
[<strong>solvenl_result_conv_iterchng(</strong><var class="command">S</var><strong>)</strong>](#result_conv_iterchng)

`real scalar`<span class="nowrap"> _
[<strong>solvenl_result_conv_nearzero(</strong><var class="command">S</var><strong>)</strong>](#result_conv_nearzero)

`real colvector`<span class="nowrap"> _
[<strong>solvenl_result_values(</strong><var class="command">S</var><strong>)</strong>](#result_values)

`real matrix`<span class="nowrap"> _
[<strong>solvenl_result_Jacobian(</strong><var class="command">S</var><strong>)</strong>](#result_Jacobian)

`real scalar`<span class="nowrap"> _
[<strong>solvenl_result_error_code(</strong><var class="command">S</var><strong>)</strong>](#result_error_code)

`real scalar`<span class="nowrap"> _
[<strong>solvenl_result_return_code(</strong><var class="command">S</var><strong>)</strong>](#result_return_code)

`string scalar`<span class="nowrap"> _
[<strong>solvenl_result_error_text(</strong><var class="command">S</var><strong>)</strong>](#result_error_text)

`void`<span class="nowrap"> _
[<strong>solvenl_dump(</strong><var class="command">S</var><strong>)</strong>](#dump)

`S`, if it is declared, should be declared as

`transmorphic S`

and `technique` optionally specified in `solvenl_init_technique()` is
one of the following:

`technique`<span style="padding-left: 15.5rem;">_Description

<span options="45">_

`gaussseidel`<span style="padding-left: 15.5rem;">_Gauss-Seidel

`dampedgaussseidel`<span style="padding-left: 15.5rem;">_Damped
Gauss-Seidel

`broydenpowell`<span
style="padding-left: 15.5rem;">_Broyden-Powell

\* `newtonraphson`<span
style="padding-left: 15.5rem;">_Newton-Raphson

<span options="45">_

\*`newton` may also be abbreviated as `nr`.

For fixed-point problems, allowed `technique`s are `gaussseidel` and
`dampedgaussseidel`. For zero-finding problems, allowed `technique`s are
`broydenpowell` and `newtonraphson`. `solvenl_*()` exits with an
error message if you specify a `technique` that is incompatible with the
type of evaluator you declared by using `solvenl_init_type()`. The
default technique for fixed-point problems is `dampedgaussseidel` with a
damping parameter of 0.1. The default technique for zero-finding
problems is `broydenpowell`.
