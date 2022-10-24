# Taking input from keyboard

a = input("Bitte geben Sie eine lange Zeichenkette ein.\n")

# prints out the whole string separated as chars from a list
print(list(a))

# counting 'a'
counter = 0
for char in list(a):
    if char == 'a':
        counter = counter + 1

# slightly different from Java which has System.out.printf("The given string contains %s a", counter);
print("The given string contains %s a" % counter)
