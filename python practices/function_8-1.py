def make_shirt(size = 'large', text_message = 'i love python'):
	print(f"\nYour shirt size is {size.title()} with printed on message :'{text_message.title()}'")
make_shirt()

def get_fortmatted_name(first_name, last_name, middle_name = ''):
	full_name = f'{first_name} {last_name} {middle_name}'
	return full_name.title()
phong_le = get_fortmatted_name('phong', 'le')
print(phong_le)