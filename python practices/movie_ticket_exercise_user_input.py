prompt = '\nTo check the price of the movie ticket please enter your age'
prompt += '\nEnter \'quit\' when you are done. '
status = True
while status:
	age = input(prompt)
	if age == 'quit':
		break

	age_int = int(age)
	if age_int <= 5:
		print('Your ticket cost $5')
	elif age_int <= 10:
		print('Your ticket cost $10')
	else:
		print('Your ticket cost $15')
