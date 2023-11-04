items = {"Coffee": 2.2, "Tea": 1.5, "Chocolate": 2.5}
income = 0
for item in items.keys():

    qty = int(input(f"How many {item}s have you sold? "))
    income = income + (qty * items[item])

print(f"\nThe income today was £{income:0.2f}")

def get_integer_input():
    try:
        num = int(input("Enter an integer: "))
        return num
    except ValueError:
        print('Try again, enter an integer')
number = get_integer_input()
print("You entered:", number)

arr= [1,2,5,217,15,-3,-7,8]
def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

print(selection_sort(arr))