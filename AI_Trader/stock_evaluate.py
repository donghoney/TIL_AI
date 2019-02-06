import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from scipy.stats import norm
from datetime import datetime
import datetime as dt
import os
from get_rawdata import read_csv,read_KS200_symbol

def midvalue(lst):
    return [i for i in sorted(lst)][len(lst) //2]

def short_item_remove(data_path,KS200_list):
    row_list = []
    for i, j in KS200_list:
        df = read_csv(data_path, i)
        row_list.append((df.shape[0]))

    mid_row = midvalue(row_list)
    print('KOSPI 200의 종목들 상장기간 중간값 : {}'.format(mid_row))
    print(len(row_list))
    print(len(KS200_list))
    new_list =[]
    for i,j in enumerate(row_list):
        # j는 행 수
        if mid_row==j:
            new_list.append((KS200_list[i][0],KS200_list[i][1]))
    print('상장 기간이 짧은 KOSPI 200 종목을 뺀 리스트 길이 : {}'.format(len(new_list)))
    return new_list



## 가설 수립
# 1. H_0 : 해당 회사 주식의 평균 수익률이 0이하이다.
# 2. H_1 : 해당 회사 주식의 평균 수익률이 0이상이다.
# ex) type(df) = <class 'pandas.core.frame.DataFrame'> , start = '20150102' , end = '20180601'
def calculate_yield_p_val(df,start,end):
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

## 가설 수립
# 1. H_0 : 해당 회사 주식(df2)의 평균 수익률에서 시장(df1)의 평균 수익률을 뺀 값이 0이다.
# 2. H_1 : 해당 회사 주식(df2)의 평균 수익률에서 시장(df1)의 평균 수익률을 뺀 값이 0이 아니다.
# ex) type(df1,df2) = <class 'pandas.core.frame.DataFrame'> , start = '20150102' , end = '20180601'
def calculate_diff_p_val(df1,df2,start,end):
    df1['Date'] = pd.to_datetime(df1['Date'])
    df1.set_index('Date', inplace=True)

    df2['Date'] = pd.to_datetime(df2['Date'])
    df2.set_index('Date', inplace=True)
    FT1 = df1[start:end]
    FT2 = df2[start:end]

    FT2=FT2.fillna(method='ffill')
    FT2=FT2.fillna(method='bfill')

    df1_price = FT1['Close']
    df2_price = FT2['Close']
    df1_returns = df1_price.pct_change()[1:]
    df2_returns = df2_price.pct_change()[1:]

    mu_df1 = df1_returns.mean()
    mu_df2 = df2_returns.mean()

    s_df1 = df1_returns.std()
    s_df2 = df2_returns.std()

    n_df1 = len(df1_returns)
    n_df2 = len(df2_returns)
    #print(mu_df2,s_df2,n_df2)
    test_statistic = ((mu_df2 - mu_df1) - 0) / ((s_df1 ** 2 / n_df1) + (s_df2 ** 2 / n_df2)) ** 0.5
    df = ((s_df1 ** 2 / n_df1) + (s_df2 ** 2 / n_df2)) ** 2 / (
                ((s_df1 ** 2 / n_df1) ** 2 / n_df1) + ((s_df2** 2 / n_df2) ** 2 / n_df2))
    p_val = (1 - norm.cdf(test_statistic, 0, 1))
    #if df>30:
    #    print('자유도가 30이상으로 매우 높으므로, 신뢰도 95% 구간은 [-1.96,1.96]입니다')
    #else :
    #    print('자유도가 30 미만이므로, 신뢰도 95% 구간은 [-1.96,1.96]이라고 볼 수 없습니다.')

    return p_val

def stock_eval():
    data_path = './data'
    KS200_name = 'KOSPI200.csv'
    KS200_jisu_name = 'KS200_jisu.csv'
    yeild_hypothesis_test = True
    diff_hypothesis_test = True

    KS200_list=read_KS200_symbol(data_path,KS200_name)
    KS200_jisu=read_csv(data_path,KS200_jisu_name)

    #상장된 날짜가 코스피200 종목 평균보다 작은 종목 리스트에서 제거
    KS200_list=short_item_remove(data_path, KS200_list)

    start = '20150102'
    end = '20180601'


    h1_list = []
    h2_list = []
    result_list = []
    if yeild_hypothesis_test == True:
        p_val_list = []
        for i,j in KS200_list:
            df = read_csv(data_path, i)
            p_val=calculate_yield_p_val(df,start,end)
            p_val_list.append((i, j, p_val))
        #print(p_val_list)
        sorted_p_val1 = sorted(p_val_list, key=lambda x: x[2])
        h1_list = sorted_p_val1[:30]
        print(h1_list)
        print('평균 수익률에 대한 가설검정 실시 완료')
    else :
        print('평균 수익률에 대한 가설검정을 하지 않습니다.')

    if diff_hypothesis_test == True:
        p_val_list = []
        for i,j in KS200_list:
            df1 = read_csv(data_path, KS200_jisu_name)
            df2 = read_csv(data_path, i)
            p_val=calculate_diff_p_val(df1,df2,start,end)
            p_val_list.append((i, j, p_val))
        #print(p_val_list)
        sorted_p_val2 = sorted(p_val_list, key=lambda x: x[2])
        h2_list = sorted_p_val2[:30]
        print(h2_list)
        print('해당 회사의 주식 평균 수익률이 KOSPI200의 평균 수익률과 다른지 에 대한 가설검정 실시 완료')
    else :
        print('해당 회사의 주식 평균 수익률이 KOSPI200의 평균 수익률과 다른지 에 대한 가설검정 실시하지 않습니다.')

if __name__ == "__main__":
    stock_eval()

