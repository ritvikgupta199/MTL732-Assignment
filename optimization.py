import cvxpy as cp
import numpy as np
import pandas as pd
import argparse
import scipy
from scipy.stats import norm


# def setup():
#     parser = argparse.ArgumentParser()
#     parser.add_argument('--cov', type=str, default='data/cov_matrix.csv')
#     parser.add_argument('--mean', type=str, default='data/mean.csv')
#     parser.add_argument('--alpha', type=float, default=0.6)
#     parser.add_argument('--d', type=float, default=0.6)
#     args = parser.parse_args()
#     return args

def setup():
    parser = argparse.ArgumentParser()
    parser.add_argument('--cov', type=str, default='data/cov_matrix_d.csv')
    parser.add_argument('--mean', type=str, default='data/mean_d.csv')
    parser.add_argument('--alpha', type=float, default=0.6)
    parser.add_argument('--d', type=float, default=0.6)
    args = parser.parse_args()
    return args

def main():
    args = setup()
    C = pd.read_csv(args.cov).to_numpy()
    mu = pd.read_csv(args.mean).iloc[:, 1].to_numpy()
    alpha = args.alpha
    d = args.d
    n = len(mu)
    print(n, mu)
    phi = norm.ppf(alpha) # inv normal cdf

    F = np.ones(n)
    g = 1
    A0 = scipy.linalg.cholesky(C, lower=True) #cholesky decomposition of C
    c0 = mu * phi
    d0 = d * phi

    w = cp.Variable(n)
    constraints = [
        cp.SOC(c0.T @ w + d0, A0 @ w),
    ]
    prob = cp.Problem(cp.Maximize(mu.T @ w), constraints + [F @ w == g])
    # prob = cp.Problem(cp.Minimize(mu.T @ w), constraints + [F @ w == g])
    # sol = prob.solve(verbose = True)
    sol = prob.solve()
    # prob.solve()
    print(sol)


if __name__=='__main__':
    main()