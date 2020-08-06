#Make a list called sandwich_orders and fill it with the names of various
#sandwiches. Then make an empty list called finished_sandwiches. Loop through
#the list of sandwich orders and print a message for each order, such as I made
#your tuna sandwich. As each sandwich is made, move it to the list of
#finished sandwiches. After all the sandwiches have been made print a message
#listing each sandwich that was made.

sandwich_orders = ['pastrami', 'club', 'pastrami', 'blt', 'tuna', 'pastrami']
finished_sandwiches = []

print("--- Order ---")
for order in sandwich_orders:
    print(f"\t{order.title()}")

print("\nSorry, we are out of pastrami.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    prepared_sandwich = sandwich_orders.pop()

    print(f"\nWe are Making: {prepared_sandwich.title()} sandwich")
    finished_sandwiches.append(prepared_sandwich)

print("\n---Finished Order---")
for sandwich in finished_sandwiches:
    print(sandwich.title())

print("\n")
