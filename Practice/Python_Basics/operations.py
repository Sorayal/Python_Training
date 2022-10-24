
# Arithmetic operations <operator> <operation> <operator>
# binary operator
print(20 + 30)  # 50

# unary operator
print(-20)

# bitwise operator
print(~2)

# Huge difference between Python and Java
print(3 / 2)
# this will be calculated as float datatype in Python the same expression
# will calculated in Java as in, so the result would be 1.
# In general divisions will be calculated as float in Python with / operator.
# If you want to simulate a int division you can use //
print(3 // 2)

# But this will get 1.0 as result. Integer won´t be converted to float.
# but after the dot it´s cut.
print(3.0 // 2)

# Rounding the result
print(round(10 / 3, 2))

# Increment, Decrement
a = 20
print(a)
a += 1
print(a)

a = 20
print(a)
a -= 1
print(a)

# More operations, even when the numbers would be Integer with division, multiply and power + float the result
# becomes a float.
a = 20
print(a)
a /= 2
print(a)  # 10.0
print(a * a)  # 100.0
print(2 ** 2)

# Difference between 19/5 and 19//5
print(19/5)  # 3.8
print(19//5)  # 3 , no round when printing the integer number instead float like above

# Power , in Java there is Math.pow() for this operation
print(2 ** 4)  # 16

# Square, root of 2
print(2 ** 0.5)  # 1.41...

# Modulo, calculation of remainder
print(10 % 3)  # 1

# Boolean operations
print(20 < 4)
print(1 != 2 & 2 == 2)  # True
print(not 1 != 2 & 2 == 2)  # False
print(not (1 != 2) & 2 == 2)  # True

# eval method
print(eval("2 + 3 / 5 ** 2"))  # 2.12
