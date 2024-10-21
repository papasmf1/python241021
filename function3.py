# function3.py
#필터링하는 함수
lst = [10,25,30]
iterL = filter(None, lst)
for item in iterL:
    print(item)
    
#조건에 해당하는 함수
def getBiggerThan20(i):
    return i > 20

iterL = filter(getBiggerThan20, lst)
for item in iterL:
    print(item)
    
print("==람다함수정의==")
iterL = filter(lambda i: i>20, lst)
for item in iterL:
    print(item)

#맵핑하는 함수
lst = [1,2,3]
def add10(i):
    return i + 10 

for item in map(add10, lst):
    print(item)

    
