import numpy as np 

#이번에는 2차원 배열 
data2d = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(data2d[0])

#넘파이에서는 특정행을 지정할 수 있다. 
arr = np.array(data2d)
print(arr[:, 0])
#[행인덱스, 열인덱스]를 지정할 수 있다. 0번 컬럼을 지정한 결과이다. 

#넘파이에서는 다차원 배열을 위한 ndarray클래스를 제공한다. 
#범용적으로 사용되는 파이썬 리스트 타입을 행렬과 다차원 배열에 최적화된 
#ndarray타입으로 변환한다.
print("---ndarray타입---")
data1 = [1,2,3,4]
arr1 = np.array(data1)
print(arr1)
print(type(arr1))

#2차원 리스트 
data2 = [
    [1,2],
    [3,4]
]
arr2 = np.array(data2)
print(arr2)
print(type(arr2))
print(type(arr2[0]))

#shape는 ndarray의 크기정보
#ndim은 차원정보, dtype은 데이터 타입
print(arr2.shape)
print(arr2.ndim)
print(arr2.dtype)

#4행 1열의 데이터
data = [
    [1],
    [2],
    [3],
    [4]
]
c = np.array(data)
print(c.shape)
#(4,1) 4행 1열로 표시된다. 

print(np.zeros(3))
print(np.ones(3))

#다차원 배열도 생성한다.
size = (3,4)
print(np.zeros(size))

#range함수와 비슷하지만 arange는 실수도
#생성할 수 있다.
print(np.arange(5))
print(np.arange(1,5))
print(np.arange(1,5,2))

ndarr1 = np.arange(6)
ndarr2 = ndarr1.reshape(2,3)
print(ndarr2)

