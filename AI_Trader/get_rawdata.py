import FinanceDataReader as fdr
print(fdr.__version__)

#  차트 설정
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import csv
import os
import re
import requests

def read_csv(path,code):
    file_list=os.listdir(path)
    for i in file_list:
        if code in i:
            print('opened  :',i)
            return pd.read_csv(os.path.join(path,i))

def read_KS200_symbol(path,name):
    temp_for_sort = []
    file_path = os.path.join(path, name)
    data_list=[]
    with open(file_path, 'r', encoding='ms949') as in_file:
        for sort_line in in_file:
            sort_line=sort_line.strip('\n')
            data=sort_line.split(',')
            data_list.append(data)

    return data_list

def write_KS200_symbol(path,name):
    BaseUrl = 'http://finance.naver.com/sise/entryJongmok.nhn?&page='
    #print(path,name)
    file_path = os.path.join(path,name)
    data_list = []


    ## delete only if file exists ##
    if os.path.exists(file_path):
        os.remove(file_path)
    else:
        print('Sorry, I can not remove {} file.'.format(file_path))

    for i in range(1,22,1):
        try:
            url = BaseUrl + str(i)
            #print(url)
            res = requests.get(url)
            tag = BeautifulSoup(res.content,'html.parser')
            items = tag.find_all('td',{'class':'ctg'})

            for item in items:
                #print(item)
                txt = item.a.get('href')
                k = re.search('[\d]+',txt)
                #print(k.group())
                if k:
                    code = k.group()
                    name = item.text
                    data = code, name
                    data_list.append(data)
                    with open(file_path,'a',encoding='ms949') as f:
                        #print('open okay')
                        writer=csv.writer(f)
                        writer.writerow(data)

        except:
            print('except')
            pass
        finally:
            temp_for_sort = []
            with open(file_path,'r',encoding='ms949') as in_file:
                for sort_line in in_file:
                    temp_for_sort.append(sort_line)
            with open(file_path,'w',encoding='ms949') as out_file:
                seen = set() # set for fast 0(1) amortized lookup
                for line in temp_for_sort:
                    if line in seen: continue

                    seen.add(line)
                    out_file.write(line)
    return data_list
def crop_list(list,start,end):
   return list[start:end]

def write_Ticker(path,start_date,end_date,code,name):

    df = fdr.DataReader(code,start_date,end_date)
    df.to_csv(os.path.join(path,'{0}{1}_{2}_{3}.csv'.format(name,code,start_date,end_date)),encoding='ms949',index=True)


def main():
    data_path = './data'
    KS200_name = 'KOSPI200.csv'
    KS200_symbol_update = False  # KOSPI200 종목코드,이름을 저장한 csv가 없을 경우 True
    KS200_rawchart_download = False #KOSPI200 csv를 통해 지정한 날짜로 주가 데이터 크롤링한다. 주가 데이터 csv가 없을 경우, True
    KS200_jisu = False  # KOSPI 200 지수 데이터 크롤링
    if KS200_symbol_update == True:
        KS200_list=write_KS200_symbol(data_path,KS200_name)
        print('KOSPI 200 종목 리스트를 업데이트 합니다.')
    else :
        KS200_list=read_KS200_symbol(data_path,KS200_name)
        print('KOSPI 200 종목 리스트를 업데이트 하지 않습니다.')
    print(len(KS200_list))

    if KS200_rawchart_download == True:
        # 종목 코드, 종목 이름으로 구성된 리스트 슬라이싱하기
        #cropped_list=crop_list(KS200_list,0,3)

        #주식데이터를 csv로 저장하기 가져올 날짜와 잘라낸 종목 리스트를 write_Ticker 함수로 저장할 수 있다.
        start_date = '2015-01-01'
        end_date = '2019-01-26'
        print('Select Crawl data {0} to {1}'.format(start_date,end_date))
        for i in KS200_list:
             code = i[0]
             name = i[1]
             write_Ticker(data_path,start_date,end_date,code,name)
        print('KOSPI 200 종목 각각의 주식 데이터를 크롤링 합니다.')

    else :
        print('KOSPI 200 종목 각각의 주식 데이터를 크롤링하지 않습니다.')
        pass
    if KS200_jisu == True:
        # 코스피 200 지수 다운로드하기
        df_krx = fdr.DataReader('KS200','2015')
        df_krx.to_csv('./data/KS200_jisu.csv', encoding='ms949',index=True)
        print('KOSPI 200 지수를 업데이트 합니다.')
    else :
        print('KOSPI 200 지수를 업데이트 하지 않습니다.')
    df = read_csv(data_path, KS200_list[1][0])
    print(df.describe())


if __name__ == "__main__":
    main()




## 그래프 설정
plt.rcParams["font.family"] = 'nanummyeongjo'
plt.rcParams["figure.figsize"] = (14,4)
plt.rcParams['lines.linewidth'] = 3
plt.rcParams["axes.grid"] = True



# KS200 지수 다운로드
#df_KS200 = fdr.StockListing('KOSDAQ')
#df_KS200.to_csv('./data/KOSDAQ_List.csv',encoding='ms949',index=False)

