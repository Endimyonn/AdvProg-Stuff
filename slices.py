slices = ["c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10", "c11", "c12", "c13"]
print("The first three items are:")
for item in slices[:3]:
    print(item)

print("The middle three items are:")
for item in slices[5:8]:
    print(item)

print("The last three items are:")
for item in slices[-3:]:
    print(item)


foods = ["fries", "cheeseburgers", "Ritz-brand Crackers", "Goldfish", "White rice"]
theoreticalFriendFoods = foods[:]
foods.append("Oyster crackers")
theoreticalFriendFoods.append("Wild rice")
print("My favorite foods are:")
for item in foods:
    print(item)
print("My friend's favorite foods are:")
for item in theoreticalFriendFoods:
    print(item)
