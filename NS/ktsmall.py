import requests
from bs4 import BeautifulSoup
import re
import datetime
import json
import os
import pandas as pd
import multiprocessing
from multiprocessing import Pool
import argparse
import pandas as pd

def readJson(name):
    try:
        path='./{}.json'.format(name)
        df = pd.read_json(path)
        return df
    except Exception as e:
        print('json파일을 읽을 수 없음',e)


def writeExcel(df,name):
    try:
        path = './{}.xlsx'.format(name)
        writer=pd.ExcelWriter(path)
        df.to_excel(writer,'sheet1')
        writer.save()
    except Exception as e:
        print('엑셀을 쓸수 없음',e)

def crawlCat():
	url = 'http://ktsmall.co.kr/main.do?mobYn=N'
	data = requests.get(url)
	print(data.status_code,url)
	return data.content

def getCategoryInfo(li):
	ctgrKind=li['data-ctgrkind']
	print(ctgrKind)
	secDepth = li.find('div',{'class':'secDepth'})
	ctgrid1_list=[]
	for sec in secDepth.findAll('li'):
		ctgrid1=sec.get('data-ctgrid1')
		ctgrid1_list.append(ctgrid1)
	#srchCtgrId = secDepth.findAll('li')[i]['data-ctgrid1']
	#print(srchCtgrId)

def parse(htmlDoc):
	result = BeautifulSoup(htmlDoc,'html.parser')
	gnb = result.find('div',{'class':'gnb'})
	lis=gnb.findAll('li')[1:]
	ctgr_list=[]
	hangul = re.compile('[^ ㄱ-ㅣ가-힣]+')
	for li in lis:
		ctgrkind = li.get('data-ctgrkind')
		ctgrid = li.get('data-ctgrid1')
		ctgrgrp= li.get('data-ctgrgrp')
		ctgrname=hangul.sub('',li.text.split()[0])
		ctgr_list.append({'ctgrid':ctgrid , 'ctgrkind':ctgrkind,'ctgrgrp':ctgrgrp,'ctgrname':ctgrname})

	return ctgr_list

def crawlItem(id):
	url = 'https://ktsmall.co.kr/product/list.do?prdtCd=&ctgrGrp=FRESH+FOOD&ctgrKind=00&ctgrId1=&ctgrId2=&srchCtgrId={}'.format(id)
	data = requests.get(url)
	print(data.status_code, url)
	return data.content

def parseItem(htmlDoc):
	result = BeautifulSoup(htmlDoc,'html.parser')
	print(result)

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('--k',type=str,default='ctgr',
						help='what is the keyword for searching')
	args = parser.parse_args()

	global keyword
	keyword = args.k

	categoryListCrawling = False
	itemListCrawling = True
	workers = 4

	# itemListCrawling : 검색 -> 아이템 리스트 크롤링
	# reviewCrawling : 아이템 리스트가 저장되어있는 json파일을 읽어서
	# 해당 url을 크롤링하여 각 id별 리뷰데이터를 크롤링

	if categoryListCrawling :
		path1 = './{}.json'.format(keyword)
		total_products = []
		htmlDoc=crawlCat()
		ctgr_list=parse(htmlDoc)

		file = open(path1,'w+')
		file.write(json.dumps(ctgr_list))
		file.close()

	if itemListCrawling :
		df=readJson(keyword)
		ctgrids=list(df['ctgrid'])
		total_products = []

		with Pool(processes=workers) as pool:
			htmlDocs=pool.map(crawlItem, ctgrids[:1])

		for htmlDoc in htmlDocs[:1]:
			parseItem(htmlDoc)






if __name__=='__main__':
	main()

