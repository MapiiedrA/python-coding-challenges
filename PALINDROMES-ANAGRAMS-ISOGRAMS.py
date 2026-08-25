"""
EXTRA CHALLENGE (optional):
 * Create a program that analyzes two different words and performs checks
 * to discover if they are:
 * - Palindromes
 * - Anagrams
 * - Isograms
 """

def check(word1: str, word2: str):

    # Palindromes: a word, phrase, or number that reads exactly the same left to right as right to left.
    print(f"Is {word1} a palindrome?: {word1 == word1[::-1]}")
    print(f"Is {word2} a palindrome?: {word2 == word2[::-1]}")

    # Anagrams: word play that consists of changing the order of the letters of a word or phrase to create a new one.
    print(f"Is {word1} an Anagram of {word2}?: {sorted(word1) == sorted(word2)}")
    print()

    # Isograms: a line on a map or chart connecting points that have the same value, such as temperature or pressure.
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