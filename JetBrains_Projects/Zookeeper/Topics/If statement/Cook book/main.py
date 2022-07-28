pasta = "tomato, basil, garlic, salt, pasta, olive oil"
apple_pie = "apple, sugar, salt, cinnamon, flour, egg, butter"
ratatouille = "aubergine, carrot, onion, tomato, garlic, olive oil, pepper, salt"
chocolate_cake = "chocolate, sugar, salt, flour, coffee, butter"
omelette = "egg, milk, bacon, tomato, salt, pepper"

ingredient = input()
suffix = str("time!")

if ingredient in pasta:
    print(f"pasta {suffix}")
if ingredient in apple_pie:
    print(f"apple pie {suffix}")
if ingredient in ratatouille:
    print(f"ratatouille {suffix}")
if ingredient in chocolate_cake:
    print(f"chocolate cake {suffix}")
if ingredient in omelette:
    print(f"omelette {suffix}")
