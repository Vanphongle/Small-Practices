guess_list = 'guess.txt'
while True:
	guess_name = input(
		"\nPlease enter your name to join our guess list. \nEnter 'x' to exit. ")
	if guess_name == 'x':
		break
	answers = input("why do you like programming? ")
	if answers == 'x':
		break
	else:
		with open(guess_list, 'a') as file_object:
			file_object.write(f'{guess_name.title()}\n')
			file_object.write(f'{guess_name.title()} like programming because it {answers}.')
		print(f"Welcome to our guess list {guess_name.title()}!")

