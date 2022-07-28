##Copysign function
##Write a program that takes two float numbers, x and y, and prints x with the sign of y. Use the copysign function defined in the math module.
##
##Variables x and y are already defined.
##
##
##Sample Input:
##-4.09989366368886 -52.150356776140484
##
##Sample Output:
##-4.09989366368886
##



# place `import` statement at top of the program
from math import copysign

# don't modify this code or the variables may not be available
x, y = map(float, input().split(' '))
print(copysign(x, y))
