from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup
import time
import os
from dotenv import load_dotenv
import undetected_chromedriver as uc

#쿠팡 - 검색 노트북 200건 리스트를 출력
# 셀레니움 방지가 적용 해제하는 방법 찾아서
# 쿠팡 - 검색 노트북 리스트를 출력


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept-Language": "ko-KR,ko;q=0.9",
    "Referer": "https://www.coupang.com/",
}



# options = Options()
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option("useAutomationExtension", False)
# options.add_argument("--disable-blink-features=AutomationControlled")
url = "https://www.coupang.com/np/search?component=&q=%EB%85%B8%ED%8A%B8%EB%B6%81&traceId=muksk87c&channel=user"
options = uc.ChromeOptions()
options.add_argument("--no-first-run --no-service-autorun --password-store=basic")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36")
browser = webdriver.Chrome(options=options)
browser.maximize_window() # 화면 최대창 확대
browser.get(url)
time.sleep(3)
# 파일저장
soup = BeautifulSoup(browser.page_source,'lxml')
with open(f'p0928/file/coupang.html','w',encoding='utf-8') as f:
        f.write(soup.prettify())
print("완료")
