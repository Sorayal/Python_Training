name = "John"


def change_name(new_name):
    global name # this needs to be added if you want to change the global variable.
    name = new_name


change_name("Mary")
print(name)
