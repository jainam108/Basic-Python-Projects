def add(x, y):
    return x+y
def substract(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y

print("Select operation")
print("1.Add")
print("2.Substract")
print("3.Multiplication")
print("4.Division")

choice = input("Enter choice from 1/2/3/4: ")
if choice in ("1","2","3","4"):
    num1 = float(input("Enter your number here: "))
    num2 = float(input("Enter your number here: "))
    if choice == '1':
        print(num1, "+" ,num2, "=", add(num1, num2))

    elif choice == '2':
        print(num1, "-", num2, "=", substract(num1, num2))

    elif choice == '3':
        print(num1, "*" ,num2, "=", mul(num1,num2))

    elif choice == '4':
        print(num1, "/" , num2, "=", div(num1, num2))

else:
    print("Invalid Input")