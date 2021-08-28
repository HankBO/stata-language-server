## Syntax

Display memory usage report

`memory`

Display memory settings

`query memory`

Modify memory settings

`set maxvar`<span class="nowrap"> _`#` <span class="nowrap">
_\[`, permanently`\]

`set niceness`<span class="nowrap"> _`#` <span class="nowrap">
_\[`, permanently`\]

`set min_memory`<span class="nowrap"> _`amt` \[`, permanently`\]

`set max_memory`<span class="nowrap"> _`amt` \[`, permanently`\]

`set segmentsize amt` \[`, permanently`\]

where `amt` is `#`\[`b`\|`k`\|`m`\|`g`\], and the default unit is `b`.

<span options="TLC">{c TLC}_

------------------------------------------------------------------------

<span options="TT">{c TT}_

------------------------------------------------------------------------

<span options="TT">{c TT}_

------------------------------------------------------------------------

<span options="TRC">{c TRC}_|<span
options="|">{c \|}_|<span
options="|">{c \|}_<span options="LT">{c LT}_

------------------------------------------------------------------------

<span options="+">{c +}_

------------------------------------------------------------------------

<span options="+">{c +}_

------------------------------------------------------------------------

<span options="RT">{c RT}_|`maxvar`|`5000`<span
options="|">{c \|}_`2048120000`|||`5000`|`204832767`<span
options="|">{c \|}_|<span
options="|">{c \|}_`2048`|`20482048`|<span
options="|">{c \|}_{cmd None}|<span
options="|">{c \|}_|<span
options="|">{c \|}_`niceness`|`5`|`010`||{cmd None}||||`min_memory`<span
options="|">{c \|}_`00max_memory`||`max_memory`<span
options="|">{c \|}_`.`|`segmentsize`|<span
options="|">{c \|}_`segmentsize`|`32m`|`1m32g`<span
options="|">{c \|}_|{cmd None}<span
options="|">{c \|}_`16m`|`1m1g`|<span options="BLC">{c
BLC}_

------------------------------------------------------------------------

<span options="BT">{c BT}_

------------------------------------------------------------------------

<span options="BT">{c BT}_

------------------------------------------------------------------------

<span options="BRC">{c BRC}_

Notes:

1\. The maximum number of variables in your dataset is limited to
`maxvar`. The default value of `maxvar` is 5,000 for Stata/MP and
Stata/SE, and 2,048 for Stata/IC. With Stata/MP and Stata/SE, this
default value may be increased by using `set maxvar`. The default value
is fixed for Stata/IC.

2\. Most users do not need to read beyond this point. Stata's memory
management is completely automatic. If, however, you are using the Linux
operating system, see `Serious bug in Linux OS` under `Remarks` below.

3\. The maximum number of observations is fixed at 1,099,511,627,775 for
Stata/MP and is fixed at 2,147,483,647 for Stata/SE and Stata/IC
regardless of computer size or memory settings. Depending on the amount
of memory on your computer, you may face a lower practical limit. See
[<strong>help obs_advice</strong>](http://www.stata.com/help.cgi?obs_advice).

4\. `max_memory` specifies the maximum amount of memory Stata can use to
store your data. The default of missing (`.`) means all the memory the
operating system is willing to supply. There are three reasons to change
the value from missing to a finite number.

1\. You are a Linux user; see `Serious bug in Linux OS` under `Remarks`
below.

2\. You wish to reduce the chances of accidents, such as typing **expand
100000** with a large dataset in memory and actually having Stata do it.
You would rather see an insufficient-memory error message. Set
`max_memory` to the amount of physical memory on your computer or more
than that if you are willing to use virtual memory.

3\. You are a system administrator; see
`Notes for system administrators` under `Remarks` below.

5\. The remaining memory parameters -- `niceness`, `min_memory`, and
`segment_size` -- affect efficiency only; they do not affect the size of
datasets you can analyze.

6\. Memory amounts for `min_memory`, `max_memory`, and `segmentsize` may
be specified in bytes, kilobytes, megabytes, or gigabytes; suffix `b`,
`k`, `m`, or `g` to the end of the number. The following are equivalent
ways of specifying 1 gigabyte:

`10737418241048576k1024m1g`

Suffix `k` is defined as (multiply by) 1024, `m` is defined as 1024^2,
and `g` is defined as 1024^3.

7\. 64-bit computers can theoretically provide up to
18,446,744,073,709,551,616 bytes of memory, equivalent to 17,179,869,184
gigabytes, 16,777,216 terabytes, 16,384 petabytes, or 16 exabytes. Real
computers have less.

8\. 32-bit computers can theoretically provide up to 4,294,967,296 bytes
of memory, equivalent to 4,194,304 kilobytes, 4,096 megabytes, or 4
gigabytes. Most 32-bit operating systems limit Stata to half that.

9\. Stata allocates memory for data in units of `segmentsize`. Smaller
values of `segmentsize` can result in more efficient use of available
memory but require Stata to jump around more. The default provides a
good balance. We recommend resetting `segmentsize` only if your computer
has large amounts of memory.

10\. If you have large amounts of memory and you use it to process large
datasets, you may wish to increase `segmentsize`. Suggested values are

`segmentsize`

------------------------------------------------------------------------

------------------------------------------------------------------------

11\. `niceness` affects how soon Stata gives back unused segments to the
operating system. If Stata releases them too soon, it often needs to
turn around and get them right back. If Stata waits too long, Stata is
consuming memory that it is not using. One reason to give memory back is
to be nice to other users on multiuser systems or to be nice to yourself
if you are running other processes.

The default value of 5 is defined to provide good performance. Waiting
times are currently defined as

------------------------------------------------------------------------

------------------------------------------------------------------------

Niceness 10 corresponds to being totally nice. Niceness 0 corresponds to
being an inconsiderate, self-centered, totally selfish jerk.

12\. `min_memory` specifies an amount of memory Stata will not fall
below. For instance, you have a long do-file. You know that late in the
do-file, you will need 8 gigabytes. You want to ensure that the memory
will be available later. At the start of your do-file, you `set`
`min_memory 8g`.

13\. Concerning `min_memory` and `max_memory`, be aware that Stata
allocates memory in `segmentsize` blocks. Both `min_memory` and
`max_memory` are rounded down. Thus the actual minimum memory Stata will
reserve will be `segmentsize*trunc(min_memory/segmentsize)`. The
effective maximum memory is calculated similarly. (Stata does not round
up `min_memory` because some users set `min_memory` equal to
`max_memory`.)
