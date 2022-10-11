
while True:
    num = input("Eine ganze Zahl eingeben: ")

    # think of try-catch in Java
    try:
        num = int(num)
    # throws a value exception if the given input is wrong
    except ValueError:
        print("Falsches Zeichen. Eine Zahl bitte.")
    # if the input was sucessful the while loop will break here
    else:
        break

print("Eingegebene Zahl: " + num)
