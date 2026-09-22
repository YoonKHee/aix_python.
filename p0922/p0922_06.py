import requests
from bs4 import BeautifulSoup

url = "https://www.daum.net/"
headers = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36 Edg/153.0.0.0"}
res = requests.get(url,headers=headers)
res.raise_for_status() # 에러시 종료

soup = BeautifulSoup(res.text,"lxml")
print("-"*60)
print(soup.title.get_text)
# print(soup.find("a",{"class":"w5hRs"}).get_text)
# print(soup.find("a",{"class":"gb_6"}).get_text)
print(soup.find("h2",{"class":"screen_out"}))