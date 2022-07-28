##Factorial
##Factorial of the number N is the result of the multiplication of all positive integers less than or equal to N. For example, the factorial of 3 is the product of 3, 2, 1, i.e. 3! = 3 x 2 x 1 = 6. Now, your task is to try and write a program that calculates the factorial of the input number using while loop.
##
##The input format:
##
##The number N in range from 1 to 100.
##
##The output format:
##
##The factorial N!.
##
##
##Sample Input:
##3
##
##Sample Output:
##6
##
##



n = int(input())
result = 1
while n > 0:
    result *= n
    n -= 1
print(result)
