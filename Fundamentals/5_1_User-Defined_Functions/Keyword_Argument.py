def print_something(name="Someone", age="Unknown"):
    print("My name is", name, "and my age is", age)


# setting None as first argument
# None is equivalent to Null in other languages like Java
print_something(None, 28)

# age is a keyword argument here
print_something(age="45")
print_something(age="45", name="Ella")
