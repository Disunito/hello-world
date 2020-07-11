#7-5 A Movie theater sharges different ticker prices depending on a
#person's age. If <3 the ticket is free.; if =3 but >12 ticket ==10$;
#if they are <12 the ticket == 15$. Write a loop in which you ask users
#their age, and then tell them the cost of their movie ticket.

prompt_1 = "\nHello Potential Patron, would you like a ticket (y/n)? "

prompt_2 = "\nYou are now buying a movie ticket, Patron."
prompt_2 += "\nPlease enter your age or the age of your guest: "

#Number of loops till program ends
ticket_count = 3
cost = 0
kid = 10
adult = 15

while True:
	
	print(f"\nTickets left: {ticket_count}")
	print(f"Total due: ${cost}")
	
	person = input(prompt_1)
	total = f"Your Total comes to ${cost}. Pay up laddy!\n"	
	
	if ticket_count <= 0:
		print("\nWe are out of tickets, Smeg off")
		print(total)
		break
	
	elif person == 'n':
		print("\nThank you have a nice life")
		print(total)
		break
			
	elif person == 'y':
		
		patron = input(prompt_2)
		age = int(patron)
	
		if age < 3:
			print(f"\n\tThat is a free ticket, for your {age}y.o.")
			
		elif age < 12:
			print(f"\n\tThat will be ${kid} for you or your {age}y.o.")
			ticket_count += -1
			cost += 10
			
		else:
			print(f"\n\tThat will be ${adult} dollars, Patron.")
			ticket_count += -1
			cost += 15
		
	else:
		print("invalid response")

		
