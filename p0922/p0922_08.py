import requests
from bs4 import BeautifulSoup

url = "https://www.melon.com/chart/index.htm"
headers = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36 Edg/153.0.0.0"}
res = requests.get(url,headers=headers)
res.raise_for_status() # 에러시 종료

soup = BeautifulSoup(res.text,"lxml")
print("-"*60)

s_tbody = soup.tbody

trs = s_tbody.find_all("tr",{"class":"lst50"})
for i in range(50):
    tds = trs[i].find_all("td")
    inputs = tds[0].find("input")["title"]
    rank = tds[1].find("span",{"class":"rank"}).text
    s_name = tds[5].find("a")["title"]
    name = tds[5].find("a",{"class":"ellipsis rank02"})["title"]
    imgs = tds[3].find("img")["src"]
    print(f"{rank}위 {inputs},{imgs} 곡정보:{s_name},{name}")