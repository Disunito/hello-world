#4-13 a buffet style resturant offers onlu five basic foods. Think of five
#simple foods, and store them in a tuple.
#   -Use a for loop to print each food the resturant offers.
#   -Try to modify one of the items, and make sure that Python rejects the
#    Change.
#   -The resturant changes its menu, replacing two of the items with different
#    foods. Add a line that rewrites the tuple, and then use a for loop to print
#    each of the items on the revised menu

a_menu = ('bread', 'soup', 'meat', 'cold liquid', 'hot liquid')
print("Welcome to Corporate Food, Get Stuffed:")
for food in a_menu:
    print(food.title())

#a_menu.append('something actually tasty')
#a_menu.insert('something nutritious')

a_menu = ('bread', 'something chunky', 'wood', 'cold liquid', 'hot liquid')
print("You requested more food so we changed the menu, Get double Stuffed:")
for food in a_menu:
    print(food.title())
