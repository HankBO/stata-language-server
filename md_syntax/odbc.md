## Syntax

List ODBC sources to which Stata can connect

`odbc list`

Retrieve available names from specified data source

`odbc query` \[`"DataSourceName" , verbose schema`
`connect_options`\]

List column names and types associated with specified table

`odbc describe` \[`"TableName" , connect_options`\]

Import data from an ODBC data source

`odbc load` \[`extvarlist`\] _\[`if`\]
\[`in`\]_ `,` <span options="-(">{c
-(}_`table:("TableName")`|`exec:("SqlStmt")`}  
\[`load_options connect_options`\]

Export data to an ODBC data source

`odbc insert`
\[[varlist](http://www.stata.com/help.cgi?varlist)\]
_\[`if`\] \[`in`\]_ `,`
`table:("TableName")`  
{`dsn("DataSourceName")`<span
options="|">{c \|}_`connectionstring:("ConnectStr")`<span
options=")-">{c )-}_  
\[`insert_options connect_options`\]

Allow SQL statements to be issued directly to ODBC data source

`odbc exec("SqlStmt") ,` <span options="-(">{c
-(}_`dsn("DataSourceName")`|`connectionstring:("ConnectStr")`<span options=")-">{c
)-}_  
\[`connect_options`\]

Batch job alternative to odbc exec

`odbc sqlfile:("filename") ,` <span options="-(">{c
-(}_`dsn("DataSourceName")`|`connectionstring:("ConnectStr")`<span options=")-">{c
)-}_  
\[`loud connect_options`\]

Specify ODBC driver type

`set odbcdriver` {`unicode`<span
options="|">{c \|}_`ansi`} \[`,`
`permanently`\]

Specify ODBC driver manager (Mac and Unix only)

`set odbcmgr` {`iodbc`<span
options="|">{c \|}_`unixodbc`}
\[`, permanently`\]

`DataSourceName` is the name of the ODBC source (database, spreadsheet,
etc.)

`ConnectStr` is a valid ODBC connection string

`TableName` is the name of a table within the ODBC data source

`SqlStmt` is an SQL SELECT statement

`filename` is pure SQL commands separated by semicolons

`extvarlist` contains

`sqlvarname`

[varname](http://www.stata.com/help.cgi?varname)=`sqlvarname`

| connect\_options                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                      | Description                                                                                           |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------|-------------------------------------------------------------------------------------------------------|
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | `user(UserID)`                       | user ID of user establishing connection                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | `password(Password)`                 | password of user establishing connection                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | `dialog(noprompt)`                   | do not display ODBC connection-information dialog, and do not prompt user for connection information  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | `dialog(prompt)`                     | display ODBC connection-information dialog                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | `dialog(complete)`                   | display ODBC connection-information dialog only if there is not enough information                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | `dialog(required)`                   | display ODBC connection-information dialog only if there is not enough mandatory information provided |
| \*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | `dsn("DataSourceName")`          | name of data source                                                                                   |
| \*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | `connectionstring("ConnectStr")` | ODBC connection string                                                                                |
| \*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | `exec("SqlStmt")`                | SQL SELECT statement to generate a table to be read into Stata                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | `clear`                              | load dataset even if there is one in memory                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | `noquote`                            | alter Stata's internal use of SQL commands; seldom used                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | `lowercase`                          | read variable names as lowercase                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | `sqlshow`                            | show all SQL commands issued                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | `allstring`                          | read all variables as strings                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | `datestring`                         | read date-formatted variables as strings                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | `multistatement`                     | allow multiple SQL statements delimited by `;` when using `exec()`                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | `bigintasdouble`                     | store BIGINT columns as Stata doubles on 64-bit operating systems                                     |
| \* `dsn("DataSourceName")` is not allowed with `odbc query`. You may not specify both `DataSourceName` and `connectionstring()` with `odbc query`. Either `dsn()` or `connectionstring()` is required with `odbc insert`, `odbc exec`, and `odbc sqlfile`. <span options="25 tabbed">{synoptset 25 tabbed}_{nobreak None} <span options="load_options">{marker load\_options}_{nobreak None} {synopthdr None:load\_options} {synoptline None} {p2coldent None:\* }`table("TableName")`name of table stored in data source |                                      |                                                                                                       |
| \* Either `table("TableName")` or `exec("SqlStmt")` must be specified with `odbc load`.                                                                                                                                                                                                                                                                                                                                                                                                                                             |                                      |                                                                                                       |

| insert\_options                                               |                                                                                       | Description                                                                          |
|---------------------------------------------------------------|---------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| \*                                                            | `table("TableName")`                                                              | name of table stored in data source                                                  |
|                                                               | `overwrite`                                                                           | clear data in ODBC table before data in memory is written to the table               |
|                                                               | `insert`                                                                              | default mode of operation for the `odbc insert` command                              |
|                                                               | `quoted`                                                                              | quote all values with single quotes as they are inserted in ODBC table               |
|                                                               | `sqlshow`                                                                             | show all SQL commands issued                                                         |
|                                                               | `as("`[varlist](http://www.stata.com/help.cgi?varlist)`")` | ODBC variables on the data source that correspond to the variables in Stata's memory |
|                                                               | `block`                                                                               | use block inserts                                                                    |
| \* `table("TableName")` is required with `odbc insert`. |                                                                                       |                                                                                      |
