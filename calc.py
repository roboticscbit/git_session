def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def mul(x, y):
    return x * y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Power")

while True:
    choice = input("Enter choice(1/2/3/4/5): ")

    if choice in ('1', '2', '3', '4','5'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(add(num1, num2))

        elif choice == '2':
            print(subtract(num1, num2))
        
        elif choice=='3':
            print(mul(num1,num2))
        
	elif choice == '5':
	    print(pow(num1, num2))
	break
    else:
        print("Invalid Input")
