prompt = "\nWhat toppings would you like on your pizza?"
prompt += "\n(Enter 'quit' when you are finished) "

while True:
	topping = input(prompt)
	
	if topping == 'quit':
		break
	elif topping == 'pineapple':
		print(f"... you monster")
	else: 
		print(f"We will add {topping} to your pizza")
