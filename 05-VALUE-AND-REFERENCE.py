"""
Value and Reference
"""

# Value Data Types ### Primitive data types such as int, str, float are passed by value

my_int_a = 10
my_int_b = my_int_a
my_int_b = 20
my_int_a = 30
print(my_int_a)
print(my_int_b)

# Reference Data Types ### In Python, non-primitive data types like list, tuple, dict are passed by reference

my_list_a = [10, 20]
my_list_b = my_list_a
my_list_b.append(30)
print(my_list_a)
print(my_list_b)

# Functions with Pass-by-Value Data

my_int_c = 10

def my_int_func(my_int: int):
    my_int = 20
    print(my_int)

my_int_func(my_int_c)
print(my_int_c)

# Functions with Pass-by-Reference Data


def my_list_func(my_list: list):
    my_list.append(30)

    my_list_d = my_list
    my_list_d.append(40)

    print(my_list_d)

my_list_c = [10, 20]
my_list_func(my_list_c)
print(my_list_c)

### Extra Challenge ###
"""
Create two programs that receive two parameters each, defined previously as variables.
 * - One program receives two parameters by value, and the other receives them by reference.
 * - Inside the functions, swap their values and return them.
 * - Assign the returned values to two new variables, distinct from the originals.
 * - Finally, print the values of both the original and new variables to verify
 *   that the values were swapped in the new ones while preserving the original values in the first ones.
 """

# By Value

def value(value_a: int, value_b: int) -> tuple:
    temp = value_a
    value_a = value_b
    value_b = temp
    return value_a, value_b


my_int_d = 10
my_int_e = 20
my_int_f, my_int_g = value(my_int_d, my_int_e)

print(f"{my_int_d}, {my_int_e}")
print(f"{my_int_f}, {my_int_g}")

# By Reference

def ref(value_a: list, value_b: list) -> tuple:
    temp = value_a
    temp.append(50)
    value_a = value_b
    value_b = temp
    return value_a, value_b


my_list_e = [10, 20]
my_int_f = [20, 40]
my_int_g, my_int_h = ref(my_list_e, my_int_f)
print(f"{my_list_e}, {my_int_f}")
print(f"{my_int_g}, {my_int_h}")