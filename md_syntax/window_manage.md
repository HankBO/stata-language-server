## Syntax

Minimize or restore the main Stata window

`window manage minimize`

`window manage restore`

Manage window preferences

`window manage prefs` {`load`
"`prefname`"\|`save` "`prefname`"\|`default`<span options=")-">{c
)-}_

Restore file associations (Windows only)

`window manage associate`

Reset main window title (Unix and Windows only)

`window manage maintitle` {`reset` \|
"`title`"}

Set Dock icon's label (Mac only)

`window manage docklabel` \["`label`"\]

Bring windows forward

`window manage forward window-name`

where `window-name` can be `command`, `doeditor`, `graph`, `help`,
`results`, `review`, `variables`, or `viewer`.

Commands to manage Graph windows

`window manage print graph`

`window manage forward graph` \["`graphname`"\]

`window manage close graph` \[<span options="-(">{c
-(}_"`graphname`"\|`_all`}\]

`window manage rename graph oldgraphname newgraphname`

Commands to manage Viewer windows

`window manage print viewer` \["`viewername`"\]

`window manage forward viewer` \["`viewername`"\]

`window manage close viewer` \[<span options="-(">{c
-(}_"`viewername`"\|`_all`}\]
