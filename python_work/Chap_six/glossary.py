#6-3 Think of 5 programming words you've learned and store their names
#as keys and definition as values. Print each in a neat format.

glossary = {
    'dictionary': 'a set with key, value pairs, where each key is unique',
    'set': 'an unordered collection with no duplicate elements',
    'tuple': 'a number of values separated by commas',
    'list comprehension': 'a concise way to create lists',
    'list': 'a mutable, or changeable, ordered sequence of elements',
}

for word, definition in glossary.items():
    print(f"{word}:\n\t{definition}")
