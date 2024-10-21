lst = ['white','black','red','red']
result = []
for i in range(len(lst)):
    item = lst[i]
    if item == 'red':
        result.append(i)

print('결과:', result)
