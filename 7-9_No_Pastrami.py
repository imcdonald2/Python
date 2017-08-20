sandwich_orders = ['hero', 'submarine', 'club', 'blt', 'pastrami', 'pastrami', 'pastrami']
finished_sandwiches = []

print("We are out of pastrami, sorry for the inconvenience.\n")

while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')

while sandwich_orders:
	current_sandwich = sandwich_orders.pop()
	
	print("Your " + current_sandwich + " is ready.  Come and get it.")
	finished_sandwiches.append(current_sandwich)

print("\nThe following sandwiches have been completed:\n")
for finished_sandwich in finished_sandwiches:
	print("\t" + finished_sandwich)