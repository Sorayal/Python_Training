sound = "music"
n_people = int(input("Enter the amount of party people"))

# Combined version
if sound == "music" and n_people > 10:
    print("We are at the party!")

# Nested version
if sound == "music":
    if n_people > 10:
        print("We are at the party!")
