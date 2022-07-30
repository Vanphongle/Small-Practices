class User:
	"""Create a user class"""
	def __init__(self, first_name, last_name, location='', job=''):
		"""Initialize attribute to describe a user profile"""
		self.first_name = first_name
		self.last_name = last_name
		self.location = location
		self.job = job
		self.login_attempts = 0

	def describe_user(self):
		"""Summary of user information"""
		if self.location and self.job:
			"""Set up alternatives descripttions for user profile"""
			print(
				f'{self.first_name} {self.last_name} is a {self.job} living in {self.location}.')
		elif self.location and not self.job:
			print(
				f'{self.first_name} {self.last_name} is living in {self.location}.')
		elif self.job and not self.location:
			print(
				f'{self.first_name} {self.last_name} is a {self.job}.')
		else:
			print(f"{self.first_name} {self.last_name} doesn't have any information")

	def greet_user(self):
		"""A personalize message to greet user"""
		if self.location:
			"""Set up alternative greeting messages."""
			print(f'Hi, {self.first_name}. How are you like living in {self.location}')
		else:
			print(f'Hi, {self.first_name}')

	def increment_login_attempts(self):
		"""Set method to increment number of login attempt"""
		self.login_attempts += 1

	def reset_login_attempts(self):
		"""Reset the login attempt"""
		self.login_attempts = 0

class Privileges:
	"""privileges class"""
	def __init__(self, privileges=['can delete post', 'can add post', 'can ban user']):
		self.privileges = privileges

	def show_privileges(self):
		print(self.privileges)

class Admin(User):
	"""Create an ADmin class from user class with some privileges"""
	

	def __init__(self, first_name, last_name):
		"""initialize attributions of parent class, then admin class"""
		super().__init__(first_name, last_name)
		self.privileges= Privileges()


"""phong = User('phong', 'le', location='Lakeland', job='Gamer' )
phong.greet_user()
phong.describe_user()
phong.increment_login_attempts()
phong.increment_login_attempts()
phong.increment_login_attempts()
phong.increment_login_attempts()
phong.increment_login_attempts()
phong.reset_login_attempts()
print(phong.login_attempts)"""
phong = Admin('phong', 'le')
phong.privileges.show_privileges()