### User-Defined Functions ###

# Simple Function

def greet():
    print("Hello, Python!")

greet() 

# Function with Return Value

def return_greet():
    return "Hello, Python!"

greet = return_greet() # to save the return value in a variable
print(return_greet) # simple print without saving to a variable

# Function with One Argument

def arg_greet(name):
    print(f"Hello, {name}!") # Requires meeting the 'name' condition to execute

arg_greet("Mauricio") # full condition, since it now has the 'name' parameter completed or filled.

# Function with Multiple Arguments

def args_greet(greet, name):
    print(f"{greet}, {name}!") # Requires meeting both conditions "greet" and "name", otherwise it will throw an error.

args_greet("hi", "Mauricio") # Function requirements are met to complete the return.
args_greet("Mauricio", "Hi") # Greeting is reversed.
args_greet(name="Mauricio", greet="Hi") # adding keyword arguments so the condition is correctly met regardless of order.

# Function with Default Argument 

def default_arg_greet(name="Python"): # if the 'name' condition is not met, it defaults to the value "Python"
    print(f"Hello, {name}!")

default_arg_greet("Mauricio") # With 'name' condition filled.
default_arg_greet() # without 'name' condition, uses default value only.

# Functions with Arguments and Return Value

def return_args_greet(greet, name):
    return f"{greet}, {name}!"

print(return_args_greet("Hi", "Mauricio"))

# Function Returning Multiple Values

def multiple_return_greet():
    return "Hello", "Python"

greet, name = multiple_return_greet()
print(greet)
print(name)

# Functions with a Variable Number of Arguments

def variable_arg_greet(*names): # * before 'names' means it can take more than one "name".
    for name in names:
        print(f"Hello, {name}!")

variable_arg_greet("Python", "Mauricio", "MapiiedrA", "World")

# Functions with a Variable Number of Keyword Arguments

def variable_arg_greet(**names):  # ** means keyword arguments
    for key, value in names.items():
        print(f"{value} ({key})!")

variable_arg_greet(
     language="Python", 
     names="Mauricio", 
     alias="MapiiedrA", 
     age=32
     )

### Functions Inside Functions (Nested Functions) ###

def outer_function():
    def inner_function():
        print("Inner function: Hello, Python!")
    inner_function()

outer_function()

### Built-in Functions ###

print(len("Mauricio"))
print(type(32))
print("Mauricio".upper())

### Local and Global Variables ### Scope # Tip: Restrict variable scope as much as possible to make the code safer.

global_var = "Python"
print(global_var)

def hello_python():
    print(f"Hello, {global_var}")

def hello_python():
    local_var = "Hello"
    print(f"{local_var}, {global_var}")

print(global_var)
# print(local_var) Cannot be accessed from outside the function

hello_python()

"""
* EXTRA CHALLENGE (optional):
 * Create a function that accepts two string parameters and returns a number.
 * - The function prints all numbers from 1 to 100, keeping in mind that:
 *   - If the number is a multiple of 3, display the text string from the first parameter.
 *   - If the number is a multiple of 5, display the text string from the second parameter.
 *   - If the number is a multiple of both 3 and 5, display both text strings concatenated.
 *   - The function returns the number of times a number was printed instead of the text strings.
 *
 * Pay special attention to the syntax required for each case.
 * Every language follows specific conventions that you should respect so the code remains readable. ###
"""

def print_numbers(text_1, text_2) -> int:
    count = 0
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0: # this condition must come first, otherwise it won't trigger since combined multiples would be caught earlier
            print(text_1 + text_2)
        elif number % 3 == 0:
            print(text_1)
        elif number % 5 == 0:
            print(text_2)
        else:
            print(number)
            count += 1
    return count

print(print_numbers("Fizz", "Buzz")) # Famous "Text_1 = Fizz", "Text_2 = Buzz" in case we want to print this for a technical interview.