"""
Recursion Exercise
"""

def countdown(number: int):
    if number >= 0:
        print(number)
        countdown(number - 1)

countdown(100)

""" Extra Challenge
Use the concept of recursion to:
 * - Calculate the factorial of a specific number (the function receives that number).
 * - Calculate the value of a specific element (based on its position) in the 
 *   Fibonacci sequence (the function receives the position).
 """

def factorial(number: int) -> int:
    if number < 0:
        print("Negative numbers are not valid")
        return 0
    elif number == 0:
        return 1

    return number * factorial(number - 1) 

print(factorial(5))

def fibonacci(number: int) -> int:
    if number <= 0:
        print("Position must be greater than zero")
        return 0
    elif number <= 2:
        return number - 1
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)

print(fibonacci(5))