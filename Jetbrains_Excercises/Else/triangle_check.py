
# Triangle or not triangle

# Read three angles given on separate input lines and check whether they form a triangle. Print the answer in the following format: "The triangle is valid!" or "The triangle is not valid!".

# Hint

#  Report a typo
# Sample Input 1:

# 1
# 2
# 3
# Sample Output 1:

# The triangle is not valid!
# Sample Input 2:

# 60
# 60
# 60
# Sample Output 2:

# The triangle is valid!

alpha = float(input())
beta = float(input())
gamma = float(input())
sum_triangle = 180

print("The triangle is valid!" if alpha + beta + gamma == sum_triangle
      else "The triangle is not valid!")
