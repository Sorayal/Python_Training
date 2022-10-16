
# Minimum and maximum

# Imagine that your friend asked you to write a program that finds the minimum and the maximum.

# Write a program that receives two integers as its input, each number goes on a new line. The output should show:

# The biggest number in the first line
# The smallest number in the second line.
# Note that your friend might insert identical numbers! In this case, just output both given numbers on separate lines.

#  Report a typo
# Sample Input 1:

# 2
# 8
# Sample Output 1:

# 8
# 2
# Sample Input 2:

# 23
# 23
# Sample Output 2:

# 23
# 23
# Sample Input 3:

# 34
# 12
# Sample Output 3:

# 34
# 12

first = int(input())
second = int(input())
if first > second:
    print(first)
    print(second)
else:
    print(second)
    print(first)
