def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return(x / y)
print("Select Operation")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    choice = input("Enter Choice(1/2/3/4 :)")
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number :"))
            num2 = float(input("Enter second number :"))
        except ValueError:
             print("Invalid input please try again")
             
             continue
        if choice == '1':
            print(num1, "+", num2, '=', add(num1, num2))
        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif choice == '3':
            print(num1, '*', num2, "=", multiply(num1, num2))
        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

    continue_cal = input("next calculation: (yes/no)")
    if continue_cal == 'no':
        break
    else:
        print("invalid input")




