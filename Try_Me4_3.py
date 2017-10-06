#
#   Joseph Owen, Block 7, File Try_Me4_3.py
#   For showing skills from 4A or something.
#
#   Note that I did not write this file using TextEdit, but Atom.
#   Additionally, I copied from my own Try Me 4-3, modified
#   to change spacing and add comments.
#

slices = ["c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10", "c11", "c12", "c13"]
#create the list of things for slicing

print("The first three items are:")
for item in slices[:3]:
    print(item)

print("The middle three items are:")
for item in slices[5:8]:
    print(item)

print("The last three items are:")
for item in slices[-3:]:
    print(item)

#print the first three, middle three and last three items using slices.



foods = ["fries", "cheeseburgers", "Ritz-brand Crackers", "Goldfish", "White rice"]
#create list of foods

theoreticalFriendFoods = foods[:]
#copy foods into the list of friend foods, creating it in doing so

foods.append("Oyster crackers")
theoreticalFriendFoods.append("Wild rice")
#append a food to my list and a different food to the theoretical friend's list

print("My favorite foods are:")
for item in foods:
    print(item)
print("My friend's favorite foods are:")
for item in theoreticalFriendFoods:
    print(item)
#print what's in my list and then the theoretical friend's list using for loops
