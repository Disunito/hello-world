#6-9 Make a dictionary called favorite_places.
#Think of three names to use as keys in the dictionary, and store one to
#three favorite places for each person. Loop through the dictionary, and print
#each person's name and their favorite places.

favorite_places = {
    'god': ['haven', 'garden of eden', 'your mom'],
    'satan': ['hell', 'your mom'],
    'jesus': ['dinner tables','deserts', 'your heart'],
    }

for names, locations in favorite_places.items():
    print(f"{names.title()}'s favorite places include:")
    for location in locations:
        print(f"\t{location.title()}")
