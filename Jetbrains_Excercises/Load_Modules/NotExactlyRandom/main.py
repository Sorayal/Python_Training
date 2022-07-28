##Not exactly random
##Python can generate random numbers using the random module. To do that, it takes one number as a starting point (it's called seed) and then uses a formula. By default, the current system time is used as seed. However, we can set the seed manually and thus make sure that our "random" number is always the same regardless of how many times we run the program.
##
##Write a program that takes an integer number n, sets the seed to that number, and then prints a random number from -100 to 100.
##
##Use the seed and randint functions from the random module. The former takes one number and the latter takes two numbers that represent the range.
##
##The variable n is already defined.
##
##
##Sample Input:
##40
##
##Sample Output:
##17


# place `import` statement at top of the program
from random import seed
from random import randint

# don't modify this code or variable `n` may not be available
n = int(input())

# put your code here
seed(n)
print(randint(-100, 100))
