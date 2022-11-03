# MTL732-Assignment

## Chance-constrained optimization

$$
\begin{aligned}
\min_{w} \quad & w^{T}\mu \\
\textrm{s.t.} \quad & -w^{T}\mu + \phi^{-1}(\alpha) || C^{1/2} w||_2 \leq d\\
  & \sum_{i=1}^n w_i = 1\\
  & w_i \geq 0, \quad i=1,\ldots,n
\end{aligned}
$$

CVXPY provides Second Order Cone Programming (SOCP) solvers. The SOCP solver solves the following problem:
$$
\begin{aligned}
\min_{} \quad & f^{T}x \\
\textrm{s.t.} \quad & ||A_i x + b_i||_2 \leq c_i^Tx+d_i, \quad i=1,\ldots,n \\
  & Fx=g\\
\end{aligned}
$$

Comparing our formulation to this form, we get,
$ 
f = \mu; \quad F = [1, 1, 1, \ldots 1]; \quad g = 1 \\ 
A_0 = C^{1/2}; \quad b_0 = 0; \quad c_0 = \mu*(\phi^{-1}(\alpha))^{-1}; \quad d_0 = (\phi^{-1}(\alpha))^{-1}d;
$