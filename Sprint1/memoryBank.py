import random

def main():
    memoryBankMenu()    
    
def memoryBankMenu():
    print("You will practice ten problems of the same type.")
    print("1)multiply")
    print("2)divide")
    print("3)add")
    print("4)subtract")
    option = int(input("Pick an option: "))

    if option == 1:
        multiply()
    elif option == 2:
        divide()
    elif option == 3:
        add()
    elif option == 4:
        subtract()
    else:
        print("pick a number 1-4")

def multiply():
    wrong = 0
    count = 1
    
    number = int(input("Pick the first number for the first problem: "))
    number0 = int(input("Pick the second number for the first problem: "))
    total = number * number0
    
    count += 1  
    number1 = int(input("Pick the first number for the second problem: "))
    number11 = int(input("Pick the second number for the second problem: "))
    total1 = number1 * number11
    
    count += 1
    number2 = int(input("Pick the first number for the third problem: "))
    number22 = int(input("Pick the second number for the third problem: "))
    total2 = number2 * number22
    
    count += 1
    number3 = int(input("Pick the first number for the fourth problem: "))
    number33 = int(input("Pick the second number the fourth problem: "))
    total3 = number3 * number33

    count += 1
    number4 = int(input("Pick the first number for the fifth problem: "))
    number44 = int(input("Pick the second number the fifth problem: "))
    total4 = number4 * number44
    
    count += 1
    number5 = int(input("Pick the first number for the sixth problem: "))
    number55 = int(input("Pick the second number the sixth problem: "))
    total5 = number5 * number55
    
    count += 1
    number6 = int(input("Pick the first number for the seventh problem: "))
    number66 = int(input("Pick the second number the seventh problem: "))
    total6 = number6 * number66
    
    count += 1
    number7 = int(input("Pick the first number for the eighth problem: "))
    number77 = int(input("Pick the second number the eighth problem: "))
    total7 = number7 * number77
    
    count += 1
    number8 = int(input("Pick the first number for the ninth problem: "))
    number88 = int(input("Pick the second number the ninth problem: "))
    total8 = number8 * number88

    count += 1
    number9 = int(input("Pick the first number for the tenth problem: "))
    number99 = int(input("Pick the second number the tenth problem: "))
    total9 = number9 * number99

    print(number,"*", number0)
    answer = int(input("Enter your answer: "))                 
    if answer != total:
        int(input("Please try again: "))
        if answer != total:
            wrong += 1
            
    print(number1,"*", number11)
    answer = int(input("Enter your answer: "))                 
    if answer != total1:
        int(input("Please try again: "))
        if answer != total1:
            wrong += 1
            
    print(number2,"*", number22)
    answer = int(input("Enter your answer: "))                 
    if answer != total2:
        int(input("Please try again: "))
        if answer != total2:
            wrong += 1

    print(number3,"*", number33)
    answer = int(input("Enter your answer: "))                 
    if answer != total3:
        int(input("Please try again: "))
        if answer != total3:
            wrong += 1

    print(number4,"*", number44)
    answer = int(input("Enter your answer: "))                 
    if answer != total4:
        int(input("Please try again: "))
        if answer != total4:
            wrong += 1

    print(number5,"*", number55)
    answer = int(input("Enter your answer: "))                 
    if answer != total5:
        int(input("Please try again: "))
        if answer != total5:
            wrong += 1
            
    print(number6,"*", number66)
    answer = int(input("Enter your answer: "))                 
    if answer != total6:
        int(input("Please try again: "))
        if answer != total6:
            wrong += 1
            
    print(number7,"*", number77)
    answer = int(input("Enter your answer: "))                 
    if answer != total7:
        int(input("Please try again: "))
        if answer != total7:
            wrong += 1

    print(number8,"*", number88)
    answer = int(input("Enter your answer: "))                 
    if answer != total8:
        int(input("Please try again: "))
        if answer != total8:
            wrong += 1
            
    print(number9,"*", number99)
    answer = int(input("Enter your answer: "))                 
    if answer != total9:
        int(input("Please try again: "))
        if answer != total9:
            wrong += 1
            
    print("You got",wrong,"wrong answers out of 10.")

