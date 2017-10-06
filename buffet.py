buffetFoods = ("Rice", "Chicken", "Fries", "Noodles", "Watermelon")
for item in buffetFoods:
    print(item)

def modify_fail():
    buffetFoods[1] = "Sushi"


try:
    modify_fail()
except Exception:
    print("\nErrored as expectable\n")
    pass

print("Menu change!")

buffetFoods = ("Sushi", "Chicken", "Cantaloupe", "Noodles", "Watermelon")
for item in buffetFoods:
    print(item)
