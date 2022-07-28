##55 is enough
##Write a program that reads numbers until a user enters 55. Once 55 is entered, stop reading the input, print out how many numbers have been entered, their total sum, and average (do the rounding this way: round(number)). Do NOT include 55 in your calculations. Print each resulting value on a new line in the following order:
##
##how many numbers there are
##their sum
##their average: sum / the number of read numbers
##Hint
##
##
##Sample Input:
##0
##1
##2
##3
##4
##5
##6
##7
##8
##9
##10
##11
##12
##13
##14
##15
##16
##17
##55
##17
##16
##15
##14
##13
##
##Sample Output:
##18
##153
##8


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
