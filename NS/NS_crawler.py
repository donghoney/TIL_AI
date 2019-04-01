import requests
from bs4 import BeautifulSoup
import re
import datetime

def get_list_data(base_url,s_page=1,e_page=,paggingSize=40,viewType='list',sort='rel',cat_id,frm=NVSHCAT):
	base_url = base_url
	pagin
res = requests.get(url)
result = BeautifulSoup(res.content,'html.parser')
tag = result.select('div.star_t1 > a > ...')
payloads={
'pagingIndex': '1',
'pagingSize': '40',
'viewType': 'list',
'sort': 'rel',
'cat_id': '50000437',
'frm': 'NVSHCAT'
}

#res = requests.post(url,data=payloads).json()
