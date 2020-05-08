#5-8 Make a list of five or more usernames, including the name 'admin'.
#Imagine you are writting code that will print a greeting to each user after
#they log in to a website. Loop through the list, and print a greeting
#each other.
#   -If the username 'admin', print a special gretting, such as Hello admin,
#    would you like a status report.
#   -Otherwise, print a generic greeting, such as Hello Jaden, Thank you for
#    logging in agian.

usernames = [ 'admin', 'slutbunny', 'DooMguy', 'iKa', 'thebaron']
#usernames = []

if usernames:
    for name in usernames:
        if name == 'admin':
            print('Welcome back Admin, would you like a system report?\n')
        else:
            print(f'Welcome back {name.title()}, good to see you.\n')
else:
    print('We need more users, Dave...')

current_users = [user.lower() for user in usernames]
new_users = ['disunito', 'ikA', 'audreythorn', 'bbbenson', 'DooMguy']

for user in new_users:
    if user.lower() in current_users:
        print('Sorry, that username is taken.')
    else:
        print(f'Welcome {user.title()}!')
