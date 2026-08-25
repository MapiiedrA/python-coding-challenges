"""
* EXERCISE:
 * - Create a comment in the code and include the URL of the official website
 *   for your chosen programming language.
 * - Demonstrate the different comment syntaxes available in the language
 *   (single-line, multi-line, etc.).
 * - Create a variable (and a constant if supported by the language).
 * - Create variables representing all primitive data types in the language
 *   (strings, integers, booleans, etc.).
 * - Print the following text to the terminal: "Hello, [name of your language]!"
"""

# https://python.org/
# this is a commentary on a line
"""
This is a multi-line comment
or documentation string (docstring)
used to describe code blocks.
"""

'''
This is a multi-line comment
or documentation string (docstring)
used to describe code blocks.
'''

my_variable = "My Variable"
my_variable = "New value of My Variable"
#python dont have Constant

My_Constant = "Mi constant" # By convention, constants are written in uppercase 

my_int = 1 #number without Double quotes for a int
my_float = 1.5 #Decimals
my_bool = True #logic boolean
my_bool = False
my_string = "My String Text"
my_other_string = 'My other String Text'

print("Hello, Python!")
      
print(type(my_int))
print(type(my_float))
print(type(my_bool))
print(type(my_string))