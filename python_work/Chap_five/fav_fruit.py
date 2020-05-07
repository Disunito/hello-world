#5-7 Make a list of your favorite fruits, and then  write a series of
#independent if statements that check for certain fruits in your list.
#   -make a list of your three fav fruits and call it favorite_fruits.
#   -write five if statements. Each should check whether a certian fruit
#    is in your list. if the fruit is in your list, the if block should print a
#    statement, such as you really like bananas!

favorite_fruits = ['grapefruits', 'kiwis', 'green apples']
message = 'Eat those '

if 'red apples' in  favorite_fruits:
    print(message + 'red apples')
if 'green apples' in favorite_fruits:
    print(message + 'green apples')
if 'oranges' in favorite_fruits:
    print(message + 'oranges')
if 'grapefruits' in favorite_fruits:
    print(message + 'grapefruits')
if 'kiwis' in favorite_fruits:
    print(message + 'kiwis')
