## Syntax

`search word` \[`word ...`\] \[`, search_options`\]

`set searchdefault` <span options="-(">{c
-(}_`all`\|`local`\|`net`} \[`,`
`permanently`\]

| search\_options |              | Description                                                                                               |
|-----------------|--------------|-----------------------------------------------------------------------------------------------------------|
|                 | `all`        | search across both the local keyword database and the `net` material; the default                         |
|                 | `local`      | search using Stata's keyword database                                                                     |
|                 | `net`        | search across materials available via Stata's `net` command                                               |
|                 | `author`     | search by author's name                                                                                   |
|                 | `entry`      | search by entry ID                                                                                        |
|                 | `exact`      | search across both the local keyword database and the `net` materials; prevents matching on abbreviations |
|                 | `faq`        | search the FAQs posted to the Stata website                                                               |
|                 | `historical` | search entries that are of historical interest only                                                       |
|                 | `or`         | list an entry if any of the words typed after `search` are associated with the entry                      |
|                 | `manual`     | search the entries in the Stata Documentation                                                             |
|                 | `sj`         | search the entries in the Stata Journal and the STB                                                       |
