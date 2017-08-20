favorite_languages = {
	'jen': ['python', 'ruby'],
	'sarah': ['c'],
	'edward': ['ruby', 'go'],
	'phil': ['python', 'haskell'],
	}
	
#iterate through dictionary to get items and values(which are a list which is accessed)
for name, languages in favorite_languages.items():
	print("\n" + name.title() + "'s favorite languages are:")

	#prints out each item in the list contained within the value of dictionary favorite_languages
	for language in languages:
		print ("\t" + language.title())
