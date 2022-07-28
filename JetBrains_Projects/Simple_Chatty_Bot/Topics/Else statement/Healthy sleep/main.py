recommended_sleep = int(input())
max_limit_sleep = int(input())
actual_sleep = int(input())

if actual_sleep < recommended_sleep:
    print("Deficiency")
elif actual_sleep > max_limit_sleep:
    print("Excess")
else:
    print("Normal")
