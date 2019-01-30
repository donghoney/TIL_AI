import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from scipy.stats import norm
from datetime import datetime
import datetime as dt
import os
from get_rawdata import read_csv,read_KS200_symbol

## 가설 수립
# 1. H_0 : KOSPI200 지수의 평균 수익률이 0이하이다.
# 2. H_1 : KOSPI200 지수의 평균 수익률이 0이상이다.

# ex) type(df) = <class 'pandas.core.frame.DataFrame'> , start = '20150102' , end = '20180601'
def calculate_p_val(df,start,end):
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date',inplace=True)
    FT = df[start:end]
    price = FT['Close']
    returns = price.pct_change()[1:]
    n = len(returns)
    test_statistic = ((returns.mean() - 0 )/ (returns.std() / np.sqrt( n - 1 )))
    #print('t test statistic : ', test_statistic)
    p_val = ( 1 - norm.cdf(test_statistic,0,1))
    #print('P - value is : ' ,p_val)
    return p_val



def stock_eval():
    data_path = './data'
    KS200_name = 'KOSPI200.csv'
    KS200_jisu_name = 'KS200_jisu.csv'
    KS200_list=read_KS200_symbol(data_path,KS200_name)
    KS200_jisu=read_csv(data_path,KS200_jisu_name)
    print(KS200_list)
    start = '20150102'
    end = '20180601'
    p_val_list = []
    for i,j in KS200_list:
        df = read_csv(data_path, i)
        p_val=calculate_p_val(df,start,end)
        p_val_list.append((i,j,p_val))
    print(p_val_list)
    sorted_p_val=sorted(p_val_list, key=lambda x : x[2])
    print(len(KS200_list))
    print(len(KS200_jisu))
    print(sorted_p_val[:100])
if __name__ == "__main__":
    stock_eval()


