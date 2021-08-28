## Syntax

Report status of log file

`log`

`log query` \[`logname` \| `_all`\]

Open log file

`log using filename` \[`, append replace` \[`text`<span
options="|">{c \|}_`smcl`\] `name(logname) nomsg`\]

Close log

`log close` \[`logname` \| `_all`\]

Temporarily suspend logging or resume logging

`log` {`off`|`on`} \[`logname`\]

Report status of command log file

`cmdlog`

Open command log file

`cmdlog using filename` \[`, append replace`\]

Close command log, temporarily suspend logging, or resume logging

`cmdlog` {`close`|`on`|`off`<span options=")-">{c
)-}_

Set default format for logs

`set logtype` {`text`|`smcl`} \[`, permanently`\]

Specify screen width

`linesize #`

In addition to using the `log` command, you may access the capabilities
of `log` by selecting **File &gt; Log** from the menu and choosing one
of the options in the list.
