
text = """Intro Text
Willkommen zu den Datentypen in Python

1. Integer / Ganzzahlen int
2. Float / Gleitkommazahlen flaot
3. String / Zeichenkette str
4. Boolean / Wahrheitswerte bool

Der Typ 'None' ist ein besonderer Typ, 
der nichts enthaelt."""

line = 40 * "-"

print(text)
integer_number = 8
float_number = 5.6
name = 'Herbert'
isRelevant = True

print(integer_number)
print(float_number)
print(name)
print(isRelevant)

print(type(integer_number))
print(type(float_number))
print(type(name))
print(type(isRelevant))

# Datatype conversion
print(line)
print(str(integer_number))
# Every value different from 0 is considered to be true
print(bool(integer_number))
print(bool(0))

print(line)
# float -> int
print(int(2.6))

# FLoating_number -> String
print(str(85.7))
