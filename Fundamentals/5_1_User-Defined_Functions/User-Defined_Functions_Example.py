# Defining function with snake_case
def my_function():
    print("This is my function")
    print("This is a second string")


# Using arguments
def my_second_function(first_str, second_str):
    print(first_str)
    print(second_str)


# Default arguments
def print_something(name="Someone", age="Unknown"):
    # Using commas
    print("My name is ", name, " and my age is ", age)


# Outside the function now
# Calling function
my_function()
print("\n\n")
my_second_function("First argument", "Second argument")
print_something("Nick", str(27))

# Calling with default arguments
print_something()
