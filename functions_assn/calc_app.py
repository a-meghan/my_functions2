#Task 1 - Arithmetic functions (Order Of Operations)

#Add
def add_nums(num_1, num_2):
    return num_1 + num_2

#Subtract
def subtract_nums(num_1, num_2):
    return num_1 - num_2

#Multiply
def multiply_nums(num_1, num_2):
    return num_1 * num_2

#Divide
def divide_nums(num_1, num_2):
        try:
            return num_1 / num_2
        except ZeroDivisionError:
            return "Error: division by zero is not allowed."


#Task 2 - Ask for numbers & OOO

#Ask for numbers
num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))

def calculate():
    operation = input("Choose an order of operation: add, subtract, multiply, divide: ")
    #Ask what operation to use
    if operation == "add":
        print(add_nums(num_1, num_2))
    elif operation == "subtract":
        print(subtract_nums(num_1, num_2))
    elif operation == "multiply":
        print(multiply_nums(num_1, num_2))
    elif operation == "divide":
        print(divide_nums(num_1, num_2))
    else:
        print("That is not a valid order of operation.")

calculate()

#Task 3- ZeroDivision error- see code blocks 16-20