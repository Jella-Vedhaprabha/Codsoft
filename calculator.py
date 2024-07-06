def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y==0:
        return "Error:Division by zero"
    else:
        return x/y
def modulus(x,y):
    if y==0:
        return "Error:Modulus by zero"
    else:
        return x%y
def power(x,y):
    return x**y
def calculator():
    print("Welcome to simple calculator!")
    while True:
        try:
            num1=float(input("Enter first number:"))
            num2=float(input("Enter second number:"))
        except ValueError:
            print("Please enter valid numbers.")
            continue
        print("1:Add")
        print("2:Subract")
        print("3:Multiply")
        print("4:Divide")
        print("5:Modulus")
        print("6:Power")
        print("Select operation:")
        try:
            choice=int(input("Enter operation number(1-6):"))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        if choice==1:
            print(f"{num1}+{num2}={add(num1,num2)}")
        elif choice==2:
            print(f"{num1}-{num2}={subtract(num1,num2)}")
        elif choice==3:
            print(f"{num1}*{num2}={multiply(num1,num2)}")
        elif choice==4:
            print(f"{num1}/{num2}={divide(num1,num2)}")
        elif choice==5:
            print(f"{num1}%{num2}={modulus(num1,num2)}")    
        elif choice==6:
            print(f"{num1}^{num2}={power(num1,num2)}")
        else:
            print("Invalid operation number.Please enter a number between 1to6.")
        another_calculation=input("Do you want to perform another calculation?(yes/no):").lower()
        if another_calculation!='yes':
            print("Thank you for using simple calculator!")
            break
        
calculator()
