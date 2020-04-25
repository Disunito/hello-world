
#4-1 Think of at least three kinds of your favorite pizza. Store these
#pizza names in a list, and then use a for loop to print the name of
#each pizza
#	-Modify your for loop to print a sentence using the name os the
#	pizza instead of printing just the name of the pizza. For each
#	pizza you should have one line of output containing a simple
#	statement like 'I like pepperoni pizza.'
#	-Add a line at the end of your program, outside the for loop, that
#	consist of the three or more lines about  the kinds of pizza you
#	like and then an additonal sentence, such as 'I really love pizza!'
#4-11 Make a copy of the list of pizzas and call it friend_pizzas.
#Then do the following:
#	-Add a new pizza to the original list
#	-Add a different pizza to the friend list
#	-Prove you have two sepreate lists

pizzas = ['supreme', 'pepperoni', 'pineapple']

for pizza in pizzas:
	print(f'The {pizza} pizza is here.')

print("""
Gah, I love pizza just, so much. So much pizza I love, Just, Gah. I love
Just pizza... MAN! DO I LOVE IT!
""")

friend_pizzas = pizzas[:]

pizzas.append('anchiove')
friend_pizzas.append('buffulo chicken')

print('My favorite pizzas are:')
for pies in pizzas:
	print(pies)
print('My friends favorite pizza is:')
for pies in friend_pizzas:
	print(pies)
