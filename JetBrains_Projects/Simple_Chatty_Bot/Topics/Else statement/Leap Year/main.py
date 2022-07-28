# put your python code here
year = int(input())
secular = 400

if year % 4 == 0 and year % 100 != 0:
    print("Leap")
elif year % secular == 0:
    print("Leap")
else:
    print("Ordinary")

# isLeap = year % 4 == 0 and year % 100 != 0 or year % secular == 0
# if isLeap:
#     print("Leap")
# else:
#     print("Ordinary")
