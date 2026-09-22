import requests
from bs4 import BeautifulSoup
import os

url = "https://www.melon.com/chart/index.htm"
headers = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36 Edg/153.0.0.0"}
res = requests.get(url,headers=headers)
res.raise_for_status() # 에러시 종료

soup = BeautifulSoup(res.text,"lxml")
print("-"*60)


# with open("melon2.html","w",encoding="utf-8") as f:
#     f.write(soup.prettify()) # 이쁘게 저장됨


# with open("melon3.html","w",encoding="utf-8") as f:
#     f.write(res.text)

print("-"*60)
#1개 들고 올때는 find 여러개는 find_all
s_tbody = soup.tbody
# print(s_tbody)
trs = s_tbody.find_all("tr")
# print(len(trs))
# for tr in trs:
for i,tr in enumerate(trs):
    tds = tr.find_all("td")
    try:
        #img 정보를 가지고 호출을 다시해야함 - img의 정보파일을 가져옴.
        os.makedirs("./melon_img", exist_ok=True)
        imgs = tds[3].find("img")["src"] #[]-1개,attrs-여러개4
        img_res = requests.get(imgs,headers=headers) 
        with open(f"melon1_2026_{i+1}.jpg","wb")as f:
            f.write(img_res.content)

        ranks = tds[1].find("span",{"class":"rank"}).get_text()
        names = tds[5].find_all("a")
        name1 = (names[0].get_text())
        name2 = (names[1].get_text())
        song = tds[6].find("a")["title"]

    except Exception as e:
        print("오류 발생:", e)
    print(f"{ranks}위\n{imgs}\n{name1}\n{name2}")


# print("완료")




