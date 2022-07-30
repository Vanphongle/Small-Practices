prompt = '\nPlease enter pizza toppings you want to add: '
prompt += "\n(Enter 'quit' when you are finish.)"
while True:
	toppings = input(prompt)
	if toppings == 'quit':
		break
	else:
		print(f"\nAdding {toppings.upper()} to your pizza")
