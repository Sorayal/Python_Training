print("Tag")
Liste = []
for i in range(10):
    try:
        Nummer = int(input("Wie lautet die Zahl: "))
        Liste.append(Nummer)
        print(Liste)
    except ValueError:
        print("Keine gueltige Eingabe")
        break

