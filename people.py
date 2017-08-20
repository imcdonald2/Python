ian = {
	'first_name': 'ian',
	'last_name': 'mcdonald',
	'age': 30,
	'city': 'vienna',
	}

alex = {
	'first_name': 'alex',
	'last_name': 'gram',
	'age': 29,
	'city': 'towson',
	}

david = {
	'first_name': 'david',
	'last_name': 'kim',
	'age': 35,
	'city': 'dulles',
}

users = [ian, alex, david]

for user in users:
	print("First name: " + user['first_name'].title())
	print("Last name: " + user['last_name'].title())
	print("Age: " + str(user['age']))
	print("Location: " + user['city'].title() + "\n")