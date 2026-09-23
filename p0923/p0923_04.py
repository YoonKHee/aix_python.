from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup
import time
import os
from dotenv import load_dotenv

# # 2. selenium : 자동화 구현
# # 상단 제어창문구 삭제
# options = Options()
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option("useAutomationExtension", False)
# options.add_argument("--disable-blink-features=AutomationControlled")
# browser = webdriver.Chrome(options=options)
# browser.maximize_window() # 화면 최대창 확대
# url = "https://www.yeogi.com/domestic-accommodations?keyword=%EA%B2%BD%EC%A3%BC&autoKeyword=%EA%B2%BD%EB%B6%81+%EA%B2%BD%EC%A3%BC%EC%8B%9C&checkIn=2026-09-23&checkOut=2026-09-24&personal=2"
# browser.get(url)

# # 자바스크립트를 통해 브라우저 높이 가져오기
# pre_height = browser.execute_script('return document.body.scrollHeight')
# print("처음 높이 : ",pre_height)

# while True:
#     # 스크롤 내리기
#     browser.execute_script('window.scroll(0,document.body.scrollHeight)')
#     time.sleep(3) # 내용추가하는데 시간대기

#     # 다시 높이 가져오기
#     next_height = browser.execute_script('return document.body.scrollHeight')
#     print('변경된 높이 : ',next_height)

#     if pre_height==next_height: break
#     else : pre_height = next_height

# soup = BeautifulSoup(browser.page_source,'lxml')
# with open('travle.html','w',encoding='utf-8') as f:
#     f.write(soup.prettify())

# print('더 이상 높이 변경이 없음')
# input()



# 파일저장해서 저장한 파일을 가지고 정보를 가져오기
# 사진 이름 별점 평가 가격

with open("travle.html","r",encoding="utf-8") as f:
    soup = BeautifulSoup(f,'lxml')

uls = soup.find("ul",{"class":"css-y5z6rw"})
lis = uls.find_all("li")

for i in range(len(lis)):
    try:
        t_img = lis[i].find("div",{"class":"css-28vbuw"}).find("img")["src"]
        t_name = lis[i].find("h3",{"class":"gc-thumbnail-type-seller-card-title css-1gsfgy5"}).get_text(strip=True)
        t_avg = lis[i].find("span",{"class":"css-ry30z7"}).get_text(strip=True)
        t_avg = float(t_avg)
        t_eva = lis[i].find("span",{"class":"css-144z61f"}).get_text(strip=True)
        t_eva = int(t_eva[:-4].replace(",",""))
        t_val = lis[i].find("span",{"class":"css-1llao6q"}).get_text(strip=True)
        t_val = int(t_val.replace(",",""))
        print(f"사진:{t_img}\n이름:{t_name}\n평점:{t_avg}\n평가수:{t_eva}\n가격:{t_val}")
        print("-"*30)
    except Exception as e:
        pass

