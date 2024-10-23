# 셀리니움_웹드라이버_네이버로그인.py
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import clipboard
import time

#selenium 4.6이상은 웹드라이버 설치 없이 사용 
driver = webdriver.Chrome()
driver.get('https://nid.naver.com/nidlogin.login')

# 로그인 창에 아이디/비밀번호 입력
loginID = "papasmf1004"
clipboard.copy(loginID)
#mac은 COMMAND, window는 CONTROL
driver.find_element(By.XPATH,'//*[@id="id"]').send_keys(
    Keys.CONTROL, 'v')

loginPW = "1234"
clipboard.copy(loginPW)
driver.find_element(By.XPATH,'//*[@id="pw"]').send_keys(
    Keys.CONTROL, 'v')
time.sleep(1)

# 로그인 버튼 클릭
driver.find_element(By.XPATH,'//*[@id="log.login"]').click()

while True:
    pass 