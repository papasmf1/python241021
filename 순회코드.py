import time
l = range(1000)

t = time.mktime(time.localtime())
for i in l:
    print(i,)
t1 = time.mktime(time.localtime()) - t

t = time.mktime(time.localtime())
print(", ".join(str(i) for i in l))
t2 = time.mktime(time.localtime()) - t

print("for  ")
print("Take {0} seconds".format(t1))
print("join() ")
print("Take {0} seconds".format(t2))
