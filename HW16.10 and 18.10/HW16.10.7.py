num = int(input("Number:"))
i = 2
br = 0
while i<num/2:
    if num % i == 0:
        br=br+1
        print ("Prime")
        break

    i=i+1
if br == 0:
    print ("Not prime")