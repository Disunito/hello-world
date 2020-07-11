avaliable_orders = ['pastrami', 'ruben', 'italian', 'club', 'veggie']
sandwich_orders = []
finished_orders = []

order_active = True

print("\n\tWelcome to Log Jammin' subs.\n")
print("Today's Menu:")
for sandwich in avaliable_orders:
	print(f"{sandwich.title()}")

while order_active:
	order = input("\nWhat kind of sandwich would you like? ")
	
	sandwich_orders = order
	
	repeat = input("Will that complete your order? (y/n)")
	if repeat == 'y':
		while sandwich_orders:
			if sandwich_orders in avaliable_orders:
				making_order = sandwich_orders.pop()
		
				print(f"Making order for {sandwhich[order].title()}.")
				making_order.append(finished_orders)
		
print("\n\t--- Order Confirmation ---")
for order, name in finished_orders.items():
	print(f"your {order.title()} is ready.")
