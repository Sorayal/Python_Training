import math


# your code here
def new_math_factorial(_):
    print("Don't cheat!")


math.factorial = new_math_factorial

# don't delete this line, please
number = 23
math.factorial(number)
