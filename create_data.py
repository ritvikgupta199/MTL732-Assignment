from tqdm import tqdm
import numpy as np
import pandas as pd
import os

ret_csv = 'data/return.csv'
tickers = 'symbols.csv'
tickers = [l.strip() for l in open(tickers,'r').readlines()[:10]]

def main():
    df = pd.read_csv(ret_csv)
    df = df[tickers]
    cov = df.cov()
    cov.to_csv('data/cov_matrix.csv', index=False)

    mean = df.mean()
    mean.to_csv('data/mean.csv')

if __name__=='__main__':
    main()