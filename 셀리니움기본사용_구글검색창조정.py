from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
import time 

#크롬드라이버 실행
driver = webdriver.Chrome() 
#url주소 추가해서 실행 
driver.get("https://www.google.co.kr")
#창이 오픈되고 3초를 대기한다. 
time.sleep(3)

#<textarea class="gLFyf" jsaction="paste:puy29d;" id="APjFqb" maxlength="2048" name="q" rows="1" aria-activedescendant="" aria-autocomplete="both" aria-controls="Alh6id" aria-expanded="false" aria-haspopup="both" aria-owns="Alh6id" autocapitalize="off" autocomplete="off" autocorrect="off" autofocus="" role="combobox" spellcheck="false" title="검색" type="search" value="" aria-label="검색" data-ved="0ahUKEwiN1oGW9oGEAxU0nq8BHYCKAqkQ39UDCA4"></textarea>
#검색어창 찾기
searchBox = driver.find_element(By.CLASS_NAME, "gLFyf")
#XPath를 사용하는 경우
#//*[@id="APjFqb"]
#searchBox = driver.find_element(By.XPATH,"//*[@id='APjFqb']")

searchBox.send_keys("아이폰16")
searchBox.send_keys(Keys.RETURN)

while True:
    pass

