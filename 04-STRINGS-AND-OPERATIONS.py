"""
Operations 
"""
s1 = "Hello"
s2 = "Python"

# Concatenation
print(s1 + ", " + s2 + "!")

# Repetition
print(s1 * 3) 

# Indexing
print(s1[0] + s1[1] + s1[2] + s1[3])

# Length
print(len(s2))

# Slicing
print(s2[2:5])
print(s2[2:])
print(s2[0:2])
print(s2[:2])

# Search
print("a" in s1)
print("i" in s1)

# Replacement
print(s1.replace("o", "a"))

# Splitting
print(s2.split("t")) # by definition split drops the character where it splits, but it can be retrieved.

# Uppercase and Lowercase
print(s1.upper()) # upper
print(s1.lower()) # lower
print("mauricio piedra".title()) # converts the first letter of each word to uppercase
print("mauricio piedra".capitalize()) # only converts the very first letter to uppercase

# Stripping leading and trailing spaces
print(" mauricio piedra ".strip())
print(" mauricio piedra ".strip() + "@MapiiedrA")

# Searching at start and end
print(s1.startswith("Ho"))
print(s1.startswith("Py"))
print(s1.endswith("la"))
print(s1.endswith("on"))

s3 = "Mauricio Piedra @MapiiedrA"

# Position search 
print(s3.find("Piedra"))
print(s3.find("M"))
print(s3.lower().find("p")) # returns the index of the first occurrence of the letter.

# Occurrence counting
print(s3.lower().count("m")) # can pass a single character or a full word.

# Formatting
print("Greeting: {}, language: {}!".format(s1, s2)) # Replaces curly braces with variables in the order provided to format()

# Interpolation
print(f"Greeting: {s1}, language: {s2}!") # "f" indicates that everything inside curly braces is a variable

# Conversion to list of characters
print(list(s3)) # curiosity

# Converting list to string
l1 = [s1, ", ",  s2, "!"]
print("-".join(l1)) # joining criteria between quotes, can also be a space.

# Numeric conversions
s4 = "123456"
s4 = int(s4)  # for integers
print(s4)

s5 = "123456.123"
s5 = float(s5) # for decimals
print(s5)

# Various checks
s4 = "123456"
print(s1.isalnum())
print(s1.isalpha())
print(s4.isalpha())
print(s4.isnumeric())

"""
EXTRA : * EXTRA CHALLENGE (optional):
 * Create a program that analyzes two different words and performs checks
 * to determine if they are:
 * - Palindromes
 * - Anagrams
 * - Isograms
 */
 """

def check(word1: str, word2: str):

    # Palindromes: a word, phrase, or number that reads the same backward as forward.
    print(f"Is {word1} a palindrome?: {word1 == word1[::-1]}")
    print(f"Is {word2} a palindrome?: {word2 == word2[::-1]}")

    # Anagrams: word play resulting from rearranging the letters of a word or phrase to produce a new word.
    print(f"Is {word1} an Anagram of {word2}?: {sorted(word1) == sorted(word2)}")
    print()

    # Isograms: a word in which no letter occurs more than once (or occurs an equal number of times).
    print(f"Is {word1} an Isogram?: {len(word1) == len(set(word1))}")
    print(f"Is {word2} an Isogram?: {len(word2) == len(set(word2))}")

    # Test
    def isogram(word: str) -> bool:
        word_dict = dict()
        for character in word:
            word_dict[character] = word_dict.get(character, 0) + 1

        isogram_result = True
        values = list(word_dict.values())
        isogram_len = values[0]
        for word_count in values:
            if word_count != isogram_len:
                isogram_result = False
                break

        return isogram_result

    print(f"Is {word1} an Isogram?: {isogram(word1)}")
    print(f"Is {word2} an Isogram?: {isogram(word2)}")

check("radar", "pythonpythonpythonpython")   
#check("amor", "roma")