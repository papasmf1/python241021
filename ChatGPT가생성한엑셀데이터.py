import openpyxl
import random

# 제품명 리스트 생성
제품명_리스트 = [
    "스마트폰", "노트북", "태블릿", "스마트워치", "이어폰", "블루투스 스피커",
    "게이밍 마우스", "기계식 키보드", "모니터", "프린터", "외장하드", "공유기"
]

# 새 워크북 생성
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "전자제품 판매 데이터"

# 헤더 추가
ws.append(["제품ID", "제품명", "수량", "가격"])

# 100개의 데이터 생성 및 추가
for i in range(1, 101):
    제품ID = f"P{i:03d}"
    제품명 = random.choice(제품명_리스트)
    수량 = random.randint(1, 100)
    가격 = random.randint(10000, 2000000)
    
    ws.append([제품ID, 제품명, 수량, 가격])

# 파일 저장
wb.save("products.xlsx")

print("products.xlsx 파일이 생성되었습니다.")