from scipy.stats import chisquare, shapiro
import pandas as pd

ret_csv = 'data/return.csv'
ticker_file = 'symbols_final.csv'

def main():
    fw = open(ticker_file, 'w')
    df = pd.read_csv(ret_csv)
    norm = 0
    for col in df.columns:
        stat, pvalue = shapiro(df[col])
        if pvalue >= 0.05:
            norm += 1
            fw.write(col + '\n')
    print(f"{norm} stocks follow normal distribution")
    fw.close()
if __name__=='__main__':
    main()