a = 2
def test():
    print(a)
    #a = 3이라고 하면 지역변수로 변경된다. 
    #a = 3


test()
print("a={0}".format(a))
