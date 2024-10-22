
lst = [100, 200, 300]

for item in lst:
    print(item)

print("---range()---")
print(list(range(10)))
print(list(range(2000,2025)))
print(list(range(1,32)))

print("---리스트 내장---")
lst = list(range(1,11))
print(lst)
print( [i**2 for i in lst if i > 5] )
tp = ("apple", "orange", "kiwi")
print( [len(i) for i in tp] )
d = {100:"apple", 200:"orange"}
print( [v.upper() for v in d.values()] )

print("---필터링 함수---")
lst = [10, 25, 30]
itemL = filter(None, lst)
for i in itemL:
    print("item:{0}".format(i))

#함수 정의
def getBiggerThan20(i):
    return i > 20

print("---필터링 함수 사용---")
itemL = filter(getBiggerThan20, lst)
for i in itemL:
    print("item:{0}".format(i))

print("---람다 함수 사용---")
itemL = filter(lambda x:x>20, lst)
for i in itemL:
    print("item:{0}".format(i))
