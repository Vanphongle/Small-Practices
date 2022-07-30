
#print(person_1['first_name'])
#(person_1['last_name'])
#print(person_1['city'])

favorite_numbers = {'Phong': (26,23,21), 'Thy': (3,6,9), 'Nhat': (20,10,23), 'Linh':(12,14,65), 'Lam': (12,55,44)}

for name, number in favorite_numbers.items():
	print(f"\n{name.upper()} favorite number is: \n\t{number}")

rivers = {'nile': 'egypt', 'hong': 'vietnam', 'mekong': 'china'}
for river, country in rivers.items():
	print(f"\nThe {river.title()} run through {country.title()}")
	

