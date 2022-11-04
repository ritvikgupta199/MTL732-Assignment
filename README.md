# MTL732-Assignment

## Chance-constrained optimization

The optimization problem for chance-constrained optimization is given by -
$$
\begin{aligned}
\max_{w} \quad & w^{T}\mu \\
\textrm{s.t.} \quad & \phi^{-1}(\alpha) || C^{1/2} w||_2 \leq w^{T}\mu + d\\
  & \sum_{i=1}^n w_i = 1\\
  & w_i \geq 0, \quad i=1,\ldots,n
\end{aligned}
$$
We have used CVXPY to solve the optimization problem. As the chance-constrained optmization problem is a Second Order Cone Problem (SOCP), we use the SOCP solver from CVXPY to find the optimum point of the problem. The SOCP solver solves the following problem:
$$
\begin{aligned}
\min_{} \quad & f^{T}x \\
\textrm{s.t.} \quad & ||A_i x + b_i||_2 \leq c_i^Tx+d_i, \quad i=1,\ldots,n \\
  & Fx=g\\
\end{aligned}
$$

Comparing our formulation to this form, we get,
$$
f = \mu; \quad F = [1, 1, 1, \ldots 1]; \quad g = 1 \\ 
A_0 = C^{1/2} * (\phi^{-1}(\alpha)); \quad b_0 = 0; \quad c_0 = \mu; \quad d_0 = d;
$$