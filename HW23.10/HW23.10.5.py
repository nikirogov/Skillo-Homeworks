list = [5, 6 , 98, 98, 3, 1 , -2]
minimum = list[0]
maximum = list[0]
for i in list:

    if(i>maximum):
        minimum = i
    else:
        maximum = i
print(minimum, maximum)