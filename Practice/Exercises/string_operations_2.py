password1 = "123abc"
password2 = "Pass Wort"
password3 = "ultr4g3h31m "

print(password1.upper())  # 123ABC
print(password2.lower())  # pass wort
print(password3.islower())  # True
print(password2.isupper())  # False
print(password1.zfill(8))  # 00123abc
print(password2.strip())  # "Pass Wort"
print(len(password3))  # 12
