from tqdm import tqdm
import numpy as np
import pandas as pd
import os

nstocks = [20, 30, 50]
ret_csv = 'data/return.csv'
tickers = 'symbols_final.csv'
save_dir = 'data/generated/'

if not os.path.exists(save_dir):
    os.makedirs(save_dir)

tickers = [l.strip() for l in open(tickers,'r').readlines()]

def main():
    for nstock in nstocks:
        df = pd.read_csv(ret_csv)
        df = df[tickers[:nstock]]

        cov = df.cov()
        if(np.linalg.det(cov.to_numpy()) == 0):
            print("C is singular")
        cov.to_csv(os.path.join(save_dir, f'cov_matrix_{nstock}.csv'), index=False)

        mean = df.mean()
        mean.to_csv(os.path.join(save_dir, f'mean_{nstock}.csv'))

if __name__=='__main__':
    main()