import openpyxl as op

#Workbook 객체 생성
wb = op.load_workbook("sample20.xlsx")
#활성화 된 Sheet를 객체로 생성
ws = wb.active

#1행부터 2개행까지 행을 삭제한다.
ws.delete_rows(1,2)

#Workbook 객체 저장
wb.save("sample20_result2.xlsx")