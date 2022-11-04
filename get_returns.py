from tqdm import tqdm
import numpy as np
import pandas as pd
import json
import os

read_symbols = 'snp500sym.csv'
write_symbols = 'symbols.csv'
write_csv = 'data/return.csv'
min_time = 400
offset=1
def get_prices(filename):
    syms = []
    prices = {}
    fr = open(filename,'r')
    for line in fr.readlines():
        symbol = line.strip()
        syms.append(symbol)
        prices[symbol] = []
    fr.close()
    for symbol in tqdm(syms):
        try:
            f = open('data/TIME_SERIES_DAILY/'+symbol+'.json','r')
            data = json.load(f)
            f.close()
            data = data["Time Series (Daily)"]
            for record in data.keys():
                prices[symbol].append(float(data[record]["4. close"]))
        except:
            pass

    return prices

def get_returns(prices):
    prices = np.array(prices)
    returns = np.diff(prices)/prices[:-offset]
    return returns[-min_time:]

def main():
    print("Fetching prices...")
    prices = get_prices(read_symbols)

    print("Calculating returns...")
    returns = {}
    fw = open(write_symbols, 'w')
    for symbol in tqdm(prices.keys()):
        if len(prices[symbol]) >= min_time + 1:
            ret = get_returns(prices[symbol])
            returns[symbol] = ret
            fw.write(f"{symbol}\n")
    fw.close()

    df = pd.DataFrame(returns)
    df.to_csv(write_csv, index=False)

if __name__=='__main__':
    main()