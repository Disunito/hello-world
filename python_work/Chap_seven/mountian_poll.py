# Empty dictionary for responses to poll
responses = {}

# Set flag to indicate that polling is active.
polling_active = True

while polling_active:
	# Prompt for the person's name and response
	name = input("\nWhat is your name? ")
	response = input("Which mountian would you like to climb someday? ")

	# Store the reponse in the dictionary
	responses[name] = response
	
	# Find out if anyone else is going to take the poll.
	repeat = input("Would anyone else like to respond? (yes/no) ")
	if repeat == 'no':
		polling_active = False

# Polling is complete. Show the results.
print("\n\t--- Poll Results ----")
for name, response in responses.items():
	print(f"{name} would like to climb {response}.")
