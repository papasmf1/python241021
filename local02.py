b = 2
def test2():
    global b
    b = 3 
    print("b={0}".format(b))

test2()
print("b={0}".format(b))
