
# Spellchecker

# Whoa! This problem requires knowledge of list collection type. If you're feeling up to the challenge, brace yourself, and good luck! Otherwise, you can skip it for now and return any time later.
# Write a simple spellchecker that tells you if the word is spelled correctly. Use the dictionary in the code below: it contains the list of all correctly written words.

# The input format:

# A single line with the "word".

# The output format:

# If the word is spelled correctly write Correct, otherwise, Incorrect.

# aa
# Sample Output 1:

# Correct

dictionary = ["aa", "abab", "aac", "ba", "bac", "baba", "cac", "caac"]
word = input()
# Tenary expression
print("Correct" if word in dictionary else "Incorrect")
