number = int(input())
word = input()

# write a condition for plurals
if number != 1:
    word += str("s")

print(number, word)
