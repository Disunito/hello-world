#3-8 Think of at least five places in the world you'd like to
#visit.
#   -Store the locations in a list. Make sure the list is not
#       in alphabethical order.
#   -Print your list in its original order. Don't worry about
#       printing the list neatly, Just print it raw.
#   -use sorted() to print your list alphabethically
#   -show that your list is still in orginal order
#   -use sorted() to reverse your list and print
#   -show that your list is still in orginal order
#   -Use reverse() to change the order of your list. Print it
#   -Use reverse() to change it back. Print it
#   -use sort() to change your list so it's stored
#       alphabethically. Print it
#   -use sort() to change  your list in reverse alphabetical
#       order. Print it.

places = ['hong kong', 'bergen', 'yosemite', 'reykjavík', 'seattle']

print(places)
print(sorted(places))
print(places)
print(sorted(places, reverse = True))
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.sort(reverse = True)
print(places)
