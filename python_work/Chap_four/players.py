#Useing slices of lists. Slices are indexed like lists

players = ['bear', 'eric', 'kayla', 'thom', 'cristina']

#Starts at the begining of the list of first number listed and ends before the
#second argument
print("These are my roommates:")
for player in players[0:3]:
    print(player.title())

#Using a neg. index counts from the end of the list
print("\nThese are my partners:")
for player in players[-3:]:
    print(player.title())

#This starts 3 from the front and prints to the end
print("\nThese people don't live with me:")
for player in players[3:]:
    print(player.title())

#This prints only the first and the 3rd and skips the second.
print("\nThese people knew each other years ago:")
for player in players[0:3:2]:
    print(player.title())

#this doesnt print the last three names in the list.
print("\nThese people are dating:")
for player in players[:-3]:
    print(player.title())
