from tqdm import tqdm
import numpy as np
import pandas as pd
from scipy.stats import norm
import scipy
import os

nstocks = [20, 30, 50]
ret_csv = 'data/return.csv'
tickers = 'symbols_final.csv'
save_dir = 'data/generated/'
alpha = 0.9

if not os.path.exists(save_dir):
    os.makedirs(save_dir)

tickers = [l.strip() for l in open(tickers,'r').readlines()]

def main():
    for nstock in nstocks:
        df = pd.read_csv(ret_csv)
        df = df[tickers[:nstock]]

        cov = df.cov()
        cov_matrix = cov.to_numpy()
        if(np.linalg.det(cov_matrix) == 0):
            print("C is singular")
        cov.to_csv(os.path.join(save_dir, f'cov_matrix_{nstock}.csv'), index=False)

        mean = df.mean()
        mu = mean.to_numpy()
        mean.to_csv(os.path.join(save_dir, f'mean_{nstock}.csv'))

        n = len(mean)
        w_eq = np.ones(n) / n
        phi = norm.ppf(alpha)
        C = scipy.linalg.cholesky(cov_matrix, lower=True)
        print(f"For {nstock} stocks, maximum d value: {phi*np.linalg.norm(C @ w_eq) - mu.T@w_eq}")

if __name__=='__main__':
    main()