##Half-life
##In nuclear physics, the half-life is used to describe the rate with which elements undergo radioactive decay. More precisely, it is the time required for an element to reduce in half.
##
##Let's take an isotope of Radium (Ra) called radium-223. Its half-life is about 12 days: this means that every 12 days the number of atoms reduces in half.
##
##Your program should:
##
##read the initial and the final quantity of atoms from the input.
##count how many complete half-life periods it would take for the initial number of atoms of radium-223 to become equal to or go below the final quantity. Note that the number of half-life periods should be an integer, not a float!
##multiply the number of half-life periods by 12 to convert the number of half-life periods to days.
##output the resulting number of days that it takes for the initial number of atoms to go below the final number.
##For example, the initial number of atoms is 4 and the resulting quantity is 3. After the first half-life period, the initial number will reduce to 2 atoms, which is below 3. Then, we take the number of half-life periods that have passed (1) and multiply it by the number of days that every half-life period takes (12). The output will be 12.
##
##The input format:
##
##The first line: the initial quantity of atoms (from 2 to 1,000,000).
##
##The second line: the final quantity of atoms.
##
##The output format:
##
##The number of days that it would take for radium-223 to go from the initial quantity of atoms to or below the final quantity of atoms.
##
##An example:
##
##The initial quantity is 8, the final quantity is 3. Your program output should be number 24.
##
##
##Sample Input:
##4
##3
##
##Sample Output:
##12
##
##
##Sample Input:
##835950
##139505
##
##Sample Output:
##36
##

half_life_days = 12

initial_quantity = float(input())
final_quantity = float(input())
current_quantity = initial_quantity
counter = 0

while current_quantity > final_quantity:
    current_quantity /= 2
    counter += 1

print(half_life_days * counter)
