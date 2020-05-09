alien_0 = {}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)
print(f"the alien is {alien_0['color']}.")

alien_0['color'] = 'yellow'
print(f"Now it is {alien_0['color']}.")

alien_0['speed'] = 'medium'
print(f"Original Position: {alien_0['x_position']}")

#move alien to the right.
#Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

#The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New poition: {alien_0['x_position']}")
