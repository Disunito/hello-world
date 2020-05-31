alien_0 = {'color': 'green', 'speed': 'slow', 'points': 5}
alien_1 = {'color': 'yellow', 'speed': 'medium', 'points': 10}
alien_2 = {'color': 'red', 'speed': 'fast', 'points': 15}

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)
print('...\n')

#Store aliens here
aliens = []

#Make 30 green aliens.
for alien_number in range(30):
    new_alien = alien_0
    aliens.append(new_alien)

#Change first 3 aliens
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

#Show the first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")

#show how many aliens have been created
print(f"Total number of aliens: {len(aliens)}")
