import  openpyxl  as  op

wb = op.load_workbook("sample20.xlsx")
ws = wb.active

#ws에서 데이터범위 설정
rng = ws["A1:C3"] 

for  row_data  in  rng:
    for  data  in  row_data:
        #해당 data가 2로 나눈 나머지가 0이면 공백처리
        if (data.value % 2) == 0:
            data.value = ""

#Workbook 객체 저장
wb.save("sample20_result.xlsx")