from scipy.stats import chisquare
import pandas as pd

ret_csv = 'data/return.csv'

def main():
    df = pd.read_csv(ret_csv)
    for col in df.columns:
        stat, pvalue = chisquare(df[col])
        if pvalue > 0.05:
            print(col, pvalue)

if __name__=='__main__':
    main()