duration_days = int(input())
duration_nights = duration_days - 1
cost_food_day = int(input())
cost_one_flight = int(input())
cost_one_night = int(input())
print(duration_days * cost_food_day + cost_one_flight * 2 + cost_one_night * duration_nights)
