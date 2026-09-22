from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
import time
import os

# 2.selenium 파일저장
# browser = webdriver.Chrome()
# url = "https://stock.naver.com/market/stock/kr"
# browser.get(url)
# time.sleep(3)
# soup = BeautifulSoup(browser.page_source,'lxml')
# with open('naver.html','w',encoding='utf-8') as f:
#     f.write(soup.prettify())



with open("naver.html","r",encoding="utf-8") as f:
    soup = BeautifulSoup(f,'lxml')

s_tbody = soup.tbody
trs = s_tbody.find_all("tr")
tds = trs[0].find_all("td")
rank = tds[0].find("span",{"class":"index"}).get_text(strip=True)
name = tds[0].find("span",{"class":"SingleLineText_text__HI_cb"}).get_text(strip=True)
t_val = tds[1].find("span",{"class":"SingleLinePrice_price__g_6VV"}).get_text(strip=True)
print(f"{rank}/{name}/{t_val}")