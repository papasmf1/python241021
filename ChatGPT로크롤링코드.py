import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

# 검색 결과 페이지 URL
url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%B0%98%EB%8F%84%EC%B2%B4"

# 헤더 설정 (User-Agent를 지정해줘야 크롤링이 차단되지 않을 수 있음)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

# 페이지 요청
response = requests.get(url, headers=headers)

# HTML 파싱
soup = BeautifulSoup(response.text, 'html.parser')

# 신문기사 제목 크롤링 (제목이 들어가는 CSS 클래스 찾기)
titles = soup.select('a.news_tit')

# 엑셀 파일 생성
wb = Workbook()
ws = wb.active
ws.title = "News Titles"

# 헤더 추가
ws.append(["No.", "Title"])

# 제목을 엑셀 파일에 기록
for idx, title in enumerate(titles, start=1):
    ws.append([idx, title.get_text()])

# 엑셀 파일 저장
wb.save("results.xlsx")

print("크롤링한 결과를 results.xlsx 파일로 저장했습니다.")
