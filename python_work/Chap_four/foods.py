my_foods = ['pizza', 'ramen', 'sandwiches']
friend_foods = my_foods[:]

my_foods.append('tears')
friend_foods.append('your mom')

print("My favorite foods are:")
for food in my_foods:
    print(food)

print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print(food)


#my_foods = friend_foods will not work to make a copy of the list.
#This essintially makes the same list that can be called two different ways
