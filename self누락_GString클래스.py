#전역변수 초기화 
strName = "Not Class Member"

class DemoString:
    def __init__(self):
        #인스턴스 멤버변수 
        self.strName = "" 
    def set(self, msg):
        self.strName = msg
    def print(self):
        #약간의 버그 발생 
        print(self.strName)

d = DemoString()
d.set("First Message")
d.print()
