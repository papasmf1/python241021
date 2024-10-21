# DemoSetTuple.py

#세트형식
a = {1,2,3,3}
b = {3,4,4,5}
print(a)
print(b)

print(type(a))
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

#튜플형식
tp = (10, 20, 30)
print(len(tp))
print(type(tp))

#함수를 정의
def calc(a,b):
    return a+b, a*b 

#함수를 호출
result = calc(3,4)
print(result[0], result[1]) 

print("id: %s, name: %s" % ("kim", "김유신"))

#형식을 변환(Type Casting)
a = set((1,2,3))
print(a)
b = list(a)
b.append(4)
print(b)
c = tuple(b)
print(c)

#딕셔너리 
colors = {"apple":"red", "banana":"yellow"}
print(colors)
#입력
colors["cherry"] = "red"
print(colors)
#삭제
del colors["apple"]
for item in colors.items():
    print(item)

for k,v in colors.items():
    print(k, v)

#Bool형식 
isRight = False 
print(type(isRight))
print(1 < 2)
print(1 != 2)
print(1 == 2)
print(True and True and True)
print(True and True and False)
print(True or False or False)

#연산자
print(5/2)
print(5//2)
print(5%2)
print(4%2)