def divide():
    wrong = 0
    count = 1
    
    number = int(input("Pick the first number for the first problem: "))
    number0 = int(input("Pick the second number for the first problem: "))
    total = number / number0
    
    count += 1  
    number1 = int(input("Pick the first number for the second problem: "))
    number11 = int(input("Pick the second number for the second problem: "))
    total1 = number1 / number11
    
    count += 1
    number2 = int(input("Pick the first number for the third problem: "))
    number22 = int(input("Pick the second number for the third problem: "))
    total2 = number2 / number22
    
    count += 1
    number3 = int(input("Pick the first number for the fourth problem: "))
    number33 = int(input("Pick the second number the fourth problem: "))
    total3 = number3 / number33

    count += 1
    number4 = int(input("Pick the first number for the fifth problem: "))
    number44 = int(input("Pick the second number the fifth problem: "))
    total4 = number4 / number44
    
    count += 1
    number5 = int(input("Pick the first number for the sixth problem: "))
    number55 = int(input("Pick the second number the sixth problem: "))
    total5 = number5 / number55
    
    count += 1
    number6 = int(input("Pick the first number for the seventh problem: "))
    number66 = int(input("Pick the second number the seventh problem: "))
    total6 = number6 / number66
    
    count += 1
    number7 = int(input("Pick the first number for the eighth problem: "))
    number77 = int(input("Pick the second number the eighth problem: "))
    total7 = number7 / number77
    
    count += 1
    number8 = int(input("Pick the first number for the ninth problem: "))
    number88 = int(input("Pick the second number the ninth problem: "))
    total8 = number8 / number88

    count += 1
    number9 = int(input("Pick the first number for the tenth problem: "))
    number99 = int(input("Pick the second number the tenth problem: "))
    total9 = number9 / number99

    print(number,"/", number0)
    answer = int(input("Enter your answer: "))                 
    if answer != total:
        int(input("Please try again: "))
        if answer != total:
            wrong += 1
            
    print(number1,"/", number11)
    answer = int(input("Enter your answer: "))                 
    if answer != total1:
        int(input("Please try again: "))
        if answer != total1:
            wrong += 1
            
    print(number2,"/", number22)
    answer = int(input("Enter your answer: "))                 
    if answer != total2:
        int(input("Please try again: "))
        if answer != total2:
            wrong += 1

    print(number3,"/", number33)
    answer = int(input("Enter your answer: "))                 
    if answer != total3:
        int(input("Please try again: "))
        if answer != total3:
            wrong += 1

    print(number4,"/", number44)
    answer = int(input("Enter your answer: "))                 
    if answer != total4:
        int(input("Please try again: "))
        if answer != total4:
            wrong += 1

    print(number5,"/", number55)
    answer = int(input("Enter your answer: "))                 
    if answer != total5:
        int(input("Please try again: "))
        if answer != total5:
            wrong += 1
            
    print(number6,"/", number66)
    answer = int(input("Enter your answer: "))                 
    if answer != total6:
        int(input("Please try again: "))
        if answer != total6:
            wrong += 1
            
    print(number7,"/", number77)
    answer = int(input("Enter your answer: "))                 
    if answer != total7:
        int(input("Please try again: "))
        if answer != total7:
            wrong += 1

    print(number8,"/", number88)
    answer = int(input("Enter your answer: "))                 
    if answer != total8:
        int(input("Please try again: "))
        if answer != total8:
            wrong += 1
            
    print(number9,"/", number99)
    answer = int(input("Enter your answer: "))                 
    if answer != total9:
        int(input("Please try again: "))
        if answer != total9:
            wrong += 1
            
    print("You got",wrong,"wrong answers out of 10.")

def add():
    wrong = 0
    count = 1
    
    number = int(input("Pick the first number for the first problem: "))
    number0 = int(input("Pick the second number for the first problem: "))
    total = number + number0
    
    count += 1  
    number1 = int(input("Pick the first number for the second problem: "))
    number11 = int(input("Pick the second number for the second problem: "))
    total1 = number1 + number11
    
    count += 1
    number2 = int(input("Pick the first number for the third problem: "))
    number22 = int(input("Pick the second number for the third problem: "))
    total2 = number2 + number22
    
    count += 1
    number3 = int(input("Pick the first number for the fourth problem: "))
    number33 = int(input("Pick the second number the fourth problem: "))
    total3 = number3 + number33

    count += 1
    number4 = int(input("Pick the first number for the fifth problem: "))
    number44 = int(input("Pick the second number the fifth problem: "))
    total4 = number4 + number44
    
    count += 1
    number5 = int(input("Pick the first number for the sixth problem: "))
    number55 = int(input("Pick the second number the sixth problem: "))
    total5 = number5 + number55
    
    count += 1
    number6 = int(input("Pick the first number for the seventh problem: "))
    number66 = int(input("Pick the second number the seventh problem: "))
    total6 = number6 + number66
    
    count += 1
    number7 = int(input("Pick the first number for the eighth problem: "))
    number77 = int(input("Pick the second number the eighth problem: "))
    total7 = number7 + number77
    
    count += 1
    number8 = int(input("Pick the first number for the ninth problem: "))
    number88 = int(input("Pick the second number the ninth problem: "))
    total8 = number8 + number88

    count += 1
    number9 = int(input("Pick the first number for the tenth problem: "))
    number99 = int(input("Pick the second number the tenth problem: "))
    total9 = number9 + number99

    print(number,"+", number0)
    answer = int(input("Enter your answer: "))                 
    if answer != total:
        int(input("Please try again: "))
        if answer != total:
            wrong += 1
            
    print(number1,"+", number11)
    answer = int(input("Enter your answer: "))                 
    if answer != total1:
        int(input("Please try again: "))
        if answer != total1:
            wrong += 1
            
    print(number2,"+", number22)
    answer = int(input("Enter your answer: "))                 
    if answer != total2:
        int(input("Please try again: "))
        if answer != total2:
            wrong += 1

    print(number3,"+", number33)
    answer = int(input("Enter your answer: "))                 
    if answer != total3:
        int(input("Please try again: "))
        if answer != total3:
            wrong += 1

    print(number4,"+", number44)
    answer = int(input("Enter your answer: "))                 
    if answer != total4:
        int(input("Please try again: "))
        if answer != total4:
            wrong += 1

    print(number5,"+",number55)
    answer = int(input("Enter your answer: "))                 
    if answer != total5:
        int(input("Please try again: "))
        if answer != total5:
            wrong += 1
            
    print(number6,"+", number66)
    answer = int(input("Enter your answer: "))                 
    if answer != total6:
        int(input("Please try again: "))
        if answer != total6:
            wrong += 1
            
    print(number7,"+", number77)
    answer = int(input("Enter your answer: "))                 
    if answer != total7:
        int(input("Please try again: "))
        if answer != total7:
            wrong += 1

    print(number8,"+", number88)
    answer = int(input("Enter your answer: "))                 
    if answer != total8:
        int(input("Please try again: "))
        if answer != total8:
            wrong += 1
            
    print(number9,"+", number99)
    answer = int(input("Enter your answer: "))                 
    if answer != total9:
        int(input("Please try again: "))
        if answer != total9:
            wrong += 1
            
    print("You got",wrong,"wrong answers out of 10.")

