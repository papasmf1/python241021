import random

#램덤 숫자를 생성
print(random.random())
print(random.random())

# 로또 번호 생성
lotto = random.sample(range(1, 46), 5)
print(lotto)

from os.path import *

print(abspath("python.exe"))
print(basename("c:\\python310\\python.exe"))

print(getsize("c:\\python310\\python.exe"))


fileName = "c:\\python310\\python.exe"

if exists(fileName):
    print("파일크기: ", getsize(fileName))
else:
    print("파일이 없습니다.")

import os 

print("운영체제이름:", os.name)
print("운영체제 환경변수:", os.environ)

#파일 목록 가져오기 
import glob
lst = glob.glob(r"c:\work\*.py")
for item in lst:
    print(item)

    


