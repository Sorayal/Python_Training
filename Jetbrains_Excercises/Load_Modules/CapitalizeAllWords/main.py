##Capitalize all words
##Write a program that takes a string, capitalizes all words in it and then prints the result. Use the capwords function from the string module.
##
##The string is already defined.
##
##
##Sample Input:
##a aaaa aaaaaaaa
##
##Sample Output:
##A Aaaa Aaaaaaaa
##



# place `import` statement at top of the program
from string import capwords

# don't modify this code or the variable may not be available
input_string = input()

# use capwords() here
print(capwords(input_string))
