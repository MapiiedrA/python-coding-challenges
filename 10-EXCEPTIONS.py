"""
Exceptions Exercises 
"""

try:
    print(10/0)

    my_list = [1, 2, 3, 4]
    print([1, 2, 3, 4][4])
except Exception as e:
    print(f"An error has occurred: {e} ({type(e).__name__})")

print("Hello, execution continues!")

"""
EXTRA CHALLENGE 
* Create a function capable of processing parameters, but which can also 
 * raise 3 different types of exceptions (one of them must correspond 
 * to a custom exception created by us, manually raised) in case of error.
 * - Catch all exceptions from the place where you call the function.
 * - Print the type of error.
 * - Print if no error occurred.
 * - Print that the execution has finished.
 """

class StrTypeError(Exception):
    pass

def process_params(parameters: list):

    if len(parameters) < 3:
        raise IndexError()
    elif parameters[1] == 0:
        raise ZeroDivisionError()
    elif type(parameters[2]) == str:
        raise StrTypeError("The third element cannot be a text string.")

    print(parameters[2])
    print(parameters[0] / parameters[1])
    print(parameters[2] + 5)

try:
    process_params([1, 2, "Mauricio", 4])
except IndexError as e:
    print("The number of elements in the list must be greater than two.")
except ZeroDivisionError as e:
    print("The second element of the list cannot be zero.")
except StrTypeError as e:
    print(f"{e}")
except Exception as e:
    print(f"An unexpected error has occurred: {e}")
else:
    print("No error has occurred.")
finally:
    print("The program finished without stopping.")