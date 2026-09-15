### ITERATIONS ###

# Exercise

# For
for i in range(1, 11):
    print(i)

# While
i = 1
while i <= 10:
    print(i)
    i += 1

# Recursion
def count_ten(i = 1):
    if i <= 10:
        print(i)
        count_ten(i + 1)

count_ten()

print("End")

"""
EXTRA DIFFICULTY (optional):
 * Write as many mechanisms as your language provides
 * to iterate over values. Are you capable of using 5? How about 10?
 */
"""

for e in [1, 2, 3 , 4]:
    print(e)

for e in {1, 2, 3, 4}:
    print(e)

for e in {1: "a", 2: "b", 3: "c", 4: "d"}:
    print(e)

for e in {1: "a", 2: "b", 3: "c", 4: "d"}.values():
    print(e)

print(*[i for i in range(1, 11)], sep="\n")

for c in "Python":
    print(c)

for e in reversed([1, 2, 3, 4]):
    print(e)

for e in sorted(["m", "o", "u", "r", "e"]):
    print(e)

for i, e in enumerate(sorted(["m", "o", "u", "r", "e"])):
    print(f"Index: {i}, value: {e}")