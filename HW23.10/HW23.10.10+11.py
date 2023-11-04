list0 = ['apple', 'banana', 'cherry', 'orange']
list1 = ['banana', 'cherry', 'apple', 'strawberry']

for i in list0:
    for j in list1:
        if(i == j):
            print(i)
print ("\n")
list = ['apple', 'banana', 'cherry', 'orange']
list2 = ['banana', 'cherry', 'apple']
brlist2 = 0
brlist1 = 0
br = 0
for i in list:
    brlist1+=1
    for j in list2:
        brlist2+=1

        if(i == j):
            print(i)
            br=br+1
brlist2 =brlist2/brlist1
if(brlist2>brlist1):
    if (br == brlist1):
        print("subset")
    else:
        print('not subset')
else:
    if (br == brlist2):
        print("subset")
    else:
        print('not subset')

