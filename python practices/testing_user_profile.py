from user_profile import User
from privileges_admin import Privileges, Admin


thy = User('Thy', 'Le')
thy.describe_user()

thy = Admin('Thy', "Le")
thy.privileges.show_privileges()