

def mainMenu():
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Quit Program")

    selection = int(input("Please enter a menu choice: "))
    if selection == 1:
        addition()
    elif selection == 2:
        subtraction()
    elif selection == 3:
        multiplication()
    elif selection == 4:
        division()
    elif selection == 5:
        exit
    else:
        print("Error wrong choice. Enter 1-5")
        mainMenu()

def addition():
    count = 1
    while count <= 2:
        firstNumber = int(input("Please enter a number: "))
        secondNumber = int(input("Please enter a second number: "))
        total = firstNumber + secondNumber
        correctAnswer = int(input("Please enter what you think the answer will be: "))
        print(firstNumber, " + ", secondNumber ," = ", correctAnswer)
        if correctAnswer == total:
            print("- - -- - - = - - - o")
        else:
            print("EEE")
            count+=1
    else:
        print(firstNumber, " + ", secondNumber ," = ", correctAnswer)
        print("The correct answer is", total)
    


def subtraction():
    count = 1
    while count <= 2:
        firstNumber = int(input("Please enter a number: "))
        secondNumber = int(input("Please enter a second number: "))
        total = firstNumber - secondNumber
        correctAnswer = int(input("Please enter what you think the answer will be: "))
        print(firstNumber, " - ", secondNumber ," = ", correctAnswer)
        if correctAnswer == total:
            print("- - -- - - = - - - o")
        else:
            print("EEE")
            count+=1
    else:
        print(firstNumber, " - ", secondNumber ," = ", correctAnswer)
        print("The correct answer is", total)

def multiplication():
    count = 1
    while count <= 2:
        firstNumber = int(input("Please enter a number: "))
        secondNumber = int(input("Please enter a second number: "))
        total = firstNumber * secondNumber
        correctAnswer = int(input("Please enter what you think the answer will be: "))
        print(firstNumber, " * ", secondNumber ," = ", correctAnswer)
        if correctAnswer == total:
            print("- - -- - - = - - - o")
        else:
            print("EEE")
            count+=1
    else:
        print(firstNumber, " * ", secondNumber ," = ", correctAnswer)
        print("The correct answer is", total)



def division():
    count = 1
    while count <= 2:
        firstNumber = int(input("Please enter a number: "))
        secondNumber = int(input("Please enter a second number: "))
        total = firstNumber / secondNumber
        correctAnswer = int(input("Please enter what you think the answer will be: "))
        print(firstNumber, " / ", secondNumber ," = ", correctAnswer)
        if correctAnswer == total:
            print("- - -- - - = - - - o")
        else:
            print("EEE")
            count+=1
    else:
        print(firstNumber, " / ", secondNumber ," = ", correctAnswer)
        print("The correct answer is", total)

if __name__ == "__main__":
    mainMenu()
