from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup
import time
import os
from dotenv import load_dotenv


# 1. requests
# 단점 : 자바스크립트로 구동되는 소스 가져올수 없다.
# requests정보가져오기 -> css문법변환 -> find,find_all()
# url = "https://nol.yanolja.com/?utm_source=google_sa&utm_medium=cpc&utm_campaign=20738115572&utm_content=160897187931&utm_term=kwd-324456684700&gad_source=1&gad_campaignid=20738115572&gbraid=0AAAAAoeYBbk9_49lb5ym46MScFFqBlFPA&gclid=EAIaIQobChMI5v3ukIuQlwMVpKZmAh31xQ9nEAAYASAAEgLLSPD_BwE"
# # User-Agent : Python-requests 정보
# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36'}
# res = requests.get(url,headers=headers)
# res.raise_for_status() #에러시 종료
# # css문법변환
# soup = BeautifulSoup(res.text,'lxml') #html소스 변경-css문법



# 2. selenium : 자동화 도구
# browser = webdriver.Chrome()
# url = "https://nol.yanolja.com/discovery/list/PRODUCT_CATEGORY_KOREA_ACCOMMODATION/HOTEL/900584"
# browser.get(url)
# time.sleep(3)
# soup = BeautifulSoup(browser.page_source,'lxml')
# with open('p0928/file/ya1.html','w',encoding='utf-8') as f:
#     f.write(soup.prettify())


# options = Options()
# url = "https://nol.yanolja.com/discovery/list/PRODUCT_CATEGORY_KOREA_ACCOMMODATION/HOTEL/900584"
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option("useAutomationExtension", False)
# options.add_argument("--disable-blink-features=AutomationControlled")
# browser = webdriver.Chrome(options=options)
# browser.maximize_window() # 화면 최대창 확대
# browser.get(url)
# time.sleep(2)


# 2-1. selenium : 자동화 구현
# 상단 제어창문구 삭제
options = Options()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
options.add_argument("--disable-blink-features=AutomationControlled")
browser = webdriver.Chrome(options=options)
browser.maximize_window() # 화면 최대창 확대
url = "https://www.yeogi.com/domestic-accommodations?keyword=%EC%A0%9C%EC%A3%BC+&checkIn=2026-09-28&checkOut=2026-09-29&personal=2&typoCorrect=true&nonAffiliated=true"
browser.get(url)

# 자바스크립트를 통해 브라우저 높이 가져오기
pre_height = browser.execute_script('return document.body.scrollHeight')
print("처음 높이 : ",pre_height)

while True:
    # 스크롤 내리기
    browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(3) # 내용추가하는데 시간대기

    # 다시 높이 가져오기
    next_height = browser.execute_script('return document.body.scrollHeight')
    print('변경된 높이 : ',next_height)

    if pre_height==next_height: break
    else : pre_height = next_height

soup = BeautifulSoup(browser.page_source,'lxml')
with open('p0928/file/ya1.html','w',encoding='utf-8') as f:
    f.write(soup.prettify())

print('더 이상 높이 변경이 없음')




# with open("p0928/file/ya1.html","r",encoding="utf-8") as f:
#     soup = BeautifulSoup(f,'lxml')

# items = soup.find("div",{"data-testid":"virtuoso-item-list"})
# print(items)
# item = items.find("dib",{"data-known-size":"228"})
