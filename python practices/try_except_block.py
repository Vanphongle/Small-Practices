print("Dividing number, enter 'x' to exit.")
while True:
	first_number = input("\nFirst number: ")
	if first_number == 'x':
		break
	second_number = input("Second number: ")
	if second_number == 'x':
		break
	try:
		answer = int(first_number) / int(second_number)
	except ZeroDivisionError:
		print("you cant divide by zero!!")
	else:
		print(answer)

	  