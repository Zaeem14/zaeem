fruits = {
    "apple" : 130,
    "avocado" : 50,
    "banana" : 110,
    "cantaloupe" : 50,
    "pineapple" : 50,
    "grapefruit" : 60,
    "grapes" : 90,
    "honeydew melon" : 50,
    "kiwifruit" : 90,
    "lemon" : 15,
    "lime" : 20,
    "nectarine" : 60,
    "orange" : 80,
    "peach" : 60,
    "pear" : 100,
    "plums" : 70,
    "strawberries" : 50,
    "sweet cherries" : 100,
    "tangerine" : 50,
    "watermelon" : 80
    }
user_input = input("Fruit: ")
user_input_new = user_input.lower().strip()
if user_input_new in fruits :
    print ("Calories:", fruits[user_input_new])
else:
    print(end="")

