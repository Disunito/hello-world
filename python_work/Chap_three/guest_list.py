#3-4If you could invite anyone, living or deceased, to dinner,
#who would you invite? Make a list that includes at least
#three people you'd like to invite to dinner. Then use your
#list to print a message to each person, inviting them to
#dinner.
#Marshall 4/15/20 I know this code can be written better
#but I dont want to spend to much time making it simple for
#now. I know loops would make this much better.

guest_list = ['heath ledger', 'sen no rikiu', 'Ching Shih', 'edward snowden']
print(len(guest_list))

message = '''\n\t We would like to invite you,
to a tea party and absinthe appreciation.
rsvp asap LOL.'''
print(f'Dear {guest_list[0].title()},' + message)
print(f'Dear {guest_list[1].title()},' + message)
print(f'Dear {guest_list[2].title()},' + message)
print(f'Dear {guest_list[3].title()},' + message)

#3-5 You just heard that one of the guests can't make the
#dinner, so you need to send out a new set of invitations
#You'll Have to think of someone else to invite.
#  -Add a print() call stating the guest who can't make it.
#  -Mod your list, replacing the name of the guest who cant
#    make it with the name of the new person you are inviting.
#  -print a second set of invitation messagea, one for each
#   person who is in your list.
guest_cancelled = 'edward snowden'
guest_list.remove(guest_cancelled)
new_guest = guest_list.append('john waters')
print(len(guest_list))

message = f"""\n\t We Had to send new invitations,
for our tea party and absinthe appreciation.
rsvp asap LOL.
\tSadly, {guest_cancelled.title()} can't make it."""
print(f'Dear {guest_list[0].title()},' + message)
print(f'Dear {guest_list[1].title()},' + message)
print(f'Dear {guest_list[2].title()},' + message)
print(f'Dear {guest_list[3].title()},' + message)

#3-6 You just found a bigger dinner table, so now more space
#is avaiable. Think of three more guests to invite to dinner.
#   -Add a print() call to the end of your program informing
#       people you found a bigger table
#   -use .insert() to add one new guest to the beginning,
#       middle, and end, each.
#   - print a new set of invitation messages.

guest_list.insert(0, 'thomas roberts')
guest_list.insert(2, 'kayla dickey')
guest_list.insert(6, 'cristina de ceasre')
print(len(guest_list))

message = f"""
\tWe have obtained more seats for our Tea and Absinthe appreciation.
We will have more guests Joining us soon."""

print(f"Hello again {guest_list[0].title()}," + message)
print(f"Hello again {guest_list[1].title()}," + message)
print(f"Hello again {guest_list[2].title()}," + message)
print(f"Hello again {guest_list[3].title()}," + message)
print(f"Hello again {guest_list[4].title()}," + message)
print(f"Hello again {guest_list[5].title()}," + message)
print(f"Hello again {guest_list[6].title()}," + message)

#3-7 You just found out that your new dinner table won't
#arrive in time for the dinner, and you have space for only
#two guests.
#   -Add a new line that prints a message saying that you
#       can invite only two guests
#   -use .pop() to remove guests from your list one at a
#       time until only two names remain in your list. Each
#       time you pop a name from your list, print a meassage
#       to that person letting them know you're sorry you
#       can't invite them to dinner.
#   -Print a message to each of the two people still on your
#       list, letting them know they're still invited.
#   -Use del to remove the last two names from your list,
#       so you have an empty list. Print your list to make
#       sure you actually hace an empty list at the end of
#       your program.

message = '''Due to the size of our cardboard box we will only be able to invite
two of our guests. There was a misunderstanding about the "large table"
it was for ants.'''

excused_guest = guest_list.pop()
print(f'Our apologies {excused_guest.title()},' + message)
excused_guest = guest_list.pop()
print(f'Our apologies {excused_guest.title()},' + message)
excused_guest = guest_list.pop()
print(f'Our apologies {excused_guest.title()},' + message)
excused_guest = guest_list.pop()
print(f'Our apologies {excused_guest.title()},' + message)
excused_guest = guest_list.pop()
print(f'Our apologies {excused_guest.title()},' + message)

message = "71m3 70 h4ck 7h3 w0rld, l0lz. d3l m3"
print(len(guest_list))

print(f"It's time {guest_list[0].title()}," + message)
print(f"It's time {guest_list[1].title()}," + message)
del guest_list[0]
del guest_list[0]
print(guest_list)
print(len(guest_list))
#3-9 Use len() to print a message indicating the number of
#people you are inviting to dinner. I will add this above
#to get the number of the original list.
