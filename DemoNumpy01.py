import numpy as np 

data = [1,2,3]
arr = np.array(data)
print(arr)
print(type(arr))

#원래는 반복문 사용
data = [1,2,3]
result = []
for i in data:
    result.append(i*10)
print(result)

arr = np.array([1,2,3])
result = arr*10
print(result)


