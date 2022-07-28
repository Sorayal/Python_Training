three_digit = int(input())
decimal = 10

sum_digits = three_digit % decimal
two_digit = three_digit // decimal

sum_digits += two_digit % decimal
result = two_digit // decimal

print(sum_digits + result)
