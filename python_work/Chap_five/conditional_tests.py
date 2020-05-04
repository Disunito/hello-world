#5-1 write a series of conditional tests. Print a statement describing each
#test and your prediction for the results of each test.
#   -look closely at your results, and make sure you understand why each
#    line evaluates to true or false.
#   -Create at least ten tests. have at least five tests evaluate to true and
#    another five evalutate to false.


runners = ['decker', 'nexus_6']
decker = runners[0]
human = runners[0]
replicant = runners[1]
human_life = 80
replicant_life = 4
this = 'never'

print("\nIs 'decker' in runners? I predict True.")
print('decker' in runners)

print("\nIs human == replicant? I predict False.")
print(human == replicant)

print("\nIs human_life > replicant_life? I predict True.")
print(human_life > replicant_life)

print("\nIs replicant != runners[0]? I predict True.")
print(replicant != runners[0])

print("\nIs decker == human? I predict True.")
print(decker == human)

print("\nIs human_life <= 75? I predict False.")
print(human_life <= 75)

print("\nIs replicant_life >= human_life? I predict False.")
print(replicant_life >= human_life)

print("\nIs replicant in runners? I predict True.")
print(replicant in runners)

print("\nIs replicant_life > 75? I predict False.")
print(replicant_life > 75)

print("\nIs this == 'over'? I predict False.")
print(this == 'over')

#5-2 More conditional tests.
#   -Test using .lower()
#   -Test using 'and' and 'or' keywords
#   -Test wether an item is not in a list
