def plus(a,b):
    return a+b
def minus(a,b):
    res=a-b
    return res
def multi(a,b):
    res=a*b
    return res
def div(a,b):
    if b==0:
        return "Division by zero is not allowed"
    res=a/b
    return res
a = float(input("Your first number"))
b = float(input("Your second number"))
znak = input("Your operator")
if(znak == '+'):
    print(plus(a,b))
elif(znak == '-'):
    print(minus(a,b))
elif(znak == '*'):
    print(multi(a,b))
elif(znak == '/'):
    print(div(a,b))