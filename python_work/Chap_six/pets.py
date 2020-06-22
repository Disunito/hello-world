#6-8 Make several dictionaries where each dictionary represents a different pet.
#In each, include the Type and Owner's name. Store these in a list called pets.
#Loop through your list and as you do print everything about each pet.

#Note to self: Find a better way to output name of each animal listed.

oz = {'type': 'cat', 'owner': 'kayla', }
abadon = {'type': 'chinchilla', 'owner': 'eric', }
cookie = {'type': 'cat', 'owner': 'cristina', }

pets = [oz, abadon, cookie]

for pet in pets:
    for label, data in pet.items():
        print(f"{label.title()}: {data.title()}")
        if data == 'kayla':
            print("Name: Oz\n")
        elif data == 'eric':
            print("Name: Abadon\n")
        elif data == 'cristina':
            print("Name: Cookie\n")
