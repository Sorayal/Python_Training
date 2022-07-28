def fahrenheit_to_celsius(temp_fahrenheit):
    shift = 32
    temp_celsius = (temp_fahrenheit - shift) * 5 / 9
    return round(temp_celsius, 3)
