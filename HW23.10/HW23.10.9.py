dict = {}
list = ['apple', 'banana', 'cherry', 'orange', 'banana', 'cherry', 'apple', 'banana']
for i in list:
    dict[i] = list.count(i)

print(dict)

