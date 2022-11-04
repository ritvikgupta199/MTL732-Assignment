# MTL732-Assignment

## Chance-constrained optimization

Suppose, $K \sim N( \mu, C)$,
If $X = (X_1, X_2, X_3, \ldots, X_n)$ follows multivariate normal distribution, then $w^T\mu$ is also normally distributed.
$$K \sim N( \mu, C) \implies -w^TK \sim N(-w^T\mu, w^TCw)$$

Consider, $\mathbb{P}(-w^TK \leq d) \geq \alpha$,
$$\implies \mathbb{P} \left( \frac{-w^TK + w^T\mu}{\sqrt{w^TCw}} \leq \frac{d + w^T\mu}{\sqrt{w^TCw}} \right) \geq \alpha$$

Note that, 
$$-w^TK \sim N(-w^T\mu, w^TCw) \implies \frac{-w^TK + w^t\mu}{\sqrt{w^TCw}} \sim N(0,1)$$
$$ 
\therefore \phi\left(  \frac{d + w^t\mu}{\sqrt{w^TCw}} \right) \geq \alpha\\
\implies \frac{d + w^t\mu}{\sqrt{w^TCw}} \geq \phi^{-1}(\alpha) \\
\implies \phi^{-1}(\alpha) ||C^{1/2}w||_2 \leq w^T\mu +d
$$
Hence, we have the chance-constrained optimization problem as,
$$
\begin{aligned}
\max_{w} \quad & \mu^{T}w \\
\textrm{s.t.} \quad & \phi^{-1}(\alpha) || C^{1/2} w||_2 \leq \mu^{T}w + d\\
  & \sum_{i=1}^n w_i = 1\\
  & w_i \geq 0, \quad i=1,\ldots,n
\end{aligned}
$$
This is a convex set for $\alpha \in [0.5, 1]$,

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
x=w; \quad f = \mu; \quad F = [1, 1, 1, \ldots 1]; \quad g = 1 \\ 
A_0 = C^{1/2} * (\phi^{-1}(\alpha)); \quad b_0 = 0; \quad c_0 = \mu; \quad d_0 = d;
$$