def subtract():
    wrong = 0
    count = 1
    
    number = int(input("Pick the first number for the first problem: "))
    number0 = int(input("Pick the second number for the first problem: "))
    total = number - number0
    
    count += 1  
    number1 = int(input("Pick the first number for the second problem: "))
    number11 = int(input("Pick the second number for the second problem: "))
    total1 = number1 - number11
    
    count += 1
    number2 = int(input("Pick the first number for the third problem: "))
    number22 = int(input("Pick the second number for the third problem: "))
    total2 = number2 - number22
    
    count += 1
    number3 = int(input("Pick the first number for the fourth problem: "))
    number33 = int(input("Pick the second number the fourth problem: "))
    total3 = number3 - number33

    count += 1
    number4 = int(input("Pick the first number for the fifth problem: "))
    number44 = int(input("Pick the second number the fifth problem: "))
    total4 = number4 - number44
    
    count += 1
    number5 = int(input("Pick the first number for the sixth problem: "))
    number55 = int(input("Pick the second number the sixth problem: "))
    total5 = number5 - number55
    
    count += 1
    number6 = int(input("Pick the first number for the seventh problem: "))
    number66 = int(input("Pick the second number the seventh problem: "))
    total6 = number6 - number66
    
    count += 1
    number7 = int(input("Pick the first number for the eighth problem: "))
    number77 = int(input("Pick the second number the eighth problem: "))
    total7 = number7 - number77
    
    count += 1
    number8 = int(input("Pick the first number for the ninth problem: "))
    number88 = int(input("Pick the second number the ninth problem: "))
    total8 = number8 - number88

    count += 1
    number9 = int(input("Pick the first number for the tenth problem: "))
    number99 = int(input("Pick the second number the tenth problem: "))
    total9 = number9 - number99

    print(number,"-", number0)
    answer = int(input("Enter your answer: "))                 
    if answer != total:
        int(input("Please try again: "))
        if answer != total:
            wrong += 1
            
    print(number1,"-", number11)
    answer = int(input("Enter your answer: "))                 
    if answer != total1:
        int(input("Please try again: "))
        if answer != total1:
            wrong += 1
            
    print(number2,"-", number22)
    answer = int(input("Enter your answer: "))                 
    if answer != total2:
        int(input("Please try again: "))
        if answer != total2:
            wrong += 1

    print(number3,"-", number33)
    answer = int(input("Enter your answer: "))                 
    if answer != total3:
        int(input("Please try again: "))
        if answer != total3:
            wrong += 1

    print(number4,"-", number44)
    answer = int(input("Enter your answer: "))                 
    if answer != total4:
        int(input("Please try again: "))
        if answer != total4:
            wrong += 1

    print(number5,"-", number55)
    answer = int(input("Enter your answer: "))                 
    if answer != total5:
        int(input("Please try again: "))
        if answer != total5:
            wrong += 1
            
    print(number6,"-", number66)
    answer = int(input("Enter your answer: "))                 
    if answer != total6:
        int(input("Please try again: "))
        if answer != total6:
            wrong += 1
            
    print(number7,"-", number77)
    answer = int(input("Enter your answer: "))                 
    if answer != total7:
        int(input("Please try again: "))
        if answer != total7:
            wrong += 1

    print(number8,"-", number88)
    answer = int(input("Enter your answer: "))                 
    if answer != total8:
        int(input("Please try again: "))
        if answer != total8:
            wrong += 1
            
    print(number9,"-", number99)
    answer = int(input("Enter your answer: "))                 
    if answer != total9:
        int(input("Please try again: "))
        if answer != total9:
            wrong += 1
            
    print("You got",wrong,"wrong answers out of 10.")

if __name__ == "__main__":
    main()
