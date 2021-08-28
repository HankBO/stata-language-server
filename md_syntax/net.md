## Syntax

Set current location for net

`net from directory_or_url`

Change to a different net directory

`net cd path_or_url`

Change to a different net site

`net link linkname`

Search for installed packages

`net search word` \[`word ...`\] \[`, search_options`\]

Report current net location

`net`

Describe a package

`net describe pkgname` \[`, from(directory_or_url)`\]

Set location where packages will be installed

`net set ado dirname`

Set location where ancillary files will be installed

`net set other dirname`

Report net 'from', 'ado', and 'other' settings

`net query`

Install ado-files and help files from a package

`net install pkgname` \[`, all replace force`
`from(directory_or_url)`\]

Install ancillary files from a package

`net get pkgname` \[`, all replace force from(directory_or_url)`\]

Shortcut to access Stata Journal (SJ) net site

`net sj vol-issue` \[`insert`\]

Shortcut to access Stata Technical Bulletin (STB) net site

`net stb issue` \[`insert`\]

List installed packages

`ado` \[`, find(string) from(dirname)`\]

`ado dir` \[`pkgid`\] \[`, find(string) from(dirname)`\]

Describe installed packages

`ado describe` \[`pkgid`\] \[`, find(string) from(dirname)`\]

Uninstall an installed package

`ado uninstall pkgid` \[`, from(dirname)`\]

| search\_options |              | Description                                                    |
|-----------------|--------------|----------------------------------------------------------------|
|                 | `or`         | list packages that contain any of the keywords; default is all |
|                 | `nosj`       | search non-SJ and non-STB sources                              |
|                 | `tocpkg`     | search both tables of contents and packages; the default       |
|                 | `toc`        | search table of contents only                                  |
|                 | `pkg`        | search packages only                                           |
|                 | `everywhere` | search packages for match                                      |
|                 | `filenames`  | search filenames associated with package for match             |
|                 | `errnone`    | make return code 111 instead of 0 when no matches found        |

`pkgname`

`pkgid` <span options="1">{space 1}_ is <span options="1">{space
1}_ name of a package

or <span options="1">{space 1}_ a number in square brackets:
`[#]`

`dirname` is <span options="1">{space 1}_ a directory name

or <span options="1">{space 1}_ `PLUS` <span options="4">{space
4}_ (default)

or <span options="1">{space 1}_ `PERSONAL`

or <span options="1">{space 1}_ `SITE`
