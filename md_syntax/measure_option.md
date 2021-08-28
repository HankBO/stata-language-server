## Syntax

`command,measure(measure)command,measure`

|                                                                                |                                                                             |
|--------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| `measure`                                                                      | Description {p2line None}                                                   |
| `cont_measure`                                                                 | similarity or dissimilarity measure for continuous data                     |
| `binary_measure`                                                               | similarity measure for binary data                                          |
| `mixed_measure`                                                                | dissimilarity measure for a mix of binary and continuous data {p2line None} |
| <span options="cont_measure">{marker cont\_measure}_`cont_measure`       | Description {p2line None}                                                   |
| `L2`                                                                           | Euclidean distance (Minkowski with argument 2)                              |
| `Euclidean`                                                                    | alias for `L2`                                                              |
| `L(2)`                                                                         | alias for `L2`                                                              |
| `L2squared`                                                                    | squared Euclidean distance                                                  |
| `Lpower(2)`                                                                    | alias for `L2squared`                                                       |
| `L1`                                                                           | absolute-value distance (Minkowski with argument 1)                         |
| `absolute`                                                                     | alias for `L1`                                                              |
| `cityblock`                                                                    | alias for `L1`                                                              |
| `manhattan`                                                                    | alias for `L1`                                                              |
| `L(1)`                                                                         | alias for `L1`                                                              |
| `Lpower(1)`                                                                    | alias for `L1`                                                              |
| `Linfinity`                                                                    | maximum-value distance (Minkowski with infinite argument)                   |
| `maximum`                                                                      | alias for `Linfinity`                                                       |
| `L(#)`                                                                         | Minkowski distance with `#` argument                                        |
| `Lpower(#)`                                                                    | Minkowski distance with `#` argument raised to `#` power                    |
| `Canberra`                                                                     | Canberra distance                                                           |
| `correlation`                                                                  | correlation coefficient similarity measure                                  |
| `angular`                                                                      | angular separation similarity measure                                       |
| `angle`                                                                        | alias for `angular` {p2line None}                                           |
| <span options="binary_measure">{marker binary\_measure}_`binary_measure` | Description {p2line None}                                                   |
| `matching`                                                                     | simple matching similarity coefficient                                      |
| `Jaccard`                                                                      | Jaccard binary similarity coefficient                                       |
| `Russell`                                                                      | Russell and Rao similarity coefficient                                      |
| `Hamann`                                                                       | Hamann similarity coefficient                                               |
| `Dice`                                                                         | Dice similarity coefficient                                                 |
| `antiDice`                                                                     | anti-Dice similarity coefficient                                            |
| `Sneath`                                                                       | Sneath and Sokal similarity coefficient                                     |
| `Rogers`                                                                       | Rogers and Tanimoto similarity coefficient                                  |
| `Ochiai`                                                                       | Ochiai similarity coefficient                                               |
| `Yule`                                                                         | Yule similarity coefficient                                                 |
| `Anderberg`                                                                    | Anderberg similarity coefficient                                            |
| `Kulczynski`                                                                   | Kulczyński similarity coefficient                                           |
| `Pearson`                                                                      | Pearson's phi similarity coefficient                                        |
| `Gower2`                                                                       | similarity coefficient with same denominator as `Pearson` {p2line None}     |
| <span options="mixed_measure">{marker mixed\_measure}_`mixed_measure`    | Description {p2line None}                                                   |
| `Gower`                                                                        | Gower's dissimilarity coefficient {p2line None}                             |
