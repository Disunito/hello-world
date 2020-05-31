favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

# I.E. for key, value in Dictionary
for person, language in favorite_languages.items():
    print(f"{person.title()}'s favorite language is {language.title()}")

#Used a list to call out two different keys from the rest of the Dictionary
friends = ['phil', 'sarah']
for person in favorite_languages:
    print(f"Hi {person.title()}")
    if person in friends:
        language = favorite_languages[person].title()
        print(f"\t{person.title()}, I see you love {language}!")

if 'erin' not in favorite_languages:
    print("Erin, please take our poll")

#Used sorted() to Thank each person in alphabetical order
for person in sorted(favorite_languages.keys()):
    print(f"Thanks for taking our poll, {person.title()}")

#Added set() to sort any duplicate languages mentioned
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())
