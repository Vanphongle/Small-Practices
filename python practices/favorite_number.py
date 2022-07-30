import json
user_input = input("What is your favorite number? ")
favorite_number = 'user_input.json'
with open(favorite_number, 'w') as f:
	json.dump(user_input, f)

with open(favorite_number) as f:
	fav_num = json.load(f)
	print(f'Your favorite number is {fav_num}')