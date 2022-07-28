half_life_days = 12

initial_quantity = float(input())
final_quantity = float(input())
current_quantity = initial_quantity
counter = 0

while current_quantity > final_quantity:
    current_quantity /= 2
    counter += 1

print(half_life_days * counter)
