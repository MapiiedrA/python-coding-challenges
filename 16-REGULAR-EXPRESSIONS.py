### REGULAR EXPRESSIONS ###
import re

"""
Exercise
"""

def find_numbers(text:str) -> list:
    return re.findall(r"\d+", text) 

print(find_numbers("This is exercise 16 published on 16/9/2026."))

### EXTRA ###
"""
EXTRA DIFFICULTY (optional):
 * Create 3 regular expressions (at your discretion) capable of:
 * - Validating an email.
 * - Validating a phone number.
 * - Validating a URL.
 */
"""

def validate_email(email: str)-> bool:
    return bool(re.match(r"^[\w.+-]+@[\w]+\.[a-zA-Z]+$", email)) # \ is used to escape outside the range

print(validate_email("mapiedra3223@gmail.com"))

def validate_phone(phone: int)-> bool:
    return bool(re.match(r"^\+?[\d\s]{3, }$", phone))

validate_phone("+506 456 411")

def validate_url(url: str)-> bool:
    return bool(re.match(r"^http[s]?://(www.)?[\w]+\.[a-zA-Z]+$", url))

print(validate_url("https://github.com"))