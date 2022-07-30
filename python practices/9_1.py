class Restaurant:
	"""Model for Restaurant"""
	def __init__(self, restaurant_name, cuisine_type):
		"""Initialize restaurant name and cuisine type."""
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		"""Describe the restaurant information."""
		print(f'\n{self.restaurant_name} is a {self.cuisine_type} restaurant')
		
	def open_restaurant(self):
		"""Display message indicate the restaurant is open."""
		print(f'\n{self.restaurant_name} is now open')

	def set_number_served(self, customer_served):
		"""Set number of customer served to the given value"""
		self.number_served = customer_served 

	def increment_number_served(self, extra_customers):
		"""Increment the number of customer have been served"""
		self.number_served += extra_customers

# Create 2 instance of restaurant from Restaurant class
pho_79 = Restaurant("Pho 79", "Vietnamese")
dominos_pizza = Restaurant("Dominos Pizza", "Fast Food")

# Print indivicually the attribution
"""print(dominos_pizza.restaurant_name)
print(dominos_pizza.cuisine_type)
print(pho_79.restaurant_name)
print(pho_79.cuisine_type)

# Call Method of the function
pho_79.describe_restaurant()
pho_79.open_restaurant()
dominos_pizza.describe_restaurant()
dominos_pizza.open_restaurant()
print("")
print(pho_79.number_served)
pho_79.number_served = 10
print(pho_79.number_served)
pho_79.set_number_served(20)
print(pho_79.number_served)
pho_79.increment_number_served(100)
print(f"\nPho 79 serve around: {pho_79.number_served} customber a day.")"""
