import numpy as np 

arr = np.arange(4)
print(arr[0])

arr = np.arange(4).reshape(2,2)
print(arr[0])


print(arr[ :2])

#2개의 인덱스를 []안에 지정할 수 있다.
#print(arr[ [0,2] ])

#2차원 데이터의 슬라이싱
#4행5열로 구성된 ndarray에서 두개의 행을 슬라이싱
print("---2차원 데이터 슬라이싱---")
arr = np.arange(20).reshape(4,5)
print(arr[ :2])

#왼쪽 끝의 두개 컬럼을 슬라이싱
#ndarray가 아닌 리스트라면 다음과 같이 리스트에
#값을 저장하는 번거로운 일을 해야 한다.
result = []
for row in arr:
    row_01 = [ row[0], row[1] ]
    result.append(row_01)

#ndarray는 한번에 컬럼의 슬라이싱을 할 수 있다. 
#행은 전체를 선택하기 위해 시작 인덱스와 끝 인덱스를 생략하고
#열은 0부터 2번위치까지만 가져온다. 
print("---왼쪽끝의 2개 컬럼을 슬라이싱---")
print(arr[:, :2])
print("-----------")

#행은 1번부터 끝까지 데이터를 가져와야 하며
#열은 2번부터 끝까지 가져온다.
print(arr[1:4, 2:5])
print(arr[1:, 2:])

#브로드캐스팅
#넘파이는 연산이 전체 데이터로 확장된다. 
#반복문을 사용하지 않으니 코드가 짦아지고 읽기도 좋아진다.
print("---브로드캐스팅---")
a = np.array( [1,2,3] )
b = np.array( [2,3,4] )
print(a+b)
print(a*b)
print(a%b)

#스칼라 연산은 전체 데이터에 확장 적용된다. 
print("---3을 더하는 브로드캐스팅---")
print(a + 3)

#데이터를 파이썬리스트가 아닌 ndarray로 표현하면 
#뺄셈 연산 하나로 일자별로 차이값을 쉽게 계산한다.
print("---고가와 저가---") 
high = [92700, 92400, 92100, 94300, 92300]
low = [90000, 91100, 91700, 92100, 90900]

arr_high = np.array(high)
arr_low = np.array(low)

arr_diff = arr_high - arr_low 
print(arr_diff)


#고가에는 3배, 저가에는 2배의 가중치를 부여
arr_high_x3 = arr_high * 3 
arr_low_x2 = arr_low * 2 
print(arr_high_x3 + arr_low_x2)


#첫번째행에는 고가, 
#두번째행에는 저가가 이차원형태로 저장
print("---하나의 변수에 담기---")
data = [
    [92700, 92400, 92100, 94300, 92300],
    [90000, 91100, 91700, 92100, 90900]
]
arr = np.array(data)
print(arr[0] * 3 + arr[1] * 2)


