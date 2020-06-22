favorite_numbers = {
    'kayla': '42',
    'cristina': '7',
    'marshall': ['13', '4', '23'],
    'thom': '0',
    'satan': ['666', '616'],
}

#print(f"Kayla's favorite number is {favorite_numbers['kayla']}")
#print(f"Cristina's favorite number is {favorite_numbers['cristina']}")
#print(f"Marshall's favorite number is {favorite_numbers['marshall']}")
#print(f"Thom's favorite number is {favorite_numbers['thom']}")
#print(f"Satan's favorite number is {favorite_numbers['satan']}")

#this code replaces the old code. Added more numbers to the dictionary.
for person, numbers in favorite_numbers.items():
    print(f"{person.title()}'s favorite numbers include")
    for number in numbers:
        print(f"{number}")
    print("\n")
