## Syntax

Distributional diagnostic plots:

|                                                                                                          |                                                    |
|----------------------------------------------------------------------------------------------------------|----------------------------------------------------|
| Command                                                                                                  | Description {p2line None}                          |
| [<strong>histogram</strong>](http://www.stata.com/help.cgi?histogram)         | histograms                                         |
| [<strong>symplot</strong>](http://www.stata.com/help.cgi?diagnostic%20plots)  | symmetry plots                                     |
| [<strong>quantile</strong>](http://www.stata.com/help.cgi?diagnostic%20plots) | quantile plots                                     |
| [<strong>qnorm</strong>](http://www.stata.com/help.cgi?diagnostic%20plots)    | quantile<span options="1">_normal plots      |
| [<strong>pnorm</strong>](http://www.stata.com/help.cgi?diagnostic%20plots)    | normal probability plots, standardized             |
| [<strong>qchi</strong>](http://www.stata.com/help.cgi?diagnostic%20plots)     | chi-squared quantile plots                         |
| [<strong>pchi</strong>](http://www.stata.com/help.cgi?diagnostic%20plots)     | chi-squared probability plots                      |
| [<strong>qqplot</strong>](http://www.stata.com/help.cgi?diagnostic%20plots)   | quantile<span options="1">_quantile plots    |
| [<strong>gladder</strong>](http://www.stata.com/help.cgi?gladder)             | ladder-of-powers plots                             |
| [<strong>qladder</strong>](http://www.stata.com/help.cgi?qladder)             | ladder-of-powers quantiles                         |
| [<strong>spikeplot</strong>](http://www.stata.com/help.cgi?spikeplot)         | spike plots and rootograms                         |
| [<strong>dotplot</strong>](http://www.stata.com/help.cgi?dotplot)             | means or medians by group                          |
| [<strong>sunflower</strong>](http://www.stata.com/help.cgi?sunflower)         | density-distribution sunflower plots {p2line None} |

Smoothing and densities:

|                                                                                                |                                          |
|------------------------------------------------------------------------------------------------|------------------------------------------|
| Command                                                                                        | Description {p2line None}                |
| [<strong>kdensity</strong>](http://www.stata.com/help.cgi?kdensity) | kernel density estimation, univariate    |
| [<strong>lowess</strong>](http://www.stata.com/help.cgi?lowess)     | lowess smoothing                         |
| [<strong>lpoly</strong>](http://www.stata.com/help.cgi?lpoly)       | local polynomial smoothing {p2line None} |

Regression diagnostics:

|                                                                                                |                                               |
|------------------------------------------------------------------------------------------------|-----------------------------------------------|
| Command                                                                                        | Description {p2line None}                     |
| [<strong>avplot</strong>](http://www.stata.com/help.cgi?avplot)     | added-variable (leverage) plots               |
| [<strong>cprplot</strong>](http://www.stata.com/help.cgi?cprplot)   | component-plus-residual plots                 |
| [<strong>lvr2plot</strong>](http://www.stata.com/help.cgi?lvr2plot) | L-R (leverage-versus-squared-residual) plots  |
| [<strong>rvfplot</strong>](http://www.stata.com/help.cgi?rvfplot)   | residual-versus-fitted plots                  |
| [<strong>rvpplot</strong>](http://www.stata.com/help.cgi?rvpplot)   | residual-versus-predicted plots {p2line None} |

Time series:

|                                                                                                            |                                                                                    |
|------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| Command                                                                                                    | Description {p2line None}                                                          |
| [<strong>ac</strong>](http://www.stata.com/help.cgi?ac)                         | correlograms                                                                       |
| [<strong>pac</strong>](http://www.stata.com/help.cgi?pac)                       | partial correlograms                                                               |
| [<strong>pergram</strong>](http://www.stata.com/help.cgi?pergram)               | periodograms                                                                       |
| [<strong>cumsp</strong>](http://www.stata.com/help.cgi?cumsp)                   | spectral distribution plots, cumulative                                            |
| [<strong>xcorr</strong>](http://www.stata.com/help.cgi?xcorr)                   | cross-correlograms for bivariate time series                                       |
| [<strong>wntestb</strong>](http://www.stata.com/help.cgi?wntestb)               | Bartlett's periodogram-based white-noise test                                      |
| [<strong>estat acplot</strong>](http://www.stata.com/help.cgi?estat%20acplot)   | parametric autocorrelation and autocovariance functions after `arima` and `arfima` |
| [<strong>estat aroots</strong>](http://www.stata.com/help.cgi?estat%20aroots)   | eigenvalues of the companion matrices after `arima`                                |
| [<strong>estat sbcusum</strong>](http://www.stata.com/help.cgi?estat%20sbcusum) | cumulative sum test for parameter stability {p2line None}                          |

Vector autoregressive (VAR, SVAR, VECM) models:

|                                                                                                        |                                                                                      |
|--------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| Command                                                                                                | Description {p2line None}                                                            |
| [<strong>fcast graph</strong>](http://www.stata.com/help.cgi?fcast%20graph) | `var`, `svar`, and `vec` forecasts                                                   |
| [<strong>varstable</strong>](http://www.stata.com/help.cgi?varstable)       | eigenvalues of the companion matrix after `var` and `svar`                           |
| [<strong>vecstable</strong>](http://www.stata.com/help.cgi?vecstable)       | eigenvalues of the companion matrix after `vec`                                      |
| [<strong>irf graph</strong>](http://www.stata.com/help.cgi?irf%20graph)     | impulse-response functions (IRFs) and forecast-error variance decompositions (FEVDs) |
| [<strong>irf ograph</strong>](http://www.stata.com/help.cgi?irf%20ograph)   | overlaid IRFs and FEVDs                                                              |
| [<strong>irf cgraph</strong>](http://www.stata.com/help.cgi?irf%20cgraph)   | combined IRFs and FEVDs {p2line None}                                                |

Longitudinal data/panel data:

|                                                                                            |                                     |
|--------------------------------------------------------------------------------------------|-------------------------------------|
| Command                                                                                    | Description {p2line None}           |
| [<strong>xtline</strong>](http://www.stata.com/help.cgi?xtline) | panel-data line plots {p2line None} |

Survival analysis:

|                                                                                                            |                                                                       |
|------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| Command                                                                                                    | Description {p2line None}                                             |
| [<strong>sts graph</strong>](http://www.stata.com/help.cgi?sts%20graph)         | survivor, hazard, or cumulative-hazard functions                      |
| [<strong>strate</strong>](http://www.stata.com/help.cgi?strate)                 | failure rates and cumulative hazard comparisons                       |
| [<strong>ltable</strong>](http://www.stata.com/help.cgi?ltable)                 | life tables                                                           |
| [<strong>stci</strong>](http://www.stata.com/help.cgi?stci)                     | means and percentiles of survival time, with CIs                      |
| [<strong>stphplot</strong>](http://www.stata.com/help.cgi?stphplot)             | log-log plots                                                         |
| [<strong>stcoxkm</strong>](http://www.stata.com/help.cgi?stcoxkm)               | Kaplan<span options="1">_Meier observed survival curves         |
| [<strong>estat phtest</strong>](http://www.stata.com/help.cgi?estat%20phtest)   | verify proportional-hazards assumption                                |
| [<strong>stcurve</strong>](http://www.stata.com/help.cgi?stcurve)               | survivor, hazard, cumulative hazard, or cumulative incidence function |
| [<strong>estat gofplot</strong>](http://www.stata.com/help.cgi?estat%20gofplot) | goodness of fit of models for interval-censored data {p2line None}    |

ROC analysis:

|                                                                                                    |                                                                     |
|----------------------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| Command                                                                                            | Description {p2line None}                                           |
| [<strong>roctab</strong>](http://www.stata.com/help.cgi?roctab)         | ROC curve                                                           |
| [<strong>rocplot</strong>](rocfit_postestimation##rocplot)              | parametric ROC curve                                                |
| [<strong>roccomp</strong>](http://www.stata.com/help.cgi?roccomp)       | multiple ROC curves, compared                                       |
| [<strong>rocregplot</strong>](http://www.stata.com/help.cgi?rocregplot) | marginal and covariate-specific ROC curves                          |
| [<strong>lroc</strong>](http://www.stata.com/help.cgi?lroc)             | ROC curve after `logistic`, `logit`, `probit`, and `ivprobit`       |
| [<strong>lsens</strong>](http://www.stata.com/help.cgi?lsens)           | sensitivity and specificity versus probability cutoff {p2line None} |

Item response theory:

|                                                                                                          |                                              |
|----------------------------------------------------------------------------------------------------------|----------------------------------------------|
| Command                                                                                                  | Description {p2line None}                    |
| [<strong>irtgraph icc</strong>](http://www.stata.com/help.cgi?irtgraph%20icc) | Item characteristic curve plot               |
| [<strong>irtgraph tcc</strong>](http://www.stata.com/help.cgi?irtgraph%20tcc) | Test characteristic curve plot               |
| [<strong>irtgraph iif</strong>](http://www.stata.com/help.cgi?irtgraph%20iif) | Item information function plot               |
| [<strong>irtgraph tif</strong>](http://www.stata.com/help.cgi?irtgraph%20tif) | Test information function plot {p2line None} |

Multivariate analysis:

|                                                                                                                      |                                                     |
|----------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
| Command                                                                                                              | Description {p2line None}                           |
| [<strong>biplot</strong>](http://www.stata.com/help.cgi?biplot)                           | biplot                                              |
| [<strong>cluster dendrogram</strong>](http://www.stata.com/help.cgi?cluster%20dendrogram) | dendrograms for hierarchical cluster analysis       |
| [<strong>screeplot</strong>](http://www.stata.com/help.cgi?screeplot)                     | scree plot of eigenvalues                           |
| [<strong>scoreplot</strong>](http://www.stata.com/help.cgi?scoreplot)                     | factor or component score plot                      |
| [<strong>loadingplot</strong>](http://www.stata.com/help.cgi?loadingplot)                 | factor or component loading plot                    |
| [<strong>procoverlay</strong>](http://www.stata.com/help.cgi?procoverlay)                 | Procrustes overlay plot                             |
| [<strong>cabiplot</strong>](http://www.stata.com/help.cgi?cabiplot)                       | correspondence analysis biplot                      |
| [<strong>caprojection</strong>](http://www.stata.com/help.cgi?caprojection)               | correspondence analysis dimension projection plot   |
| [<strong>mcaplot</strong>](http://www.stata.com/help.cgi?mcaplot)                         | plot of category coordinates                        |
| [<strong>mcaprojection</strong>](http://www.stata.com/help.cgi?mcaprojection)             | MCA dimension projection plot                       |
| [<strong>mdsconfig</strong>](http://www.stata.com/help.cgi?mdsconfig)                     | multidimensional scaling configuration plot         |
| [<strong>mdsshepard</strong>](http://www.stata.com/help.cgi?mdsshepard)                   | multidimensional scaling Shepard plot {p2line None} |

Quality-control charts:

|                                                                                                |                                         |
|------------------------------------------------------------------------------------------------|-----------------------------------------|
| Command                                                                                        | Description {p2line None}               |
| [<strong>cusum</strong>](http://www.stata.com/help.cgi?cusum)       | cusum plots                             |
| [<strong>cchart</strong>](http://www.stata.com/help.cgi?cchart)     | c (control) charts                      |
| [<strong>pchart</strong>](http://www.stata.com/help.cgi?pchart)     | p (fraction-defective) charts           |
| [<strong>rchart</strong>](http://www.stata.com/help.cgi?rchart)     | R (range or dispersion) charts          |
| [<strong>xchart</strong>](http://www.stata.com/help.cgi?xchart)     | X-bar (control line) charts             |
| [<strong>shewhart</strong>](http://www.stata.com/help.cgi?shewhart) | X-bar and R charts, vertically aligned  |
| [<strong>serrbar</strong>](http://www.stata.com/help.cgi?serrbar)   | standard error bar charts {p2line None} |

Other statistical graphs:

|                                                                                                                  |                                                                                                                                          |
|------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| Command                                                                                                          | Description {p2line None}                                                                                                                |
| [<strong>marginsplot</strong>](http://www.stata.com/help.cgi?marginsplot)             | graph of results from [<strong>margins</strong>](http://www.stata.com/help.cgi?margins) (profile plots, etc.) |
| [<strong>bayesgraph</strong>](http://www.stata.com/help.cgi?bayesgraph)               | graph of results from [<strong>bayesmh</strong>](http://www.stata.com/help.cgi?bayesmh)                       |
| [<strong>power, graph</strong>](http://www.stata.com/help.cgi?power_optgraph)         | graph of results from [<strong>power</strong>](http://www.stata.com/help.cgi?power)                           |
| [<strong>tabodds</strong>](http://www.stata.com/help.cgi?tabodds)                     | odds-of-failure versus categories                                                                                                        |
| [<strong>teffects overlap</strong>](http://www.stata.com/help.cgi?teffects%20overlap) | overlap plots                                                                                                                            |
| [<strong>npgraph</strong>](http://www.stata.com/help.cgi?npgraph)                     | conditional mean function                                                                                                                |
| [<strong>grmap</strong>](http://www.stata.com/help.cgi?grmap)                         | visualization of spatial data                                                                                                            |
| [<strong>pkexamine</strong>](http://www.stata.com/help.cgi?pkexamine)                 | summarize pharmacokinetic data {p2line None}                                                                                             |
