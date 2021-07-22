## Syntax

`egen` _\[`type`\] \[_
[newvar](http://www.stata.com/help.cgi?newvar)
`= fcn(arguments)` _\[`if`\]
\[`in`\]_ \[`, options`\]

`by` is allowed with some of the `egen` functions, as noted below.

where depending on the `fcn`, `arguments` refers to an expression,
`varlist`, or `numlist`, and the `options` are also `fcn` dependent, and
where `fcn` is

`anycount(varlist), values(integer numlist)`

may not be combined with `by`. It returns the number of variables in
`varlist` for which values are equal to any integer value in a supplied
`numlist`. Values for any observations excluded by either
[<strong>if</strong>](http://www.stata.com/help.cgi?if)
or
[<strong>in</strong>](http://www.stata.com/help.cgi?in)
are set to 0 (not missing). Also see `anyvalue(varname)` and
`anymatch(varlist)`.

`anymatch(varlist), values(integer numlist)`

may not be combined with `by`. It is 1 if any variable in `varlist` is
equal to any integer value in a supplied `numlist` and 0 otherwise.
Values for any observations excluded by either
[<strong>if</strong>](http://www.stata.com/help.cgi?if)
or
[<strong>in</strong>](http://www.stata.com/help.cgi?in)
are set to 0 (not missing). Also see `anyvalue(varname)` and
`anycount(varlist)`.

`anyvalue(varname), values(integer numlist)`

may not be combined with `by`. It takes the value of `varname` if
`varname` is equal to any integer value in a supplied `numlist` and is
missing otherwise. Also see `anymatch(varlist)` and `anycount(varlist)`.

`concat(varlist)` \[`, format(%fmt) decode maxlength(#)`
`punct(pchars)`\]

may not be combined with `by`. It concatenates `varlist` to produce a
string variable. Values of string variables are unchanged. Values of
numeric variables are converted to string, as is, or are converted using
a numeric format under the `format(%fmt)` option or decoded under
the `decode` option, in which case `maxlength()` may also be used to
control the maximum label length used. By default, variables are added
end to end: `punct(pchars)` may be used to specify punctuation, such as
a space, `punct(" ")`, or a comma, `punct(,)`.

`count(exp)`{right None:(allows
}[<strong>by</strong> <var class="command">varlist</var><strong>:</strong>](http://www.stata.com/help.cgi?by))

creates a constant (within `varlist`) containing the number of
nonmissing observations of `exp`. Also see
[<strong>rownonmiss()</strong>](#rownonmiss())
and [<strong>rowmiss()</strong>](#rowmiss()).

`cut(varname),` <span options="-(">{c
-(}_`at(#,#,...,#)`\|`group(#)`<span
options=")-">{c )-}_ \[`icodes label`\]

may not be combined with `by`. It creates a new categorical variable
coded with the left-hand ends of the grouping intervals specified in the
`at()` option, which expects an ascending numlist.

`at(#,#,...,#)` supplies the breaks for the groups, in
ascending order. The list of breakpoints may be simply a list of numbers
separated by commas but can also include the syntax `a(b)c`, meaning
from `a` to `c` in steps of size `b`.
[newvar](http://www.stata.com/help.cgi?newvar)
is set to missing for observations with `varname` less than the first
number specified in `at()` and for observations with `varname` greater
than or equal to the last number specified in `at()`. If no breaks are
specified, the command expects the `group()` option.

`group(#)` specifies the number of equal frequency grouping intervals to
be used in the absence of breaks. Specifying this option automatically
invokes `icodes`.

`icodes` requests that the codes 0, 1, 2, etc., be used in place of the
left-hand ends of the intervals.

`label` requests that the integer-coded values of the grouped variable
be labeled with the left-hand ends of the grouping intervals. Specifying
this option automatically invokes `icodes`.

`diff(varlist)`

may not be combined with `by`. It creates an indicator variable equal to
1 if the variables in `varlist` are not equal and 0 otherwise.

`ends(strvar)` \[`, punct:(pchars) trim`
\[`head`\|`last`\|`tail`\]\]

may not be combined with `by`. It gives the first "word" or head (with
the `head` option), the last "word" (with the `last` option), or the
remainder or tail (with the `tail` option) from string variable
`strvar`.

`head`, `last`, and `tail` are determined by the occurrence of `pchars`,
which is by default one space (" ").

The head is whatever precedes the first occurrence of `pchars`, or the
whole of the string if it does not occur. For example, the head of "frog
toad" is "frog" and that of "frog" is "frog". With `punct(,)`, the head
of "frog,toad" is "frog".

The last word is whatever follows the last occurrence of `pchars` or is
the whole of the string if a space does not occur. The last word of
"frog toad newt" is "newt" and that of "frog" is "frog". With
`punct(,)`, the last word of "frog,toad" is "toad".

The remainder or tail is whatever follows the first occurrence of
`pchars`, which will be the empty string "" if `pchars` does not occur.
The tail of "frog toad newt" is "toad newt" and that of "frog" is "".
With `punct(,)`, the tail of "frog,toad" is "toad".

The `trim` option trims any leading or trailing spaces.

`fill(numlist)`

may not be combined with `by`. It creates a variable of ascending or
descending numbers or complex repeating patterns. `numlist` must contain
at least two numbers and may be specified using standard `numlist`
notation; see
[<strong>numlist</strong>](http://www.stata.com/help.cgi?numlist).
[<strong>if</strong>](http://www.stata.com/help.cgi?if)
and
[<strong>in</strong>](http://www.stata.com/help.cgi?in)
are not allowed with `fill()`.

`group(varlist)` \[`, missing label lname(name)`
`truncate(num)`\]

may not be combined with `by`. It creates one variable taking on values
1, 2, ... for the groups formed by `varlist`. `varlist` may contain
numeric variables, string variables, or a combination of the two. The
order of the groups is that of the sort order of `varlist`. `missing`
indicates that missing values in `varlist` <span class="nowrap">(either
`.` or `""`_) are to be treated like any other value when
assigning groups, instead of as missing values being assigned to the
group missing. The `label` option returns integers from 1 up according
to the distinct groups of `varlist` in sorted order. The integers are
labeled with the values of `varlist` or the value labels, if they exist.
`lname()` specifies the name to be given to the value label created to
hold the labels; `lname()` implies `label`. The `truncate()` option
truncates the values contributed to the label from each variable in
`varlist` to the length specified by the integer argument `num`. The
`truncate` option cannot be used without specifying the `label` option.
The `truncate` option does not change the groups that are formed; it
changes only their labels.

`iqr(exp)`{right None:(allows
}[<strong>by</strong> <var class="command">varlist</var><strong>:</strong>](http://www.stata.com/help.cgi?by))

creates a constant (within `varlist`) containing the interquartile range
of `exp`. Also see
[<strong>pctile()</strong>](#pctile()).

`kurt(varname)`{right None:(allows
}[<strong>by</strong> <var class="command">varlist</var><strong>:</strong>](http://www.stata.com/help.cgi?by))

returns the kurtosis (within `varlist`) of `varname`.

`mad(exp)`{right None:(allows
}[<strong>by</strong> <var class="command">varlist</var><strong>:</strong>](http://www.stata.com/help.cgi?by))

returns the median absolute deviation from the median (within `varlist`)
of `exp`.

`max(exp)`{right None:(allows
}[<strong>by</strong> <var class="command">varlist</var><strong>:</strong>](http://www.stata.com/help.cgi?by))

creates a constant (within `varlist`) containing the maximum value of
`exp`.

`mdev(exp)`{right None:(allows
}[<strong>by</strong> <var class="command">varlist</var><strong>:</strong>](http://www.stata.com/help.cgi?by))

returns the mean absolute deviation from the mean (within `varlist`) of
`exp`.

`mean(exp)`{right None:(allows
}[<strong>by</strong> <var class="command">varlist</var><strong>:</strong>](http://www.stata.com/help.cgi?by))

creates a constant (within `varlist`) containing the mean of `exp`.

`median(exp)`{right None:(allows
}[<strong>by</strong> <var class="command">varlist</var><strong>:</strong>](http://www.stata.com/help.cgi?by))

creates a constant (within `varlist`) containing the median of `exp`.
Also see
[<strong>pctile()</strong>](#pctile()).

`min(exp)`{right None:(allows
}[<strong>by</strong> <var class="command">varlist</var><strong>:</strong>](http://www.stata.com/help.cgi?by))

creates a constant (within `varlist`) containing the minimum value of
`exp`.

`mode(varname),minmodemaxmodenummode(integer)missing`{right
None:(allows
}[<strong>by</strong> <var class="command">varlist</var><strong>:</strong>](http://www.stata.com/help.cgi?by))

produces the mode (within `varlist`) for `varname`, which may be numeric
or string. The mode is the value occurring most frequently. If two or
more modes exist or if `varname` contains all missing values, the mode
produced will be a missing value. To avoid this, the `minmode`,
`maxmode`, or `nummode()` option may be used to specify choices for
selecting among the multiple modes, and the `missing` option will treat
missing values as categories. `minmode` returns the lowest value, and
`maxmode` returns the highest value. `nummode(#)` will return the `#`th
mode, counting from the lowest up. Missing values are excluded from
determination of the mode unless `missing` is specified. Even so, the
value of the mode is recorded for observations for which the values of
`varname` are missing unless they are explicitly excluded, that is, by
<span class="nowrap">`if varname < .` or `if varname`
`!= ""`_.

`mtr(year income)`

may not be combined with `by`. It returns the U.S. marginal income tax
rate for a married couple with taxable income `income` in year `year`,
where 1930

`year`

2017\. `year` and `income` may be specified as variable names or
constants; for example, <span class="nowrap">`mtr(1993 faminc)`_,
`mtr(surveyyr 28000)`, or `mtr(surveyyr faminc)`. A blank or comma may
be used to separate `income` from `year`.

`pc(exp), prop`{right None:(allows
}[<strong>by</strong> <var class="command">varlist</var><strong>:</strong>](http://www.stata.com/help.cgi?by))

returns `exp` (within `varlist`) scaled to be a percentage of the total,
between 0 and 100. The `prop` option returns `exp` scaled to be a
proportion of the total, between 0 and 1.

`pctile(exp), p(#)`{right None:(allows
}[<strong>by</strong> <var class="command">varlist</var><strong>:</strong>](http://www.stata.com/help.cgi?by))

creates a constant (within `varlist`) containing the `#`th percentile of
`exp`. If `p(#)` is not specified, 50 is assumed, meaning medians. Also
see [<strong>median()</strong>](#median()).

`rank(exp),fieldtrackunique`{right None:(allows
}[<strong>by</strong> <var class="command">varlist</var><strong>:</strong>](http://www.stata.com/help.cgi?by))

creates ranks (within `varlist`) of `exp`; by default, equal
observations are assigned the average rank. The `field` option
calculates the field rank of `exp`: the highest value is ranked 1, and
there is no correction for ties. That is, the field rank is 1 + the
number of values that are higher. The `track` option calculates the
track rank of `exp`: the lowest value is ranked 1, and there is no
correction for ties. That is, the track rank is 1 + the number of values
that are lower. The `unique` option calculates the unique rank of `exp`:
values are ranked 1,...,`#`, and values and ties are broken arbitrarily.
Two values that are tied for second are ranked 2 and 3.

`rowfirst(varlist)`

may not be combined with `by`. It gives the first nonmissing value in
`varlist` for each observation (row). If all values in `varlist` are
missing for an observation,
[newvar](http://www.stata.com/help.cgi?newvar)
is set to missing.

`rowlast(varlist)`

may not be combined with `by`. It gives the last nonmissing value in
`varlist` for each observation (row). If all values in `varlist` are
missing for an observation,
[newvar](http://www.stata.com/help.cgi?newvar)
is set to missing.

`rowmax(varlist)`

may not be combined with `by`. It gives the maximum value (ignoring
missing values) in `varlist` for each observation (row). If all values
in `varlist` are missing for an observation,
[newvar](http://www.stata.com/help.cgi?newvar)
is set to missing.

`rowmean(varlist)`

may not be combined with `by`. It creates the (row) means of the
variables in `varlist`, ignoring missing values; for example, if three
variables are specified and, in some observations, one of the variables
is missing, in those observations
[newvar](http://www.stata.com/help.cgi?newvar)
will contain the mean of the two variables that do exist. Other
observations will contain the mean of all three variables. Where none of
the variables exist, `newvar` is set to missing.

`rowmedian(varlist)`

may not be combined with `by`. It gives the (row) median of the
variables in `varlist`, ignoring missing values. If all variables in
`varlist` are missing for an observation,
[newvar](http://www.stata.com/help.cgi?newvar)
is set to missing in that observation. Also see
[<strong>rowpctile()</strong>](#rowpctile()).

`rowmin(varlist)`

may not be combined with `by`. It gives the minimum value in `varlist`
for each observation (row). If all values in `varlist` are missing for
an observation,
[newvar](http://www.stata.com/help.cgi?newvar)
is set to missing.

`rowmiss(varlist)`

may not be combined with `by`. It gives the number of missing values in
`varlist` for each observation (row).

`rownonmiss(varlist)` \[`, strok`\]

may not be combined with `by`. It gives the number of nonmissing values
in `varlist` for each observation (row) -- this is the value used by
`rowmean()` for the denominator in the mean calculation.

String variables may not be specified unless the `strok` option is also
specified. If `strok` is specified, string variables will be counted as
containing missing values when they contain "". Numeric variables will
be counted as containing missing when their value is "

`.`".

`rowpctile(varlist)` \[`, p(#)`\]

may not be combined with `by`. It gives the `#`th percentile of the
variables in `varlist`, ignoring missing values. If all variables in
`varlist` are missing for an observation, `newvar` is set to missing in
that observation. If `p()` is not specified, `p(50)` is assumed, meaning
medians. Also see
[<strong>rowmedian()</strong>](#rowmedian()).

`rowsd(varlist)`

may not be combined with `by`. It creates the (row) standard deviations
of the variables in `varlist`, ignoring missing values.

`rowtotal(varlist)` \[`, missing`\]

may not be combined with `by`. It creates the (row) sum of the variables
in `varlist`, treating missing as 0. If `missing` is specified and all
values in `varlist` are missing for an observation, `newvar` is set to
missing.

`sd(exp)`{right None:(allows
}[<strong>by</strong> <var class="command">varlist</var><strong>:</strong>](http://www.stata.com/help.cgi?by))

creates a constant (within `varlist`) containing the standard deviation
of `exp`. Also see
[<strong>mean()</strong>](#mean()).

`seq(),from(#)to(#)block(#)`{right None:(allows
}[<strong>by</strong> <var class="command">varlist</var><strong>:</strong>](http://www.stata.com/help.cgi?by))

returns integer sequences. Values start from `from()` (default 1) and
increase to `to()` (the default is the maximum number of values) in
blocks (default size 1). If `to()` is less than the maximum number,
sequences restart at `from()`. Numbering may also be separate within
groups defined by `varlist` or decreasing if `to()` is less than
`from()`. Sequences depend on the sort order of observations, following
three rules: 1) observations excluded by
[<strong>if</strong>](http://www.stata.com/help.cgi?if)
or
[<strong>in</strong>](http://www.stata.com/help.cgi?in)
are not counted; 2) observations are sorted by `varlist`, if specified;
and 3) otherwise, the order is that when called. No `arguments` are
specified.

`skew(varname)`{right None:(allows
}[<strong>by</strong> <var class="command">varlist</var><strong>:</strong>](http://www.stata.com/help.cgi?by))

returns the skewness (within `varlist`) of `varname`.

`std(exp)` \[`, mean(#) std(#)`\]

may not be combined with `by`. It creates the standardized values of
`exp`. The options specify the desired mean and standard deviation. The
default is `mean(0)` and `std(1)`, producing a variable with mean 0 and
standard deviation 1.

`tag(varlist)` \[`, missing`\]

may not be combined with `by`. It tags just one observation in each
distinct group defined by `varlist`. When all observations in a group
have the same value for a summary variable calculated for the group, it
will be sufficient to use just one value for many purposes. The result
will be 1 if the observation is tagged and never missing, and 0
otherwise. Values for any observations excluded by either
[<strong>if</strong>](http://www.stata.com/help.cgi?if)
or
[<strong>in</strong>](http://www.stata.com/help.cgi?in)
are set to 0 (not missing). Hence, if `tag` is the variable produced by
`egen tag = tag(varlist)`, the idiom `if tag` is always safe.
`missing` specifies that missing values of `varlist` may be included.

`total(exp),missing`{right None:(allows
}[<strong>by</strong> <var class="command">varlist</var><strong>:</strong>](http://www.stata.com/help.cgi?by))

creates a constant (within `varlist`) containing the sum of `exp`
treating missing as 0. If `missing` is specified and all values in `exp`
are missing, `newvar` is set to missing. Also see
[<strong>mean()</strong>](#mean()).
