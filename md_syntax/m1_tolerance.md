## Syntax

`somefunction(`...`, real scalar tol,` ...`)`

where, concerning argument `tol`,

optional<span class="nowrap"> _Argument `tol` is usually optional;
not specifying `tol` is equivalent to specifying `tol`=1.

`tol`&gt;0<span class="nowrap"> _Specifying `tol`&gt;0 specifies
the amount by which the usual tolerance is to be multiplied: `tol`=2
means twice the usual tolerance; `tol`=.5 means half the usual
tolerance.

`tol`&lt;0<span class="nowrap"> _Specifying `tol`&lt;0 specifies
the negative of the value to be used for the tolerance: `tol` = -1e-14
means 1e-14 is to be used.

`tol`=0<span class="nowrap"> _Specifying `tol`=0 means all numbers
are to be taken at face value, no matter how close to 0 they are. The
single exception is when `tol` is applied to values that,
mathematically, must be greater than or equal to zero. Then negative
values (which arise from roundoff error) are treated as if they were
zero.

The default tolerance is given by formula, such as

`eta1e-14`

or

`etaepsilon(1)`{right None:(see
}**[<strong>[M-5] epsilon()</strong>](http://www.stata.com/help.cgi?mf_epsilon)**)

or

`eta1000*epsilon(trace(abs(A))/rows(A))`

Specifying `tol`&gt;0 specifies a value to be used to multiply `eta`.
Specifying `tol`&lt;0 specifies that -`tol` be used in place of `eta`.
Specifying `tol`=0 specifies that `eta` be set to 0.

The formula for `eta` and how `eta` is used are found under `Remarks`.
For instance, the `Remarks` might say that `A` is declared to be
singular if any diagonal element of `U` of its LU decomposition is less
than or equal to `eta`.
