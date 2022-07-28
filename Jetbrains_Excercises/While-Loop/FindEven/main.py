##Find even
##Write a program that takes number N as input and prints all positive even numbers less than this input number. Please, use the while loop for that.
##
##The input format:
##
##The maximum number N (varying from 1 to 200).
##
##The output format:
##
##All positive even numbers that are less than N. Print them in the ascending order. Each number must be on a separate line.
##
##
##Sample Input:
##8
##
##Sample Output:
##2
##4
##6


number = int(input())
counter = 1
while counter < number:
    if counter % 2 == 0:
        print(counter)
    counter += 1
