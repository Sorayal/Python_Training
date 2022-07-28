# This is about classes in general

# example
class Dog:
    # placeholder, prevents that an error will be thrown
    # pass

    # Class attribute
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age


# Creating instance of Dog
x = Dog("Rex", 20)
print(x.__str__())
print(x.name)

y = Dog()
