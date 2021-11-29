# calculator! 
from art import logo
print(logo)
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

def continue_calc(answer,num3,final_answer):
    chosen_operation = input("Pick an operation: ")
    call_function = operations[chosen_operation]
    num3 = int(input("pick another number: "))
    final_answer = call_function(num1,num2)
    print(f"{answer} {chosen_operation} {num3} = {final_answer}")

num1 = int(input("what is your first number? "))
# print out operations in list
for i in operations:
    print(i)


chosen_operation = input("Pick an operation: ")
num2 = int(input("pick another number: "))
call_function = operations[chosen_operation]
answer = call_function(num1,num2)
print(f"{num1} {chosen_operation} {num2} = {answer}")

continue_calc = input(f"type 'y' to continue calculating with {answer}, or 'n' to exit").lower()
# if continue_calc == 'y':
#     using_calc = True
#     while using_calc == True:
#         continue_calc(answer)
#     else:
#         using_calc == False
# else:
#     print("thanks for using, see you next time")