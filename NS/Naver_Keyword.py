# coding=utf-8

from selenium import webdriver
import os

browser = webdriver.Chrome('/Users/Donghoon/Github/TIL_AI/NS/chromedriver')

browser.implicitly_wait(10)
browser.get('http://www.naver.com')
login_bt = browser.find_element_by_class_name('lg_local_btn')
login_bt.click()

#browser.implicitly_wait(10)
naver_id = 'glee1228'
naver_password=os.environ['LOGNAME']+str(int(os.environ['XPC_SERVICE_NAME'][-4:])+137)

# ID를 입력한다
id = browser.find_element_by_id('id')
id.send_keys(naver_id)


browser.implicitly_wait(10)

#PWD를 입력 한다
id = browser.find_element_by_id('pw')
id.send_keys(naver_password)
#print(naver_id)
#print(naver_password)

browser.implicitly_wait(10)

naver_submit = browser.find_element_by_class_name('btn_global')
naver_submit.click()
