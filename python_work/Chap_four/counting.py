#4-3 Use a for loop to print the numbers from 1 to 20, inclusive.
numbers = [number for number in range(1, 21)]
print(numbers)

#4-4 Make a list of the numbers from one to one million, and then
#use a for loop to print the numbers.(if the output is taking too
#long, stop it by pressing CTRL-C or by closing the output window)

millions = [num for num in range(1, 10**6+1)]
print(millions)

#4-5  make a list of the numbers from one to one million, and
#then use min() and max() to make sure your list actually starts
#at one and ends one million. Also, use the sum() function to see
#how quickly Python can add a million numbers.

print(f"\n{min(millions)}, \n{max(millions)}, \n{sum(millions)}")


print(millions[0:3])
print(millions[499_998: 500_001])
print(millions[-3:])
