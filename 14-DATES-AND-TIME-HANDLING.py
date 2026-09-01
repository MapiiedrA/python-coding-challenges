from datetime import datetime

"""
Date exercises in Python
"""
now = datetime.now()
birth_date = datetime(1994, 8, 21, 0, 0)

print(now)
print(birth_date)

difference = now - birth_date
print(type(difference))

print(difference.days // 365)  # Years ##With integer division so the calculation is exact and without decimals.

print(f"I am {difference.days // 365} years old.")

"""
* EXTRA CHALLENGE (optional):
 * Using your birth date, format it and display the result in
 * 10 different ways. For example:
 * - Day, month, and year.
 * - Hour, minute, and second.
 * - Day of the year.
 * - Day of the week.
 * - Name of the month.
 * (whatever you can think of...)
 """

# Format 1: Day, month, and year
print(birth_date.strftime("%d %m %y")) #Inside strftime you can use any format you want, and combine it with other characters like dashes, slashes, etc. 
print(birth_date.strftime("%d %m %Y"))

# Format 2: Hour, minute, and second
print(birth_date.strftime("%H:%M:%S"))

# Format 3: Day of the year
print(birth_date.strftime("%j"))

# Format 4: Day of the week
print(birth_date.strftime("%A"))

# Format 5: Name of the month
print(birth_date.strftime("%B"))
print(birth_date.strftime("%h"))

# Default locale representation
print(birth_date.strftime("%c"))
print(birth_date.strftime("%x"))
print(birth_date.strftime("%X"))

# AM/PM
print(birth_date.strftime("%p"))