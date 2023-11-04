import random
num1 = random.randint(1, 100)
num2 = random.randint(1, 100)
print (num1,num2)
answer = int(input("How much does it equal to:"))
sum=num1+num2

while answer != sum:

    answer = int(input("No, how much does it equal to:"))

