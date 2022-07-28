# write your code here
print('''
XOX
OXO
XXO''')


def print_playground():
    print(f'''
    ---------
    | {cells[0]} {cells[1]} {cells[2]} |
    | {cells[3]} {cells[4]} {cells[5]} |
    | {cells[6]} {cells[7]} {cells[8]} |
    ---------''')


cells = input('Enter cells: ')
print_playground()
