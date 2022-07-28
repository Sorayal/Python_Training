a = 1
b = 2

def func():
    c = 3
    d = a + b
    global e
    e = b + c
    f = 4
    def inner_func():
        nonlocal f
        f = 5
    inner_func()


func()

# a, b, e are globals

# a and b are defined outside of the function and are therefore considered global. e is defined inside the function with a keyword global and is therefore considered global.
# f is defined with a keyword nonlocal, which still doesn’t make a variable global. You can easily prove it by executing this code and then trying to print all the variables
# – only a, b and e can be printed without errors, the others will raise NameError.