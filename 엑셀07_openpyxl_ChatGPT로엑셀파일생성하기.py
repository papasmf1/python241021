from openpyxl import Workbook

# 전자제품 판매 데이터 생성 (임의의 데이터)
products_data = [
    {"제품ID": 1, "제품명": "스마트폰", "수량": 50, "가격": 1000000},
    {"제품ID": 2, "제품명": "노트북", "수량": 30, "가격": 1500000},
    {"제품ID": 3, "제품명": "태블릿", "수량": 20, "가격": 700000},
    # 추가 데이터 필요시 여기에 계속 추가
]

# 엑셀 워크북 생성
wb = Workbook()
ws = wb.active

# 헤더 추가
ws.append(["제품ID", "제품명", "수량", "가격"])

# 데이터 추가
for product in products_data:
    ws.append([product["제품ID"], product["제품명"], product["수량"], product["가격"]])

# 엑셀 파일 저장
file_path = "c:/work/products.xlsx"
wb.save(file_path)

print(f"데이터가 {file_path}에 저장되었습니다.")
