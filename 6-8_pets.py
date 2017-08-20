pet1 = {
	'animal': 'cat',
	'owner name': 'ian',
}

pet2 = {
	'animal': 'dog',
	'owner name': 'alex',
}

pet3 = {
	'animal': 'fish',
	'owner name': 'david',
}

pets = [pet1, pet2, pet3]

for pet in pets:
	print("Type of animal: " + pet['animal'].title())
	print("Owner: " + pet['owner name'].title() + "\n")