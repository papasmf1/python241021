import numpy as np 

#조건 연산
print("---조건 연산---")
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
print("---조건을 묶은경우---")
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
print("---where함수---")
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

