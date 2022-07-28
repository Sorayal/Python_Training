# The LEGB- Rule => Order of considerung variables within different scopes
# Local, Enclosing, Global, Built-In
# commented out from inner functions to outer functions and global, constant e will be called from math library

from math import e

# e = 1

def func_1():
    # e = 0
    def func_2():
        # e = -1
        def func_3():
            # e = 10
            print(e)
        func_3()
    func_2()


func_1()
