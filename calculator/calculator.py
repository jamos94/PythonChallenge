# calculator! 
from art import logo
# import decimal
# from decimal import Decimal
def add(n1, n2):
    """Addition"""
    return n1 + n2

def minus(n1,n2):
    """Subtraction"""
    return n1 - n2

def times(n1,n2):
    """Multiplication"""
    return n1 * n2

def divide(n1,n2):
    """Division"""
    return n1 / n2

operations = {
    '+': add, 
    '-': minus, 
    '*': times,
    '/': divide
    }

def calculator():
    print(logo)

    num1 = float(input("what is your first number? "))
    # print out operations in list
    for i in operations:
        print(i)
    continue_calc = True
    while continue_calc == True:
        chosen_operation = input("Pick an operation: ")
        num2 = float(input("pick another number: "))
        call_function = operations[chosen_operation]
        answer = call_function(num1,num2)
        print(f"{num1} {chosen_operation} {num2} = {answer}")

        if input(f"type 'y' to continue calculating with {answer}, or 'n' to start a new calculation.\n").lower() == 'y':
            num1 = answer
        else: 
            calculator() # 'recursion' recalls the calculator to start fresh with new numbers to calculator
            continue_calc = False

calculator()