
# Variables pattern in Python <name> = <value>

name = "Maru"
age = 157

print(f"Name: {name}, Age: {age}")

# Multiple declarations and initializations
# a = 1, b = 2, c = 3
a, b, c = 1, 2, 3
print(a)
print(b)
print(c)

# swapping values without temporary variable
surname = "Temper"
lastname = "Ron"
print(f"Surname: {surname}, Lastname: {lastname}")
surname, lastname = lastname, surname
print(f"Surname: {surname}, Lastname: {lastname}")

"""Rules for Python variable naming:
- Lowercase
- starting with underscore or char, never a digit!
- valid signs: char, digit, underscore
- no keywords!
"""