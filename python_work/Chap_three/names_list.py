#3-1 Store the names of a few of your friends in a list called names.
#Print each person's name by accessing each element in the list,
#one at a time.

names = ['bear', 'mikey', 'eric', 'kayla', 'cristina', 'jamie']

print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])
print(names[5])

#3-2 Print a message to each name. The text of each message
#should be the same, but each message should be personalized
#with the person's name.

print(f'Would you like some tea, {names[0].title()}')
print(f'Would you like some tea, {names[1].title()}')
print(f'Would you like some tea, {names[2].title()}')
print(f'Would you like some tea, {names[3].title()}')
print(f'Would you like some tea, {names[4].title()}')
print(f'Would you like some tea, {names[5].title()}')

#3-3 Think of your favorite mode of transportation, such as a
#motorcycle or a car, and make a list that stores several examples.
#Use your list to print a series of statements about these items,
#such as "I would like to own a Honda motorcycle."

wheels = ['Black on Black', 'WarRig', 'Smoker', 'Funpolice']

print(f'I was hoping to see the {wheels[0]} this year.')
print(f'Or even watching the {wheels[1]} covered in warboys.')
print(f'Maybe even chase a few down in a {wheels[2]}')
print(f'But most of all I will miss the {wheels[3].upper()}!')
