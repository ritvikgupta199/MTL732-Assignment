import cvxpy as cp
import numpy as np
import pandas as pd
import argparse

def setup():
    parser = argparse.ArgumentParser()
    parser.add_argument('--cov', type=str, default='data/cov_matrix.csv')
    parser.add_argument('--mean', type=str, default='data/mean.csv')
    parser.add_argument('--alpha', type=float, default=0.6)
    args = parser.parse_args()
    return args

def main():
    args = setup()
    C = pd.read_csv(args.cov).to_numpy()
    mu = pd.read_csv(args.mean).iloc[:, 1].to_numpy()
    alpha = args.alpha
    n = len(mu)


    F = np.ones(n)
    g = 1
    A0 = C #C^1/2
    c0 = mu * alpha
    d0 = d * alpha

    w = cp.Variable(n)
    constraints = [
        cp.SOC(c0.T @ w + d0, A0 @ w),
    ]
    prob = cp.Minimise(mu.T @ w, constraints + [F @ w == g])


if __name__=='__main__':
    main()