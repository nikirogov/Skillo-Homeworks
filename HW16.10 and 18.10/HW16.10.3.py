i=1
for i in range(1000):

    if i % 15 != 0 and i != 0:
        if i % 3 == 0:
            print (i,"Fizz")
        if i % 5 == 0:
            print (i,"Buzz")
    if i % 15 == 0 and i != 0:
        print(i,"FizzBuzz")

i=i+1