import numpy as np 

arr = np.arange(4)
print(arr[ :2])

#2개의 인덱스를 []안에 지정할 수 있다.
print(arr[ [0,2] ])

#2차원 데이터의 슬라이싱
#4행5열로 구성된 ndarray에서 두개의 행을 슬라이싱
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
print(arr[:, :2])


#행은 1번부터 끝까지 데이터를 가져와야 하며
#열은 2번부터 끝까지 가져온다.
print(arr[1:4, 2:5])
print(arr[1:, 2:])

#브로드캐스팅
#넘파이는 연산이 전체 데이터로 확장된다. 
#반복문을 사용하지 않으니 코드가 짦아지고 읽기도 좋아진다.
a = np.array( [1,2,3] )
b = np.array( [2,3,4] )
print(a+b)
print(a*b)
print(a%b)

#스칼라 연산은 전체 데이터에 확장 적용된다. 
print(a + 3)

#데이터를 파이썬리스트가 아닌 ndarray로 표현하면 
#뺄셈 연산 하나로 일자별로 차이값을 쉽게 계산한다. 
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
data = [
    [92700, 92400, 92100, 94300, 92300],
    [90000, 91100, 91700, 92100, 90900]
]
arr = np.array(data)
print(arr[0] * 3 + arr[1] * 2)



# weight = np.array( [3,2]).reshape(2,1)
# print(weight * arr).sum(axis=0)


#조건 연산
arr = np.array([10,20,30])
print(arr > 10)

arr = np.array([10,20,30])
cond = [False, True, True]
print(arr[ cond ])

#비교 연산이 간단하기 때문에
#코드를 한줄로 표현
print(arr[ arr > 10])

#얻어온 조건이 모두 참인지의 여부를 확인하고 
#싶은 경우가 종종 있다. 
#any는 하나라도 참인 경우
#all은 전체가 참인 경우
# cond.all()
# cond.any()

#파이썬의 and, or, not은 
#넘파이에서는 &, |, ~를 사용한다. 
arr = np.array([10,20,30])
cond0 = arr > 10
cond1 = arr < 30 
print(arr[ cond0 & cond1 ])

#코드를 한줄로 표현하면
arr = np.array([10,20,30])
print(arr[ (arr > 10) & (arr < 30) ])

#조건이 10이상이 값이 크다는 의미로 1
#그렇지 않은 경우 0으로 맵핑한다.
arr = np.array([10,20,30])
cond = arr > 10 
arr[cond] = 1 
arr[~cond] = 0 
print(arr)

#넘파이에는 where함수가 정의되어 있다. 
arr = np.array([10,20,30])
arr = np.where(arr>10, 1, 0)
print(arr)

#10보다 크면 10을 더하고
#그렇지 않으면 10을 빼는 경우
arr = np.where( arr>10, arr+10, arr-10)
print(arr)

#LG전자의 일자별 종가가 85000원 이하로 
#떨어진 날은?
lge = np.array([93000, 82400, 99100,
                81000, 72300])
result = lge[ lge <= 85000 ]
print( len(result) )

#함수와 메서드 
arr = np.arange(8).reshape(4,2)
print(arr.sum())

#sum메서드에 축정보를 지정할 수 있다. 
print(arr.sum(axis=0))
print(arr.sum(axis=1))

#램덤 정수를 만드는 경우
#아래는 실행할 때마다 숫자가 다르게 나온다. 
print(np.random.randint(3))
#5개를 출력하고 2행5열로 출력한다. 
print(np.random.randint(46, size=5))
print(np.random.randint(46, size=(2,5)))


#차트를 그릴 때 빈번히 사용하는 linespace함수
#시작,종료, 분할 지점의 수를 입력받아 균일한 크기의 구간으로 분할
x = np.linspace(0, 10, 3)
print(x)


#넘파이의 stack함수는 여러개의 ndarray를 하나로 합칠 때 사용
#수직으로 vstack 수평으로 hstack 
a = np.arange(4)
b = np.arange(4,8)
c = np.vstack( [a,b] )
print(c)

