from selenium import webdriver as wb
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
#이미지를 저장하기 위한 라이브러리 
from urllib.request import urlretrieve

def createFolder (name) :
    if os.path.isdir(f'./{name}') == False :
        os.mkdir(f'./{name}')
        print(f'{name} 폴더 생성 완료')
    else :
        print('이미 존재하는 폴더입니다.')


input_name = input("검색할 동물이름:")
driver = wb.Chrome()
driver.get(f"https://search.naver.com/search.naver?where=image&sm=tab_jum&query={input_name}")
#약간의 대기 시간 주기 
time.sleep(2) 
for i in range(2) : 
    driver.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.END)
    time.sleep(2) 
print("스크롤 다운 완료")
img = driver.find_elements(By.CSS_SELECTOR, "._fe_image_tab_content_thumbnail_image") 

#이미지의 src속성값 가져오기 
src = [i.get_attribute('src') for i in img] 
srclst = []
#잘못된 주소를 가져온 src 데이터를 빼고 src_lst에 담기
for i in src : 
    if 'data:image' not in i :
            srclst.append(i)
#먼저 폴더를 생성 
createFolder(input_name) 
#.jpg 이미지 파일로 저장
for i in range(len(srclst)) : 
    urlretrieve(srclst[i], f'./{input_name}/{input_name}_{i+1}.jpg')
driver.close() # 브라우저 닫기
print(f'{input_name} 이미지 수집, 저장 작업 완료')