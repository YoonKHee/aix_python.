from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup
import time
import os
from dotenv import load_dotenv


# # .env파일 읽어와서 변수값 입력.
# load_dotenv()
# id = os.getenv("id")
# # id = "admin" # 프로그램에 노출됨.
# print(id)



# 1. requests
# 단점 : 자바스크립트로 구동되는 소스 가져올수 없다.
# requests정보가져오기 -> css문법변환 -> find,find_all()
# url = "https://flight.naver.com/flights/domestic/SEL:city-CJU:airport-20261006/CJU:airport-SEL:city-20261008?adult=1&fareType=YC"
# User-Agent : Python-requests 정보
# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36'}
# res = requests.get(url,headers=headers)
# res.raise_for_status() #에러시 종료
# # css문법변환
# soup = BeautifulSoup(res.text,'lxml') #html소스 변경-css문법


# with open('p0928/file/ya1.html','w',encoding='utf-8') as f:
#     f.write(soup.prettify())

# f_div = soup.find("div",{"flights List domestic_DomesticFlight__N2IQ_"}).find("div",{"class":"domestic_inner__8geIy"}).find("div",{"class":"domestic_results__gp5WB"})
# print(f_div)

# # 2-1. selenium : 자동화 구현
# # 상단 제어창문구 삭제
# options = Options()
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option("useAutomationExtension", False)
# options.add_argument("--disable-blink-features=AutomationControlled")
# browser = webdriver.Chrome(options=options)
# browser.maximize_window() # 화면 최대창 확대
# url = "https://flight.naver.com/flights/domestic/SEL:city-CJU:airport-20261006/CJU:airport-SEL:city-20261008?adult=1&fareType=YC"
# browser.get(url)

# # 자바스크립트를 통해 브라우저 높이 가져오기
# pre_height = browser.execute_script('return document.body.scrollHeight')
# print("처음 높이 : ",pre_height)

# while True:
#     # 스크롤 내리기
#     browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
#     time.sleep(3) # 내용추가하는데 시간대기

#     # 다시 높이 가져오기
#     next_height = browser.execute_script('return document.body.scrollHeight')
#     print('변경된 높이 : ',next_height)

#     if pre_height==next_height: break
#     else : pre_height = next_height

# soup = BeautifulSoup(browser.page_source,'lxml')
# with open('p0928/file/flight2.html','w',encoding='utf-8') as f:
#     f.write(soup.prettify())

# print('더 이상 높이 변경이 없음')



# with open("p0928/file/flight2.html","r",encoding="utf-8") as f:
#     soup = BeautifulSoup(f,'lxml')

# flights = soup.find_all("div",{"class":"domestic_Flight__8bR_b"})

# # flight = soup.find("div",{"class":"domestic_Flight__8bR_b"}).find("i",{"class":"domestic_num__ShOub"})
# # print(flight)

# # 7만원 이하에 있는 비행기 표를 출력.
# for i in range(len(flights)):
#     cost = flights[i].find("i",{"class":"domestic_num__ShOub"}).get_text(strip=True)
#     cost = int(cost.replace(",",""))
#     if cost <= 70000:
#         name = flights[i].find("b",{"class","airline_name__0Tw5w"}).get_text(strip=True)
#         routes = flights[i].find_all("span",{"class","route_airport__tBD9o"})
#         start = routes[0].get_text(strip=True)
#         end = routes[1].get_text(strip=True)

        
        # result = flights[i].find("b",{"class","airline_name__0Tw5w"}).get_text(strip=True)
        # print(f"{name}\t{start}\t{end}\t{cost}")







with open("p0928/file/yeo1.html","r",encoding="utf-8") as f:
    soup = BeautifulSoup(f,'lxml')

ul = soup.find("ul",{"class":"css-y5z6rw"})
lis = ul.find_all("li")

# img = lis[0].find("img")["src"]
# print(img)

for i in range(len(lis)):
    try:
        cost = lis[i].find("span",{"class":"css-1llao6q"}).get_text(strip=True)
        cost = int(cost.replace(",",""))
        avg = lis[i].find("span",{"class":"css-ry30z7"}).get_text(strip=True)
        avg = float(avg)
        if cost >= 200000 and avg >9.5:
            os.makedirs("p0928/imgs", exist_ok=True)
            imgs = lis[i].find("img")["src"] #[]-1개,attrs-여러개4
            img_res = requests.get(imgs)
            with open(f"p0928/imgs/hotel{i+1}.jpg", "wb") as f:
                f.write(img_res.content)
            name = lis[i].find("h3",{"class":"gc-thumbnail-type-seller-card-title css-1gsfgy5"}).get_text(strip=True)
            print(f"{name}\t{cost}원\t{avg}")
    except Exception as e:
            pass 
    



