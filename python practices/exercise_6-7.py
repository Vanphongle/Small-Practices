persons = {'ThyLe' : {'first_name': 'Thy', 'last_name': 'Le', 'city': 'Lakeland'},
'TyLa' : {'first_name': 'Ty', 'last_name': 'La', 'city': 'Lakeland'},
'HyUl' : {'first_name': 'hy', 'last_name': 'ul', 'city': 'Lakeland'}
}
for name, info in persons.items():
	print(f'\nName: {name}')
	full_name = f"{info['first_name']} {info['last_name']}"
	location = info['city']
	print(f'\tFull Name: {full_name.title()}')
	print(f'\tLocation: {location.title()}')
pets = {
	'dog': {'kind': 'yorkie', 'owner_name': 'Thy'},
	'cat': {'kind': 'yellow', 'owner_name': 'lol'}
}
for pet, pet_info in pets.items():
	print(f'\nType of pet: {pet.title()}')
	kind_of_pet = pet_info['kind']
	pet_owner_name = pet_info['owner_name']
	print(f'\tPet kind: {kind_of_pet.title()}')
	print(f'\tOwner Name: {pet_owner_name.title()}')

favorite_places = {
'Julia':('England', 'Australia', 'iceland'),
 'alex': ('united states', 'germany', 'france'),
 'tom': ('Egypt', 'argentina', 'brazil')}
for name_1, place_1 in favorite_places.items():
 	print(f'\n{name_1.title()} favorite places are: {place_1[0].title()}')

cities = {
	'miami':{'country': 'usa', 'population': 3, 'fact': 'boring'},
	'ho chi minh':{'country': 'vietnam', 'population': 10, 'fact': 'fun'},
	'paris':{'country': 'france', 'population': 7, 'fact': 'ok'}
}

for city, city_info in cities.items():
	print(f'\nCity name: {city.title()}')
	country_origin = city_info['country']
	population_of_city = city_info['population']
	fun_fact = city_info['fact']
	print(f'\tLocated in {country_origin} with population of {population_of_city}millions people ')
