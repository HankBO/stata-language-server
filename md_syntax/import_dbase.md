## Syntax

Load a dBase file

`import dbase` \[`using`\] `filename` \[`, clear`
`case(preserve`\|`lower`\|`upper)`\]

Save data in memory to a dBase file

`export dbase` \[`using`\] `filename` _\[`if`\]
\[`in`\]_ \[`, datafmt replace`\]

Save subset of variables in memory to a dBase file

`export dbase`
\[[varlist](http://www.stata.com/help.cgi?varlist)\]
`using filename` _\[`if`\] \[`in`\]_ \[`,`
`datafmt replace`\]

If `filename` is specified without an extension, `.dbf` is assumed for
both `import dbase` and `export dbase`. If `filename` contains embedded
spaces, enclose it in double quotes.
