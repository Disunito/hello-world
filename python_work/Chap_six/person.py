#6-1 Use a dictionary to store information about a person you know.
#Store their first, Last name, age, and CIty they live in. you should
#Print each peice of information stored.

disunito = {
    'first_name': 'harvey',
    'last_name': 'swick',
    'age': 32,
    'city': 'los angeles',
}

audrey_c = {
    'first_name': 'audrey',
    'last_name': 'coffins',
    'age': 35,
    'city': 'los angeles'
}

tunaslurp = {
    'first_name': 'scott',
    'last_name': 'dickey',
    'age': 64,
    'city': 'seattle',
}

people = (disunito, audrey_c, tunaslurp)

for person in people:
    for info in person:
        print(f"\nName: {'last_name'.title()}, {'first_name'.title()}")
        print(f"Age: {'age'}")
        print(f"Location: {'city'.title()}"


