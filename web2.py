# web2.py 
#웹크롤링에 관련된 선언 
from bs4 import BeautifulSoup
#웹서버에 요청 
import requests


url = "https://www.daangn.com/fleamarket/"
response = requests.get(url)
#검색이 용이한 객체 생성
soup = BeautifulSoup(response.text, "html.parser")
#파일에 저장:기존 파일에 첨부
f = open("daangn.txt", "a+", encoding="utf-8")
posts = soup.find_all("div", attrs={"class":"card-desc"})
for post in posts:
    titleElem = post.find("h2", attrs={"class":"card-title"})
    priceElem = post.find("div", attrs={"class":"card-price"})
    regionElem = post.find("div", attrs={"class":"card-region-name"})
    title = titleElem.text.replace("\n", "").strip()
    price = priceElem.text.replace("\n","").strip()
    address = regionElem.text.replace("\n","").strip()
    #내부에 문자열 출력: f-string
    print(f"{title}, {price}, {address}")
    f.write(f"{title}, {price}, {address}\n")

f.close() 
# <div class="card-desc">
#       <h2 class="card-title">호박 고구마10k</h2>
#       <div class="card-price ">
#         9,000원
#       </div>
#       <div class="card-region-name">
#         서울 중랑구 면목동
#       </div>
