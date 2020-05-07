#5-3 Imagine an alien was just shot down in a game. Create variable called
#alien_color and assign it a value of 'green', 'yellow', or 'red'.
#   -write an if statement to test wether the alien's color is green. if it is,
#    print a message that the player just earned 5 points.
#   -Write one version of this program that passes the if test and another that
#    fails.(The version the fails will have no output)

points = ('5 points', '10 points', '15 points')
gp = points[0]
rp = points[2]
yp = points[1]
alien_color = 'green'


if 'red' in alien_color:
    print(rp)
if 'yellow' in alien_color:
    print(yp)
if 'green' in alien_color:
    print(gp)

#5-4 Choose a color for an alien as you did in 5-3, and write an if-else chain.
#If the alien is green 5 points, if it isnt green they earn 10 points.
#Write one version that runs the if block and one that runs the else block.

if 'green' in alien_color:
    print(gp)
else:
    print(yp)

alien_color = 'yellow'
if 'green' in alien_color:
    print(gp)
else:
    print(yp)

#5-5 Turn your else if chain from 5-4 into an if-elif-else chain.
#   -green is 5 points, yellow is 10 points and red is 15 points.
#   -Write three versions of this program, making sure each message is printed
#    for the appropriate alien.

#this kills yellow for 10 points
m = f' killed {alien_color}'
if 'red' in alien_color:
    alien_color = 'green'
    print(rp + m)
elif 'yellow' in alien_color:
    alien_color = 'red'
    print(yp + m)
else:
    alien_color = 'yellow'
    print(gp + m)

#this kills red for 15 points
m = f' killed {alien_color}'
if 'red' in alien_color:
    alien_color = 'green'
    print(rp + m)
elif 'yellow' in alien_color:
    alien_color = 'red'
    print(yp + m)
else:
    alien_color = 'yellow'
    print(gp + m)

#this kills green for 5 points
m = f' killed {alien_color}'
if 'red' in alien_color:
    alien_color = 'green'
    print(rp + m)
elif 'yellow' in alien_color:
    alien_color = 'red'
    print(yp + m)
else:
    alien_color = 'yellow'
    print(gp + m)
