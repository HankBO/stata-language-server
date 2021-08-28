## Syntax

`dnormalden(z)dnormalden(x,sd)dnormalden(x,meansd)pnormal(z)zinvnormal(p)ln(d)lnnormalden(z)ln(d)lnnormalden(x,sd)ln(d)lnnormalden(x,meansd)ln(p)lnnormal(z)pbinormal(z1,z2,rho)ln(d)lnmvnormalden(M,V,X)dbetaden(a,b,x)pibeta(a,b,x)qibetatail(a,b,x)xinvibeta(a,b,p)xinvibetatail(a,b,q)pkbinomialp(n,k,pi)pbinomial(n,k,pi)qbinomialtail(n,k,pi)piinvbinomial(n,k,p)piinvbinomialtail(n,k,q)dcauchyden(a,b,x)pcauchy(a,b,x)qcauchytail(a,b,x)xinvcauchy(a,b,p)xinvcauchytail(a,b,q)ln(d)lncauchyden(a,b,x)dchi2den(df,x)pchi2(df,x)qchi2tail(df,x)xinvchi2(df,p)xinvchi2tail(df,q)pdunnettprob(k,df,x)xinvdunnettprob(k,df,p)dexponentialden(b,x)pexponential(b,x)qexponentialtail(b,x)xinvexponential(b,p)xinvexponentialtail(b,q)dFden(df1,df2,f)pF(df1,df2,f)qFtail(df1,df2,f)finvF(df1,df2,p)finvFtail(df1,df2,q)dgammaden(a,b,g,x)pgammap(a,x)qgammaptail(a,x)xinvgammap(a,p)xinvgammaptail(a,q)dg/dadgammapda(a,x)dg/dxdgammapdx(a,x)d2g/da2dgammapdada(a,x)d2g/dadxdgammapdadx(a,x)d2g/dx2dgammapdxdx(a,x)ln(d)lnigammaden(a,b,x)pkhypergeometricp(N,K,n,k)phypergeometric(N,K,n,k)digaussianden(m,a,x)pigaussian(m,a,x)qigaussiantail(m,a,x)xinvigaussian(m,a,p)xinvigaussiantail(m,a,q)ln(d)lnigaussianden(m,a,x)dlaplaceden(m,b,x)plaplace(m,b,x)qlaplacetail(m,b,x)xinvlaplace(m,b,p)xinvlaplacetail(m,b,q)ln(d)lnlaplaceden(m,b,x)dlogisticden(x)dlogisticden(s,x)dlogisticden(m,s,x)plogistic(x)plogistic(s,x)plogistic(m,s,x)qlogistictail(x)qlogistictail(s,x)qlogistictail(m,s,x)xinvlogistic(p)xinvlogistic(s,p)xinvlogistic(m,s,p)xinvlogistictail(q)xinvlogistictail(s,q)xinvlogistictail(m,s,q)pknbinomialp(n,k,pi)pnbinomial(n,k,pi)qnbinomialtail(n,k,pi)piinvnbinomial(n,k,p)piinvnbinomialtail(n,k,q)dnbetaden(a,b,np,x)pnibeta(a,b,np,x)xinvnibeta(a,b,np,p)dnchi2den(df,np,x)pnchi2(df,np,x)qnchi2tail(df,np,x)xinvnchi2(df,np,p)xinvnchi2tail(df,np,q)npnpnchi2(df,x,p)dnFden(df1,df2,np,f)pnF(df1,df2,np,f)qnFtail(df1,df2,np,f)finvnF(df1,df2,np,p)finvnFtail(df1,df2,np,q)npnpnF(df1,df2,f,p)dntden(df,np,t)pnt(df,np,t)qnttail(df,np,t)tinvnt(df,np,p)tinvnttail(df,np,q)npnpnt(df,t,p)pkpoissonp(mean,k)ppoisson(mean,k)qpoissontail(mean,k)minvpoisson(k,p)minvpoissontail(k,q)dtden(df,t)pt(df,t)qttail(df,t)tinvt(df,p)tinvttail(df,q)ptukeyprob(k,df,x)xinvtukeyprob(k,df,p)dweibullden(a,b,x)dweibullden(a,b,g,x)pweibull(a,b,x)pweibull(a,b,g,x)qweibulltail(a,b,x)qweibulltail(a,b,g,x)xinvweibull(a,b,p)xinvweibull(a,b,g,p)xinvweibulltail(a,b,q)xinvweibulltail(a,b,g,q)dweibullphden(a,b,x)dweibullphden(a,b,g,x)pweibullph(a,b,x)pweibullph(a,b,g,x)qweibullphtail(a,b,x)qweibullphtail(a,b,g,x)xinvweibullph(a,b,p)xinvweibullph(a,b,g,p)xinvweibullphtail(a,b,q)xinvweibullphtail(a,b,g,q)ln(d)lnwishartden(df,V,X)ln(d)lniwishartden(df,V,X)`

where

1\. All functions return real and all arguments are real or real
matrices.

2\. The left-hand-side notation is used to assist in interpreting the
meaning of the returned value:

`dpkpstatistic`

`x`

<!-- -->

`qp`

`npln(p)ln(d)`

3\. Hypergeometric distribution:

`NKKNnnNknNK`

`k`

`Kn`

4\. Negative binomial distribution: `n` &gt; 0 and may be nonintegral.

5\. Multivariate normal, Wishart, and inverse Wishart distributions:

`MVX`
