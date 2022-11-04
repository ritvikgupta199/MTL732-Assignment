import cvxpy as cp
import numpy as np
import pandas as pd
import argparse
import scipy
import os
from scipy.stats import norm

nstocks = [20, 30, 50]

def setup():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_dir', type=str, default='data/generated/')
    parser.add_argument('--alpha', type=float, default=0.9)
    parser.add_argument('--d', type=float, default=0.1)
    parser.add_argument('--short', action='store_true', default=False)
    args = parser.parse_args()
    return args

def main():
    args = setup()
    ws = []
    for nstock in nstocks:
        C = pd.read_csv(os.path.join(args.data_dir, f'cov_matrix_{nstock}.csv')).to_numpy()
        mu = pd.read_csv(os.path.join(args.data_dir, f'cov_matrix_{nstock}.csv')).iloc[:, 1].to_numpy()
        alpha = args.alpha
        d = args.d
        n = len(mu)
        # print(n, mu)
        phi = norm.ppf(alpha) # inv normal cdf

        F = np.ones(n)
        g = 1
        A0 = scipy.linalg.cholesky(C, lower=True) #cholesky decomposition of C
        c0 = mu / phi
        d0 = d / phi

        w = cp.Variable(n)
        constraints = [
            cp.SOC(c0.T @ w + d0, A0 @ w),
        ]

        w_eq = [1/nstock for _ in range(nstock)]
        phi * norm()

        if not args.short:
            prob = cp.Problem(cp.Maximize(mu.T @ w), constraints + [F @ w == g] + [w >= 0])
        else:
            prob = cp.Problem(cp.Maximize(mu.T @ w), constraints + [F @ w == g])
        sol = prob.solve(verbose = False)
        sol_eq = np.dot(w_eq, mu)
        print("expected return", sol)
        print("expected return if equally distributed", sol_eq)
        print("weights", w.value)
        ws.append(w.value)
    return ws

if __name__=='__main__':
    main()