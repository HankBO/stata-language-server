## Syntax

|     |                  |                          |
|-----|------------------|--------------------------|
|     | `real colvector` | `mvnormal(U, R)`         |
|     | `real colvector` | `mvnormal(L, U, R)`      |
|     | `real colvector` | `mvnormalcv(L, U, M, V)` |

|     |                  |                               |
|-----|------------------|-------------------------------|
|     | `real colvector` | `mvnormalqp(U, R, q)`         |
|     | `real colvector` | `mvnormalqp(L, U, R, q)`      |
|     | `real colvector` | `mvnormalcvqp(L, U, M, V, q)` |

|     |        |                                               |
|-----|--------|-----------------------------------------------|
|     | `void` | `mvnormalderiv(U, R, dU, dR)`                 |
|     | `void` | `mvnormalderiv(L, U, R, dL, dU, dR)`          |
|     | `void` | `mvnormalcvderiv(L, U, M, V, dL, dU, dM, dV)` |

|     |        |                                                    |
|-----|--------|----------------------------------------------------|
|     | `void` | `mvnormalderivqp(U, R, dU, dR, q)`                 |
|     | `void` | `mvnormalderivqp(L, U, R, dL, dU, dR, q)`          |
|     | `void` | `mvnormalcvderivqp(L, U, M, V, dL, dU, dM, dV, q)` |

where

`Lreal matrix LUreal matrix UMreal matrix MRreal matrix RVreal matrix Vqreal scalar q`

The types of `dL`, `dU`, `dM`, `dR`, and `dV` are irrelevant; results
are returned there as real matrices.
