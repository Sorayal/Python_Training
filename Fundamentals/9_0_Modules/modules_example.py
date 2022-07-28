#Modules

'''
In Python we are able to write a long program and save as a module. This
is known as creating a script. We are able to import modules across modules
and into the Python interpreter. This negates the need to keep repeating
ourselves.
DRY!....Don't repeat yourself

Pythons standard library can be found here https://docs.python.org/3/library/

When the interpreter looks up for modules, it looks at first in the same
directory and then at built-in modules. If the interpreter can´t find the
module, an error will be raised.

You can import whole modules with "import demo_module"
or specific functions from other modules with
"from demo_module import demo_function"

Write module imports at the beginning.
'''


from functions import demo_func

def func_1(arg:int):
    x = [y for y in range(2, 10, 2)]
    x.append(arg)
    print(x)

def func_2(number:int, power:int):
    print(pow(number,power))