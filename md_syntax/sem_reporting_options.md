## Syntax

`sem`
[<var class="command">paths</var><strong></strong>](http://www.stata.com/help.cgi?sem_and_gsem%20path%20notation)
...`,` ... `reporting_options`

`sem, reporting_options`

| reporting\_options |                   | Description                                                                    |
|--------------------|-------------------|--------------------------------------------------------------------------------|
|                    | `level(#)`        | set confidence level; default is `level(95)`                                   |
|                    | `standardized`    | display standardized coefficients and values                                   |
|                    | `coeflegend`      | display coefficient legend                                                     |
|                    | `nocnsreport`     | do not display constraints                                                     |
|                    | `nodescribe`      | do not display variable classification table                                   |
|                    | `noheader`        | do not display header above parameter table                                    |
|                    | `nofootnote`      | do not display footnotes below parameter table                                 |
|                    | `notable`         | do not display parameter tables                                                |
|                    | `nofvlabel`       | display group values rather than value labels                                  |
|                    | `fvwrap(#)`       | allow `#` lines when wrapping long value labels                                |
|                    | `fvwrapon(style)` | apply `style` for wrapping long value labels; `style` may be `word` or `width` |
|                    | `byparm`          | display results in a single table with rows arranged by parameter              |
|                    | `showginvariant`  | report all estimated parameters                                                |
