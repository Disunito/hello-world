motorcycles = ['honda', 'yamaha', 'suzuki']

print(motorcycles)

motorcycles.insert(2, 'ducati')
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

#I added in 'suzuki' again to practice .insert(), and .pop().
motorcycles.insert(3, 'suzuki')
last_owned = motorcycles.pop()
first_owned = motorcycles.pop(0)

print(f'The last motorcycle I owned was a {last_owned.title()}.')
print(f'The First motorcycle I owned was a {first_owned.title()}.')

#wanted to restore my list using .append() so I could
#try out .remove() on my orginal list
motorcycles.append(last_owned)
motorcycles.append(first_owned)

print(f'\n{motorcycles}')

#Marshall 4/15/20 Finally figured out how to use \n with a variable correctly
#in conjunction with function.
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(f'\n{motorcycles}')
print(f'\nA {too_expensive.title()} is out of my budget.')
