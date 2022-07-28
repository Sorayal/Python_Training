students_room_a = int(input())
students_room_b = int(input())
students_room_c = int(input())
students_per_desk = 2


def needed_desks(students_room, students_desk):
    return students_room // students_desk + students_room % students_desk


sum_desks = needed_desks(students_room_a, students_per_desk)
sum_desks += needed_desks(students_room_b, students_per_desk)
sum_desks += needed_desks(students_room_c, students_per_desk)
print(sum_desks)
