
# Integer arithmetic
# A complex expression

# Write a program that takes a single integer number n and then performs the following operations in the following order:

# adds n to itself
# multiplies the result by n
# subtracts n from the result
# exactly divides the result by n (that means, you need to carry out integer division).
# Then print the result of the division. The example is given below:

# 8 + 8 = 16
# 16 * 8 = 128
# 128 - 8 = 120
# 120 // 8 = 15
# The variable n is already defined.

n = int(input())
print(((n + n) * n - n) // n)
