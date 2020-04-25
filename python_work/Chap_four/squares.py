#This Shows three different ways to write all
#the squares in a range from 1 to 100
#
#We start by calling up and empty list (squares) that we will build into.
#then the range from 1-10 for the values in the list. Taking those values
# in range by the power of 2 we then .append() them to the squares list.
#
#squares = []
#for value in range(1, 11)
#    square = value ** 2
#    squares.append(square)
#
#Simplifying the above code. We set the exponents into .append().
#
#squares = []
#for value in range(1, 11):
#    squares.append(value ** 2)
#
#Simplifying even futher. We do all of our previous actions and
#store them into the list itself.
#This is an excellent example of list comprehension
squares = [value**2 for value in range(1, 11)]

print(squares)

#Within loops and lists you can also sort using min(), max() and sum()
print(min(squares))
print(max(squares))
print(sum(squares))
