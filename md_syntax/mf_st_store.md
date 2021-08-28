## Syntax

`void_st_store(real scalar i,real scalar j,real scalar x)voidst_store(real matrix i,rowvector j,real matrix X)`{right
None:(1,2)}`voidst_store(real matrix i,rowvector j,scalar selectvar,`

`real matrix X)`{right None:(1,2,3)}

`void_st_sstore(real scalar i,real scalar j,string scalar s)voidst_sstore(real matrix i,rowvector j,string matrix X)`{right
None:(1,2)}`voidst_sstore(real matrix i,rowvector j,scalar selectvar,`

`string matrix X)`{right None:(1,2,3)}

where

1\. `i` may be specified in the same way as with
**[<strong>st_data()</strong>](http://www.stata.com/help.cgi?mf_st_data)**.

2\. `j` may be specified in the same way as with
**[<strong>st_data()</strong>](http://www.stata.com/help.cgi?mf_st_data)**,
except that time-series operators may not be specified.

3\. `selectvar` may be specified in the same way as with
**[<strong>st_data()</strong>](http://www.stata.com/help.cgi?mf_st_data)**.
