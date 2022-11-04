from scipy.stats import chisquare, shapiro
import pandas as pd

ret_csv = 'data/return.csv'

def main():
    df = pd.read_csv(ret_csv)
    norm = 0
    for col in df.columns:
        stat, pvalue = shapiro(df[col])
        if pvalue >= 0.05:
            norm += 1
            print(col, pvalue)
    print(norm)

if __name__=='__main__':
    main()