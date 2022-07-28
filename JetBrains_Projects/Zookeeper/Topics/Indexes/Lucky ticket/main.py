# Save the input in this variable
ticket = input()

# Add up the digits for each half
first_half = int(ticket[0]) + int(ticket[1]) + int(ticket[2])
second_half = int(ticket[3]) + int(ticket[4]) + int(ticket[5])

# Thanks to you, this code will work
if first_half == second_half:
    print("Lucky")
else:
    print("Ordinary")