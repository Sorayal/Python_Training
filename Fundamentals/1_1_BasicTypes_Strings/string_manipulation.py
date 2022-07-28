print('Hello String')
print('She said: "I want this"')

# Escaping char
print("He said: Don\'t do that")

print("She said: Don't do that")

# Concatenate
value = "Hello, " + "Miyo"
print(value)
print("M" + "i" + "y" + "o")

# Concatenate and converting number into string
# Convert is necessary because the int value can´t be
# converted implicit
print("This costs " + str(6) + " Euro")
print("This costs " + str(5 + 6) + " Dollar")

value2 = "Hello:Miyo"
# split operation, result is an array
print(value2.split(":"))
# Performs split operation and takes the second
# value of the result array
print("My name is " + value2.split(":")[1])

name = "Paula"
print("Is name lowercased? " + str(name.islower()))

# Counts how often a sequence or char exist in a string
print(name.count("a"))

# New Line
print("first line\nsecond line")

# Raw Strings
print(r'C:\name\dir')

# String literal
s = """ 
        Test
Test-------Test
        Test
"""
print(s)

