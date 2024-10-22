# class1.py 
#1)클래스를 정의
class Person:
    #초기화 메서드
    def __init__(self):
        #초기화 변수작업
        self.name = "default name"
    #메서드
    def print(self):
        print("My name is {0}".format(self.name))

#2)인스턴스 생성
p1 = Person()
p2 = Person() 
p1.name = "전우치"

p1.print() 
p2.print() 


    