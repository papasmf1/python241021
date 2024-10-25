import numpy as np

#타입을 지정할 수 있다. 
arr = np.array([1,2,3], 
               dtype=np.uint8)
print(arr.dtype)
print(arr.dtype.kind)
print(arr.dtype.alignment)

#인덱싱과 슬라이싱
arr = np.arange(4)
print(arr[0])

#2차원 ndarray의 경우 인덱싱은 기본적으로 행에 적용
#아래의 코드는 0번째 행을 리턴 
arr = np.arange(4).reshape(2,2)
print(arr[0])

#0행 0열을 지정한다면
print(arr[0][0])
#이렇게 지정하는 것이 성능상 유리하다.
print(arr[0,0])




