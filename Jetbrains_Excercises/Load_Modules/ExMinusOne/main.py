##E ** x minus one
##Write a program that takes an integer x and prints e (a mathematical constant) raised to the power of x, minus one. Here's the formula: (ex−1).
##
##Use the function expm1() defined in the math module. To do so, read its documentation carefully.
##
##The variable x is already defined.
##
##
##Sample Input:
##70
##
##Sample Output:
##2.515438670919167e+30
##

# place `import` statement at top of the program
from math import expm1

# don't modify this code, otherwise, `x` may not be available
x = int(input())

# use expm1() here
print(expm1(x))
