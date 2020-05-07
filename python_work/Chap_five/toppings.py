requested_toppings = ['mushrooms', 'onions', 'pineapple']

if requested_toppings != 'anchovies':
    print('Hold the anchovies')

for requested_topping in requested_toppings:
    if requested_topping == 'onions':
        print('Sorry, we are out of onions right now.')
    else:
        print(f'Adding {requested_topping}')

print('\nFinshed making your pizza!')
