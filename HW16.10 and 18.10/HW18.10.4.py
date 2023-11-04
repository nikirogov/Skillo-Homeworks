
products = {
    'banana' : 2,
    'bread' : 3,
    'Lego' : 43,
    'PC': 453,
    'gum': 1,
}
cart=[]
def add():
    total = 0
    while command == "add":
        stock = input("Your product (Type 'stop' to end): ")
        if stock == "stop":
            break
            
        if stock in products:
                # quantity = int(input(f"Quantity: "))
                # if quantity>0:
                #     cart.append((stock,quantity))
                #     total += products[stock]*quantity
            cart.append(stock)
            total+=products[stock]
        else:
            print("Product not found in the inventory.")
        print("Items added to the cart.")
    return total

def total_price():
    total = 0
    for item in cart:
        total += products.get(item)
    return total
def remove():
    total = total_price()
    while True:
        stock = input("Your product to remove (Type 'Stop' to end): ")
        if stock == "stop":
            break
        if stock in cart:
            total -= products[stock]
            cart.remove(stock)

        else:
            print("Product not found in the inventory.")
    print("Items added to the cart.")
    return total

def total_price_remove():
    total = 0
    for item in cart:
        total += products.get(item,0)
    return total

def ready():
    print("Items:")
    for item in cart:
        print(item)
    total_cost = total_price_remove()
    print(f"Total cost $:{total_cost}")
command = input("Command:")
while command == "add" or command == "remove"  or command =="ready" or command == "exit":
    if command == "add":
        add()
    elif command == "remove":
        remove()
    elif command == "ready":
        ready()
    elif command == "exit":
        break
    command=input("Command: ")




