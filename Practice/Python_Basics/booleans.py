# testing boolean functions
print("19 > 10 = %s" % (19 > 10))

# four linebreaks
print(4 * "\n")


# Testing with values if Not(a and b) = Not a or Not b
# a = True
# b = True

# printing multiple arguments
# print("a = %s , b = %s" % (a, b))
# print("Not(a and b) : %s" % (not(a and b)))
# print("Not a or Not b : %s" % (not a and not b))
# print("Not(a and b) = Not a or Not b : %s" % (not(a and b) == (not a and not b)))

def check_equality(first, second):
    print("a = %s , b = %s" % (first, second))
    print("Not(a and b) : %s" % (not (first and second)))
    print("Not a or Not b : %s" % (not first and not second))
    print("Not(a and b) = Not a or Not b : %s" % (not (first and second) == (not first and not second)))
    print("\n")


# Testing with values if Not(a and b) = Not a or Not b
a = True
b = True
check_equality(a, b)

a = True
b = False
check_equality(a, b)

a = False
b = True
check_equality(a, b)

a = False
b = False
check_equality(a, b)

# Something different between Java and Python when compare Strings
# In Java you have to use equals method to compare strings values, with == it compares only the references there.
# In Python, you can use == to compare the string values

firstName = "Paula"
secondName = "Paula"

print(firstName == secondName)

# The XOR operator
# W & W = False
# W & F = True
# F & W = True
# F & F = False

a = True
b = True
print("a = %s , b = %s" % (a, b))
print("XOR: a or exclusive b are true : %s" % (a ^ b))
