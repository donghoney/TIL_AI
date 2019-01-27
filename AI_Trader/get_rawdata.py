import FinanceDataReader as fdr
print(fdr.__version__)

#  차트 설정
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

plt.rcParams["font.family"] = 'nanummyeongjo'
plt.rcParams["figure.figsize"] = (14,4)
plt.rcParams['lines.linewidth'] = 3
plt.rcParams["axes.grid"] = True

# 한국 거래소 상장종목 전체
#df_krx = fdr.StockListing('KRX')
#print('한국 거래소 상장종목')
#print(df_krx.columns)
#print(df_krx.loc[:,'Symbol':'Sector'].head(100))
#print(df_krx.head(50))
#print(len(df_krx))
#df_krx_csv=df_krx.to_csv('./data/df_krx.csv', encoding='ms949',index=False)
df_KS200 = fdr.StockListing('KOSDAQ')
df_KS200.to_csv('./data/KOSDAQ_List.csv',encoding='ms949',index=False)
start_year = '2015'
end_year= '2018'
Symbols=[]
def KS200_download_csv(start_year,end_year,Symbols):

    for i in range(start_year,end_year):
        for j in range(Symbols):
            df = fdr.DataReader(j,i)
            df.tocsv('./data/{0}_{1}.csv'.format(j,i),encoding='ms949',index=True)

# df_ks200_2018 = fdr.DataReader('KS200','2018')
# print('Kospi 200 지수 - 2018')
# print(df_ks200_2018.describe())
# df_ks200_2018.to_csv('./data/df_ks200_2018.csv',encoding='ms949',index=False)
#
# df_ks200_2019 = fdr.DataReader('KS200','2019')
# df_ks200_2019.to_csv('./data/df_ks200_2019.csv',encoding='ms949',index=False)
# print('Kospi 200 지수 - 2019 ')
# print(df_ks200_2019.head(50))


#df['Open'].plot()
#df['Close'].plot()
#plt.show()