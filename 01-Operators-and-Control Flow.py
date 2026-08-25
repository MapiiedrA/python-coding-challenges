"""
Operators # Remember print(f"") for Op formatting # Operators apply to numbers, text strings, and objects
"""

# Arithmetic Operators
print(f"Addition: 10+3= {10+3}") # interpolation {}
print(f"Subtraction: 10-3= {10-3}")
print(f"Multiplication: 10*3 = {10*3}")
print(f"Division: 10 / 3 = {10/3}")
print(f"Modulus: 10 % 3 = {10*3}") # Integer Result
print(f"Exponent: 10 ** 3 = {10 ** 3}")
print(f"Floor Division: 10 // 3 = {10//3}")

# Comparison Operators # can be used with numbers and letters or variables
print(f"Equality: 10==3 is {10==3}")
print(f"Inequality: 10 != 3 is {10 != 3}")
print(f"Greater than: 10 > 3 is {10 > 3}")
print(f"Less than: 10 < 3 is {10 < 3}")
print(f"Greater than or equal to: 10 >= 3 {10 >= 3}")
print(f"Less than or equal to: 10 <= 3 {10 <= 3}")
print(f"Greater than or equal to: 10 >= 10 {10 >= 10}") # >= or <= True or False in Terminal depending on reality.

# Logical Operators
print(f"AND &&: 10 + 3 == 13 and 5 - 1 == 4 is {10 + 3 == 13 and 5 - 1 == 4}") # For AND && to be TRUE BOTH must be true.
print(f"OR ||: 10 + 3 == 13 or 5 - 1 == 4 is {10 + 3 == 13 or 5 - 1 == 4}")
print(f"OR ||: 10 + 3 == 14 or 5 - 1 == 4 is {10 + 3 == 14 or 5 - 1 == 4}") # The result will be TRUE in the Terminal because one of the Logical conditions is met.
print(f"NOT !: 10 + 3 == 14 is {10 + 3 == 14}")
print(f"NOT !: not 10 + 3 == 14 is {not 10 + 3 == 14}") # Will yield TRUE since the condition is met by the result being incorrect # it is a Reality

# Assignment Operators
my_number = 11 # assignment or Assignment Op # = is used to assign the number to the variable in this case "my_number"
print(my_number)
my_number += 1 # Addition and Assignment
print(my_number)
my_number -= 1 # Subtraction and Assignment
print(my_number)
my_number *= 2 # Multiplication and Assignment
print(my_number)
my_number /= 2 # Division and Assignment
print(my_number)
my_number %= 2 # Modulus and Assignment
print(my_number)
my_number **= 1 # Exponent and Assignment
print(my_number)
my_number //= 1 # Floor Division and Assignment
print(my_number)

# Identity Operators # Used to compare values but in their memory position
my_new_number = 1.0
print(f"my_number is my_new_number is {my_number is my_new_number}") # gives False because it has different memory values
my_new_number = my_number 
print(f"my_number is my_new_number is {my_number is my_new_number}") # Gives True because now "my_new_number has the same value as my_number" # the identity is the same
print(f"my_number is not my_new_number is {my_number is not my_new_number}") # adding not to negate the identity.

# Membership Operators # Something belongs to something
print(f"'a' in Mauricio' = {'a' in 'Mauricio'}") # Checks that "a" is inside "Mauricio" # True since it does belong or is inside the set
print(f"'b' not in Mauricio' = {'b' not in 'Mauricio'}") # False since 'b' is not inside Mauricio or the set

# Bitwise Operators # used to see bit operators
a = 10 # 1010 # Numbers or values in Binary
b = 3 # 0011
print(f"AND: 10 & 3 = {10 & 3}") # Result at bit level 0010 = 2
print(f"OR: 10 | 3= {10 | 3}") # 1011
print(f"XOR: 10 ^ 3 = {10 ^ 3}") # 1001
print(f"NOT: ~10 = {~10}") # gives Negative because it is inverting the result Bit by Bit on that representation of 10
print(f"Right shift: 10 >> 2 = {10 >> 2}") # 0010 is the binary value assigned to 2
print(f"Left shift: 10 << 2 = {10 << 2}") # 101000 this is basically 40 in binary

"""
Control Structures
"""

# Conditionals

my_string = "Mauricio"

if my_string == "Mauricio":
    print("my_string is 'Mauricio'")
elif my_string == "Mapiedra":
    print("my_string is 'Mapiedra'")
else:
    print("my_string is not 'Gutierrez' nor 'Rojas'")

# Iteratives

for i in range(11):  # FOR is used to create loops.
    print(i)

i = 0   

while i <= 10: # so the loop runs while the condition is met, the value of i being less than 10 continues the loop until the condition is not met
    print(i) # Infinite loop
    i += 1  # adds +1 for each loop

# Exception Handling

try:
    print(10/0) # 100% Error since it is impossible
except:
    print("An error has occurred")
finally:
    print("Exception handling has finished")


"""
* EXTRA CHALLENGE (optional):
 * Create a program that prints to the console all numbers between
 * 10 and 55 (inclusive) that are even, and are neither 16 nor multiples of 3.
 *
 * If you carefully reviewed all the possibilities, you surely discovered something new.
"""

for number in range(10 , 56):
    if number % 2 == 0 and number != 16 and number % 3 != 0: # condition 1: only show evens, Condition 2: skip 16, condition 3: must be a multiple of 3 with the modulus.
         print(number) # Add double TAB