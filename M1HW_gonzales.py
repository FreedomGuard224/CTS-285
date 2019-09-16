## Edmund Gonzales
## 31 August 2019

def main():

    menu()

def menu():
    print("Welcome to the claculator program.")
    print("1. Add")
    print("2. Subtract")
    print("3. Divide")
    print("4. Mulitply")
    print("5. Exit")
    option = int(input("Enter a number: "))
    print("")

    if option == 1:
        add()
    elif option == 2:
        subtract()
    elif option == 3:
        divide()
    elif option == 4:
        multiply()
    elif option == 5:
        print("Have a great day!")
            
def choose():

    choice = ""
    print("")
    print("1. Repeat")
    print("2. Main Menu")
    choice = int(input("Enter a number: "))
    print("")

    if choice == 1:
        return 1
    elif choice == 2:
        return 2

    while choice != 1 or choice != 2:
        print(choice)
        choice = int(input("Enter 1 or 2: "))
        if choice == 1:
            return 1
        elif choice == 2:
            return 2

def add():
    print("Add two numbers together.")
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    sum = number1 + number2
    print(number1,"+",number2,"=",sum)
     
    if choose() == 1:
        add()
    else:
        menu()
    
def subtract():
    print("Get the value of a subtraction problem.")
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    sum = number1 - number2
    print(number1,"-",number2,"=",sum)

    if choose() == 1:
        subtract()
    else:
        menu()

def divide():
    print("Get the value of a division problem.")
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    sum = number1 / number2
    print(number1,"/",number2,"=",sum)

    if choose() == 1:
        divide()
    else:
        menu()
        
def multiply():
    print("Get the value of a multiplication problem.")
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    sum = number1 * number2
    print(number1,"*",number2,"=",sum)

    if choose() == 1:
        multiply()
    else:
        menu()
    
main()
