

# declare functions
def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def mult(x,y):
    return x * y

def div(x,y):
    return x / y


# Print the options for the user to select from
print("Select operation, 1 = Add, 2 = Subtract, 3 = multiply, 4 = divide")

# While statement to ensure the program knows what to do while the following is happening (true)
while True:
    choice = input("Enter choice(1/2/3/4): ")

    # If statement to tell the program as long as the user is entering a valid choice (1,2,3,4) the program should ask for the 2 numbers inputted
    if choice in ("1","2","3","4"):
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        #If statement to tell the program depending what choice was inputted, to perform the following
    if choice == '1':
        print(num1, "+", num2, '=', add(num1, num2))

        #elif is if the first choice isnt selected, it is an ELSE IF (elif) to check if the choice selected was this selection
    elif choice == '2':
            print(num1, "-", num2, '=', sub(num1, num2))

    elif choice == '3':
                print(num1, "*", num2, multiply(num1, num2))


    elif choice == '4':
                    print(num1, "/", num2, div(num1, num2))

    break

# Else statement for error handling if the commands inputted from the user is invalid
else:
                print("Invalid input")
