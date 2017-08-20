favorite_places = {
	'ian': ['beach', 'outer space', 'the moon'],
	'alex': ['place', 'there', 'thing'],
	'david': ['word', 'sleep', 'chair']
}

for person, places in favorite_places.items():
	x = person.title() + "'s favorite places are "
	for place in places:
		x += ", " + place
	print(x + ".")