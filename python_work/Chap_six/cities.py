#6-11 Make a dictionary called cities. Use the name of three cities as keys in
#your dictionary. Create a disctionary of informarion avout each city and
#include the country that the city is in, its approximate population, and one
#fact about it. the keys for each city's dictionary should be something like
# country, population, and fact. Print each name of the city and all of the
#information you have stored about it.

cities = {
    'los angeles': {
        'country': 'united states',
        'population': 3_990_000,
        'fact': "The LA coroner’s office has a gift shop",
    },

    'bergen': {
        'country': 'norway',
        'population': 271_949,
        'fact': 'bergen is known as the city of the seven mountains',
    },

    'Utashinai': {
        'country': 'japan',
        'population': 3_494,
        'fact': "Japan's smallest city by population"
    },

}

for city, data in cities.items():
    print(f'City: {city.title()}')
    for topic, info in data.items():
        if topic == 'country':
            print(f'{topic.title()}: {info.title()}')
        else:
            print(f'{topic.title()}: {info}')
    
    print('\n')
