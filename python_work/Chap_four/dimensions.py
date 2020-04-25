#Playing with tuples
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

#this is here to show you cannot adjust or amend the value of a tuple.
#dimensions[0] = 250

print("\nOriginal dimensions")
for dimension in dimensions:
    print(dimension)

#You can reassign the variable for the tuple however
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
