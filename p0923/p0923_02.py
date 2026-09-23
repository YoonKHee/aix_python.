from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
import time
import os

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36'}
# 2. selenium : 자동화 도구
# browser = webdriver.Chrome()
# url = "https://comic.naver.com/bestChallenge?sortType=starscore"
# browser.get(url)
# time.sleep(3)
# soup = BeautifulSoup(browser.page_source,'lxml')
# with open('webtoon.html','w',encoding='utf-8') as f:
#     f.write(soup.prettify())


# 파일 BeautifulSoup변환
with open('webtoon.html','r',encoding='utf-8') as f:
    soup = BeautifulSoup(f,'lxml')


uls = soup.find("ul",{"class":"BestChallengeView__challenge_list--sUqhh"})
lis = uls.find_all("li")
avgs = []
sees = []
for i in range(3):
    s_img = lis[i].find("img")["src"]
    s_name = lis[i].find("span",{"class":"ContentTitle__title--e3qXt"}).get_text(strip=True)
    s_name2 = lis[i].find("a",{"class":"ContentAuthor__author--CTAAP"}).get_text(strip=True)
    avg = lis[i].find("span",{"class":"Rating__star_area--dFzsb"}).find("span", {"class":"text"}).get_text(strip=True)
    avg = float(avg.replace(",", ""))
    avgs.append(avg)
    see = lis[i].find("span",{"class":"Rating__view_area--GQb_S"}).find("span", {"class":"text"})
    see = int((see.get_text(strip=True)[:-1]).replace(",",""))
    sees.append(see)
    # see = int(see)
    print(f"{s_img}\t{s_name}\t{s_name2}\t{avg}\t{see}")
print(f"평점평균:{sum(avgs)/len(avgs)}")
print(f"조회수평균:{(sum(sees)/len(sees)):.2f}만")


    # # 이미지 저장
    # img_res = requests.get(s_img,headers=headers)
    # # 폴더생성
    # os.makedirs("./p0923/webtoon",exist_ok=True)
    # count = 1
    # with open(f"./p0923/webtoon/webtoon_{count}.jpg","wb") as f:
    #     f.write(img_res.content)

# print("완료")