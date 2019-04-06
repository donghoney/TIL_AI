import requests
from bs4 import BeautifulSoup
import re
import datetime
import json
import os
import pandas as pd
import multiprocessing
from multiprocessing import Pool
from readJson import readJson,writeExcel
import argparse

def crawl(keyword,i):
	url = 'https://search.shopping.naver.com/search/all.nhn?query={}&pagingSize=80&viewType=list&pagingIndex={}&sort=rel&cat_id=&frm=NVSHPAG'.format(keyword,i)
	data = requests.get(url)
	print(data.status_code,url)
	return data.content


def getProductInfo(li):
	img = li.find('img')
	nvMid=li['data-expose-id']
	alt = img['alt']
	tit = li.find('a',{'class':'tit'})
	href = tit['href']
	info = li.find('div',{'class':'info'})
	price=info.find('span',{'class':'price'})
	priceReload = price.find('span',{'class':'_price_reload'})
	lowest_price = priceReload.text.replace(',','')
	btnCompare = price.find('a',{'class':'btn_compare'})
	numOfSellers=re.findall('\d+', btnCompare.text)[0]
	depth = info.find('span',{'class':'depth'})
	category = depth.select('a')
	category1 = category[0].text
	category2 = category[1].text
	category3 = category[2].text
	etc = info.find('span',{'class':'etc'})
	em = etc.select('em')
	numOfReviews=em[0].text.replace(',','')
	#keepCount = li.find('em',{'nvmid':nvMid})
	#print(keepCount)
	first_date = '/'.join(re.findall('\d+',etc.select('span.date')[0].text))
	graph = etc.find('span',{'class':'star_graph'})
	star = float(re.findall('\d+',graph.select('span')[0]['style'])[0])/100


	return {'first_date':first_date,
			'numOfReviews':numOfReviews,
			'lowestPrice': lowest_price,
			'numOfSellers':numOfSellers,
			'cat1': category1,
			'cat2': category2,
			'cat3': category3,
			'href': href,
			'name': alt,
			'star':star,
			'nvMid': nvMid }


def parse(htmlDoc):
	result = BeautifulSoup(htmlDoc,'html.parser')
	ul = result.find('ul',{'class':'goods_list'})
	lis = ul.findAll('li',{'class':'_model_list _itemSection'})

	products =[]
	for li in lis:
		product = getProductInfo(li)
		if product:
			products.append(product)

	return products

def multiprocessing_crawl(i):
	htmlDoc = crawl(keyword,i)
	products = parse(htmlDoc)
	#print('num of products : ',len(products))
	#print(products)
	return products

def getReviewIndex(nvMid):
	url = 'https://search.shopping.naver.com/detail/review_list.nhn'
	header = {
		'nvMid': nvMid,
		'page': 1,
		'reviewSort': 'accuracy',
		'reviewType': 'all',
		'ligh': 'true'
	}
	data = requests.post(url, data=header)
	result = BeautifulSoup(data.content, 'html.parser')
	reviewPaging = result.find('div',{'class':'co_paginate'})
	try:
		a = reviewPaging.findAll('a')
		endPage = re.findall('\d+',a[-1]['onclick'])[0]
	except:
		endPage = 1

	print(endPage)
	return endPage

def reviewCrawl(i):
	url = 'https://search.shopping.naver.com/detail/review_list.nhn'

	header = {
		'nvMid':current_nvMid,
		'page':i,
		'reviewSort':'accuracy',
		'reviewType':'all',
		'ligh':'true'
	}
	data = requests.post(url,data=header)
	print(data.status_code,url)
	return data.content
def getReviewInfo(atcArea):
	star=atcArea.select('span.curr_avg')[0].text
	date=atcArea.select('span.date')[0].text.replace('.','/')[:-1]
	subject = atcArea.select('p')[0].text
	atc = atcArea.select('div.atc')[0].text

	return {'star':star,
			'date':date,
			'subject':subject,
			'atc':atc }

def reviewParse(htmlDoc):
	result = BeautifulSoup(htmlDoc,'html.parser')
	ul = result.find('ul',{'class':'lst_review'})
	atcAreas = ul.findAll('div',{'class':'atc_area'})
	reviewsInfo =[]

	for atcArea in atcAreas:
		reviewInfo = getReviewInfo(atcArea)
		if reviewInfo:
			reviewsInfo.append(reviewInfo)

	return reviewsInfo
def multiprocessing_review_crawl(i):
	htmlDoc = reviewCrawl(i)
	reviewInfos = reviewParse(htmlDoc)
	return reviewInfos

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('--k',type=str,default='설화수',
						help='what is the keyword for searching')
	args = parser.parse_args()

	global keyword
	keyword = args.k

	itemListCrawling = True
	reviewCrawling = True
	workers = 4

	# itemListCrawling : 검색 -> 아이템 리스트 크롤링
	# reviewCrawling : 아이템 리스트가 저장되어있는 json파일을 읽어서
	# 해당 url을 크롤링하여 각 id별 리뷰데이터를 크롤링

	if itemListCrawling :
		index = 20   # 80 * index 의 개수만큼 search
		path1 = './{}.json'.format(keyword)
		total_products = []

		num_list= [i for i in range(1,index+1)]
		with Pool(processes=workers) as pool:
			products=pool.map(multiprocessing_crawl,num_list)
			#print(len(products))
			for product in products :
				total_products+=product

		file = open(path1,'w+')
		file.write(json.dumps(total_products))
		file.close()

	if reviewCrawling :
		df = readJson(keyword)
		nvMids = list(df['nvMid'])
		global current_nvMid

		for nvMid in nvMids:
			total_reviews = []
			path2 = './{}.json'.format(nvMid)
			print(path2)
			current_nvMid=nvMid
			reviewIndex=int(getReviewIndex(current_nvMid))
			review_index_list = [i for i in range(1,reviewIndex+1)]
			with Pool(processes=workers) as pool:
				reviewInfos=pool.map(multiprocessing_review_crawl,review_index_list)
				for reviewInfo in reviewInfos:
					total_reviews+=reviewInfo

			print(total_reviews)
			file = open(path2,'w+')
			file.write(json.dumps(total_reviews))
			file.close()
			df=readJson(nvMid)
			writeExcel(df,nvMid)

if __name__=='__main__':
	main()


