#3-10 Think of something you could store in a list. Write a
#program that creates a list containing these items and then
#uses each function introduced in this chapter at least once.
#

colors = []
colors.append('#FF0000')
colors.append('#4169E1')
colors.insert(0, '#7ed321')
colors.sort(reverse = True)
colors[1]= 'green'
colors.pop()
colors.append('baloo')
del(colors[0])
colors.insert(0, 'red')
colors.remove('baloo')
colors.append('blue')
colors.reverse()
print(sorted(colors, reverse = True))
print(f'{colors[1].title()} is number 1')
print(f'There are {len(colors)} colors in this list')
