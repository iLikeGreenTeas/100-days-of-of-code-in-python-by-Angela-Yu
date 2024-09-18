import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

math_operations={"+":add, "-":subtract,
                "*":multiply, "/":divide}

#print(math_operations["*"](n1=4, n2=8))

def run():
    print(art.logo)
    accumulate = "n"
    num1 = float(input("Enter the first number:\n"))
    exit_loop = False
    while exit_loop == False:
        operator = input("Add, Subtract, Multiply, or Divide? Type '+', '-', '*', or '/':\n")
        num2 = float(input("Enter the second number:\n"))
        result = math_operations[operator](num1, num2)
        print(f"The result is: {result}.")
        again = input("Another calculation? Type 'y' or 'n':\n").lower()
        if again == 'n':
            exit_loop = True
        elif again == 'y':
            accumulate = input("Continue working with the previous result? Type 'y', or 'n':\n").lower()
            if accumulate == 'y':
                num1 = result
            elif accumulate == 'n':
                num1 = int(input("Enter the first number:\n"))
            else:
                print("Enter 'y' or 'n':\n").lower()
        else:
            print("Enter 'y' or 'n':\n").lower()
                
run()
        
        
        
### Functionality
# - Program asks the user to type the first number.
# - Program asks the user to type a mathematical operator (a choice of "`+`", "`-`", "`*`" or "`/`")
# - Program asks the user to type the second number.
# - Program works out the result based on the chosen mathematical operator.
# - Program asks if the user wants to continue working with the previous result.
# - If yes, program loops to use the previous result as the first number and then repeats the calculation process.
# - If no, program asks the user for the fist number again and wipes all memory of previous calculations.
# - Add the logo from art.py