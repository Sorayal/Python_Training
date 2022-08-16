a = 13
global b


def func():
    global b # without this, b would be shadow the global variable which leads to NameError
    b = a % 10


func()
print(b)
