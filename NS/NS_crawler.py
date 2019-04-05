import requests
from bs4 import BeautifulSoup
import re
import datetime
import json

def crawl(keyword):
	url = 'https://search.shopping.naver.com/search/all.nhn?query={}&cat_id=&frm=NVSHATC'.format(keyword)
	data = requests.get(url)
	print(data.status_code,url)
	return data.content

def getProductInfo(li):
	img = li.find('img')
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
	keepCount = etc.find('em',{'class':'_keepCount'})
	print(keepCount)
	first_date = '/'.join(re.findall('\d+',etc.select('span.date')[0].text))
	graph = etc.find('span',{'class':'star_graph'})
	star = float(re.findall('\d+',graph.select('span')[0]['style'])[0])/100


	return {'first_date':first_date,'name': alt,'star':star, 'numOfReviews':numOfReviews,'lowest_price': lowest_price,'numOfSellers':numOfSellers, 'cat1': category1, 'cat2': category2, 'cat3': category3, 'href': href}



def parse(htmlDoc):
	result = BeautifulSoup(htmlDoc,'html.parser')
	ul = result.find('ul',{'class':'goods_list'})
	lis = ul.findAll('li',{'class':'_model_list _itemSection'})

	products =[]
	for li in lis:
		product = getProductInfo(li)
		products.append(product)

	return products

keyword = '설화수'
htmlDoc = crawl(keyword)
products = parse(htmlDoc)
print('num of products : ',len(products))
print(products)

file = open('./{}_products.json'.format(keyword),'w+')
file.write(json.dumps(products))


