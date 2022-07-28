# This asterix * shows a people array or list as parameter
# , but it is flexible
# iterates over the list and prints the person
def print_people(*people):
    for person in people:
        print("This person is", person)


print_people("Nick", "Dan", "Jack", "Linda", "King", "Smiley")
