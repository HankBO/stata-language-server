## Syntax

`checksum filename` \[`, options`\]

`set checksum` {`on`\|`off`<span
options=")-">{c )-}_ \[`, permanently`\]

| Options |                                          | Description                                                     |
|---------|------------------------------------------|-----------------------------------------------------------------|
|         | `save`                                   | save output to `filename.sum`; default is to display a report |
|         | `replace`                                | may overwrite `filename.sum`; use with `save`                 |
|         | `saving(filename2`\[`, replace`\]`)` | save output to `filename2`; alternative to `save`               |
