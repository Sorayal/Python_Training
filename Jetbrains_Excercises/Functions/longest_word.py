
# Longest word

# Find the longest word in a pair and print its length.

# The variables word1 and word2 are defined for you.

# Hint

#  Report a typo
# Sample Input 1:

# Riddikulus
# Alohomora
# Sample Output 1:

# 10
# Sample Input 2:

# earthquake
# Supercalifragilisticexpialidocious
# Sample Output 2:

# 34

word_1 = input()
word_2 = input()

# How many letters does the longest word contain?
print(max(len(word_1), len(word_2)))
