## Syntax

`print filename` \[`, like(ext) name(windowname)`
`override_options` \]

`filename`, in addition to being the filename to be printed, may be
specified as `@Result` to mean print the Results window, `@Viewer` to
mean print the topmost Viewer window, and `@Graph` to mean print the
topmost Graph window. Unix(GUI) users should use the `name` option when
specifying `@Viewer` or `@Graph` to ensure the correct window is printed
when there is more than one viewer or graph open (see the
[<strong>Technical note for Unix(GUI) users</strong>](#GUI)).
