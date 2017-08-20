active = True
while active:
	age = input("What is your age?  Please enter a number.\n")
	age = int(age)
	if age < 3:
		print("Your ticket is free.")
	elif age >= 3 and age <= 12:
		print("Your ticket cost is $10.")
	elif age > 12:
		print("Your ticket cost is $15.")
	else:
		break