students_room_a = int(input())
students_room_b = int(input())
students_room_c = int(input())
students_per_desk = 2

sum_desks_room_a = students_room_a // students_per_desk + students_room_a % students_per_desk

sum_desks_room_b = students_room_b // students_per_desk + students_room_b % students_per_desk

sum_desks_room_c = students_room_c // students_per_desk + students_room_c % students_per_desk
sum_desks = sum_desks_room_c + sum_desks_room_b + sum_desks_room_a

print(sum_desks)