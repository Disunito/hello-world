##Use a variable to represent a person's name, and print
#a message to that person. Your message should be simple,
#such as "Hello Eric, would you like to learn some python?"

name = "Mikey"
print(f"""
You can bounce off your boy's dick all day long {name},
but you still gotta get those weeds.
""")
#Use a variable to represent a person's name, and print
#thst prerson's name in lowercase, uppercase, and title case.

first_name = name
last_name = "Boyce"
full_name = f"{first_name} {last_name}"
print(full_name.lower())
print(full_name.upper())
print(f'{full_name.title()}\n')

#Find a quote from a famous person you admire. Print the
#quote and the name of its author. Your output should look
#something like the following, including the quotation marks:
#   Albert Einstein once Said, "A person who never made a
#       mistake never tried anything new."

print('''
Kakuzo Okakura was said to say “Those who cannot feel the littleness of
great things in themselves are apt to overlook the greatness of little things
in others.”
''')

#Repeat the last exercise, but this time, represent the famous
#person's name using a variable called famous_person. Then
#compose your message and represent it with a new variable
#called message. Print your message.

famous_person = "Kakuzo Okakura"
print(f'''{famous_person} was said to say “Those who cannot feel the littleness
of great things in themselves are apt to overlook the greatness of little things
in others.”\n''')

#   Use a variable to represent a person's name, and include
#some whitespace characters at the beginning and end of the name.
#Make sure you use each character combination, "\t" and "\n",
#at least once.
#   Print the name once, so the whitespace around the name
#is displayed.Then print the name using each of the three
#stripping functions, lstrip(), rstrip(), and strip().
name = " Rammstein "
print(f"""Let me see you stripped '{name}':\n\t'{name.rstrip()}'
    \t'{name.lstrip()}'\n\t'{name.strip()}'""")
