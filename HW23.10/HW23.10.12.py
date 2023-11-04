final_set = set()
list = ['apple', 'banana', 'cherry', 'orange', 'banana', 'cherry', 'apple', 'banana']
for i in list:
    if(list.count(i)==1):
        final_set.add(i)

print(final_set)
