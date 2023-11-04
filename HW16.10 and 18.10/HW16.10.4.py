import random
num = random.randint(1, 100)
guess = int(input("Your guess:"))
while guess != num:

    if guess>num:
        print ("Too high")

    if guess<num:
        print ("Too low")


    guess = int(input("Your guess:"))
if  guess == num:
    print ("Congrats")