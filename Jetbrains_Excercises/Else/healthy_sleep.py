
# Healthy sleep

# Ann watched a TV program about health and learned that it is recommended to sleep at least A hours per day, but oversleeping is also not healthy, and you should not sleep more than B hours. Now Ann sleeps H hours per day. If Ann's sleep schedule complies with the requirements of that TV program – print "Normal". If Ann sleeps less than A hours, output “Deficiency”, and if she sleeps more than B hours, output “Excess”.

# The input to this program is three strings with variables in the following order: A
# A
# , B
# B
# , H
# H
# . A
# A
#  is always less than or equal to B
# B
# .

# Please note the letter cases: the output should exactly correspond to what's required in the problem, i.e., if the program must output "Excess", outputs such as "excess", "EXCESS", or "ExCeSs" will not be graded as correct.

# You should carefully think about all the conditions which you need to use. Special attention should be paid to the strictness of the used conditional operators: remember the difference between \lt
# <
#  and \le
# ≤
# ; \gt
# >
#  and \ge
# ≥
# . In order to understand which ones to use, please carefully read the problem statement.

#  Report a typo
# Sample Input 1:

# 6
# 10
# 8
# Sample Output 1:

# Normal
# Sample Input 2:

# 7
# 9
# 10
# Sample Output 2:

# Excess
# Sample Input 3:

# 7
# 9
# 2
# Sample Output 3:

# Deficiency

recommended_sleep = int(input())
max_limit_sleep = int(input())
actual_sleep = int(input())

if actual_sleep < recommended_sleep:
    print("Deficiency")
elif actual_sleep > max_limit_sleep:
    print("Excess")
else:
    print("Normal")
