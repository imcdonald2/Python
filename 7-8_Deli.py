sandwich_orders = ['hero', 'submarine', 'club', 'blt']
finished_sandwiches = []

while sandwich_orders:
	current_sandwich = sandwich_orders.pop()
	
	print("Your " + current_sandwich + " is ready.  Come and get it.")
	finished_sandwiches.append(current_sandwich)

print("\nThe following sandwiches have been completed:\n")
for finished_sandwich in finished_sandwiches:
	print("\t" + finished_sandwich)