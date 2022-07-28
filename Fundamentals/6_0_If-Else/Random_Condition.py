import random

conditions = ["Blue", "Red", "Green", "Yellow"]

while True:
    current_choice = random.choice(conditions)
    if current_choice == "Blue":
        print("Picked Blue")
    elif current_choice == "Red":
        print("Picked Red")
    elif current_choice == "Green":
        print("Picked Green")
    elif current_choice == "Yellow":
        print("Picked Yellow")
    else:
        print("Picked nothing.")
    key_input = input("Hit 'Enter' to do another round\n")
    if key_input != "":
        break

print("Have a nice day!")
