# put your code here
counter = -1
number = 0
sum_numbers = 0
break_con = 55

while number != break_con:
    sum_numbers += number
    counter += 1
    number = int(input())
print(counter)
print(sum_numbers)
print(round(sum_numbers / counter))
