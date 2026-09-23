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
for i,tr in enumerate(trs):
    try:
        tds = tr.find_all("td")
        rank = tds[0].find("span",{"class":"index"}).get_text(strip=True)
        name = tds[0].find("span",{"class":"SingleLineText_text__HI_cb"}).get_text(strip=True)
        t_val = tds[1].find("span",{"class":"SingleLinePrice_price__g_6VV"}).get_text(strip=True)
        update = tds[2].find("span",{"class":"ModulePriceChange_amount__4QYMz"}).get_text(strip=True)
        update2 = tds[2].find("span",{"class":"ModulePercent_module-percent__zioL9 ModulePercent_medium__OThzX ModulePercent_down__IhNnh"}).get_text(strip=True)
        money1 = tds[3].find("span",{"class":"SingleLinePrice_single-line-price__bnpQv SingleLinePrice_medium__QoN_F"}).get_text(strip=True)
        money2 = tds[4].find("span",{"class":"SingleLinePrice_single-line-price__bnpQv SingleLinePrice_medium__QoN_F"}).get_text(strip=True)
        max = tds[5].find("span",{"class":"SingleLinePrice_price__g_6VV"}).get_text(strip=True)
        min = tds[6].find("span",{"class":"SingleLinePrice_price__g_6VV"}).get_text(strip=True)
        all = tds[7].find("span",{"class":"SingleLineText_text__HI_cb"}).get_text(strip=True)
        print(f"{rank}/{name}/{t_val}/{update}{update2}/{money1}/{money2}/{max}/{min}/{all}")
    except Exception as e:
            print("오류 발생:", e)    