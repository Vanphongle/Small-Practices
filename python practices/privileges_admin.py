from user_profile import User

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


