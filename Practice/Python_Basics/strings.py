"""
Schlange (array of chars. indicies)
 S   c   h   l   a   n   g   e
[0] [1] [2] [3] [4] [5] [6] [7]

Also allowed, index counting reverse:
 S    c    h    l    a    n    g    e
[0] [-7] [-6] [-5] [-4] [-3] [-2] [-1]

"""

# Several methods to use the index
animal = "Schlange"
print(animal)  # animal
print(animal[3])  # l
print(animal[-7])  # c
print(animal[4:100])  # ange

# defining line
line = 40 * "-" + "\n"
print(line)

# convention
example_char = 'c'
example_string = "Wasserfall"

# length of a char and a string, using string format and len()
print(f"Length of 'c': {len(example_char)}")
print(f"Length of \"Wasserfall\": {len(example_string)}")

print(line)

# Removing whitespace from lead and trail using "".strip()
car = "  Lotus   "
print(f"Length of \"  Lotus   \": {len(car)}")
print(f"Length of \"Lotus\": {len(car.strip())}")

print(line)

# Filling Zeros at lead
# len = 6
language = "Python"

# filling empty spaces at lead with zeros, because language length
# is 6, 4 zeros will be filled here
result = language.zfill(10)
print(result)

print(line)
