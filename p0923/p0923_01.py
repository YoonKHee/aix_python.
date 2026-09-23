from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
import time
import os

# 2. selenium : 자동화 도구
# browser = webdriver.Chrome()
# url = "https://stock.naver.com/market/stock/kr/stocklist/priceTop"
# browser.get(url)
# time.sleep(3)
# soup = BeautifulSoup(browser.page_source,'lxml')
# with open('stock1.html','w',encoding='utf-8') as f:
#     f.write(soup.prettify())



# 1. requests
# 단점 : 자바스크립트로 구동되는 소스 가져올수 없다.
# requests정보가져오기 -> css문법변환 -> find,find_all()
# url = "https://www.melon.com/chart/index.htm"
# # User-Agent : Python-requests 정보
# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36'}
# res = requests.get(url,headers=headers)
# res.raise_for_status() #에러시 종료
# # css문법변환
# soup = BeautifulSoup(res.text,'lxml') #html소스 변경-css문법



# 파일 BeautifulSoup변환
with open('stock1.html','r',encoding='utf-8') as f:
    soup = BeautifulSoup(f,'lxml')


s_tbody = soup.tbody
trs = s_tbody.find_all("tr") # tr 제일 앞에꺼만 추출된
# trs = s_tbody.find_all("tr") # tr전부
s_headTitle = []
s_tr = soup.thead.tr
s_ths = s_tr.find_all("th")
for th in s_ths:
    s_headTitle.append(th.get_text(strip=True))

print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*s_headTitle))
for tr in trs:
    tds = tr.find_all("td")
    rank = tds[0].find("span",{"class":"index"}).get_text(strip=True)
    s_title = tds[0].find("span",{"class":"SingleLineText_text__HI_cb"}).get_text(strip=True)
    s_val = tds[1].find("span",{"class":"SingleLinePrice_price__g_6VV"}).get_text(strip=True)
    c_val = tds[2].find("span",{"class":"ModulePriceChange_amount__4QYMz"}).get_text(strip=True)
    get = tds[3].find("span",{"class":"SingleLinePrice_single-line-price__bnpQv SingleLinePrice_medium__QoN_F"}).get_text(strip=True)
    money = tds[4].find("span",{"class":"SingleLinePrice_single-line-price__bnpQv SingleLinePrice_medium__QoN_F"}).get_text(strip=True)
    max = tds[5].find("span",{"class":"SingleLinePrice_single-line-price__bnpQv SingleLinePrice_medium__QoN_F"}).get_text(strip=True)
    min = tds[6].find("span",{"class":"SingleLinePrice_single-line-price__bnpQv SingleLinePrice_medium__QoN_F"}).get_text(strip=True)
    all_val = tds[7].find("span",{"class":"SingleLineText_text__HI_cb"}).get_text(strip=True)
    print(f"{rank}\t{s_title}\t{s_val}\t{c_val}\t{get}\t{money}\t{max}원\t{min}원\t{all_val}")
    print("-"*100)
