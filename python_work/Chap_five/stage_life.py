#5-6 Write an if-elif-else chain the determines a person's stage of life.
#Set a value for the variable age, and then:
#   -less then 2yo print baby
#   -least 2to less 4yo, print toddler
#   -least 4yo less 13yo, print kid
#   -least 13yo less 20 yo, print teen
#   -least 20yo less 65yo, print adult
#   -least 65yo print elder

current_age = 32

message = "You are currently a"
if current_age < 2:
    print(message + ' baby.')
elif current_age < 4:
    print(message + ' toddler.')
elif current_age < 13:
    print(message + ' kid.')
elif current_age < 20:
    print(message + ' teen.')
elif current_age < 65:
    print(message + ' adult. FUCK.')
else:
    print(message + ' elder.')
