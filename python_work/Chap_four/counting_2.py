#4-6 Use the third argument of the range() function to make a list
#of the odd numbers from 1 to 20. Use a for loop to print each number.

odd_numbers = [odd for odd in range(1, 21, 2)]
print(odd_numbers)

#4-7 Make a list of the multiples of 3 from 3 to 30. Use a for loop
#to print the numbers in a list.

threes = [num for num in range(3, 31, 3)]
print(threes)

#4-8 Make a list of the first 10 cubes (that is, the cube of each
#integer from 1 to 10), and use a for loop to print out the value
#of each cube.

cubes = [cube**3 for cube in range(1, 10)]
print(cubes)
