
# Young and beautiful

# Read the input three times. Each one contains the age of a person – Jack's, Alex's, and Lana's. Find the youngest one among them and print this person's age.

#  Report a typo
# Sample Input 1:

# 23
# 42
# 34
# Sample Output 1:

# 23

jack_age = int(input())
alex_age = int(input())
lana_age = int(input())
print(min(jack_age, alex_age, lana_age))
