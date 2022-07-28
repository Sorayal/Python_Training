##Favor
##Carl asks you to count the sum of the first k natural numbers. Read k from the input, then add up numbers from 1 to k and print your answer.
##
##
##Sample Input:
##7
##
##Sample Output:
##28



k = int(input())
sum_k = 0
while k > 0:
    sum_k += k
    k -= 1
print(sum_k)
