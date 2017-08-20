cities = {
	'baltimore': {
		'country': 'United States',
		'population': 10000001,
		'fact': 'high murder rate',
		},
	'paris': {
		'country': 'France',
		'population': 25,
		'fact': 'speak french',
		},
	'vienna': {
		'country': 'United States',
		'population': 34,
		'fact': 'it has a metro',
		},
	}

for city, info in cities.items():
	print('There are some facts about ' + city.title() + ':')
	for key, value in info.items():
		print(key.title() + ": " + str(value).title())
	print("\n")