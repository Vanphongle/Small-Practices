def sandwich_topping(*toppings):
	print('\nAdding toppings to your sandwiches:')
	for topping in toppings:
		print(f'\t-{topping}')
sandwich_topping('ham', 'cheese', 'buns')
sandwich_topping('ham', 'cheese', 'buns')
sandwich_topping('ham', 'cheese', 'buns')
sandwich_topping('ham', 'cheese', 'buns')
 # Create a user profile function to store info of user with flexible 
def build_profile(first, last, aas, **user_info):
	user_info['first_name'] = first
	user_info['last_name'] = last
	user_info['sas'] = aas
	return user_info

user_profile = build_profile('albert', 'einstein', 'ass', field='physics', location='princeton')
#print(user_profile)

# Create a car info
def make_car(manufacture, model, **info):
	info['manufacture_name'] = manufacture
	info['model_name'] = model
	return info
car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)