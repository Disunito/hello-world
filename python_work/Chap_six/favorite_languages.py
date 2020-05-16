favorite_languages = {
    'Jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'java',
}

for person, language in favorite_languages.items():
    print(f"{person.title()}'s favorite language is {language.title()}")

friends = ['phil', 'sarah']
for person in favorite_languages:
    print(f"Hi {person.title()}")
    if person in friends:
        language = favorite_languages[person].title()
        print(f"\t{person.title()}, I see you love {language}!")

if 'erin' not in favorite_languages:
    print("Erin, please take our poll")
