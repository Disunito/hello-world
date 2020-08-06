menu = ['ruben', 'italian', 'club', 'veggie']
sandwich_orders = ['pastrami', 'club', 'pastrami', 'pastrami', 'veggie']
finished_orders = []

order_active = True

# States what the aviable choices are.
print("\n\tWelcome to Log Jammin' subs.\n")
print("Today's Menu:")
for item in menu:
	print(f"\t-{item.title()}")

# Take order and place order in sandwich_orders.
while sandwich in sandwich_orders:
	sandwich = sandwich_orders.pop()
	if sandwich in menu:
		print(f"We will get that {sandwich.title()} ready for you.")
		finished_orders.append(sandwich)
	else:
		print(f"we are currently not serving {sandwich.title()}.")

# Prints out The finished order
print("\n\t--- Order Confirmation ---")
for order_up in finished_orders:
	print(f"your {order.title()} is ready.")
