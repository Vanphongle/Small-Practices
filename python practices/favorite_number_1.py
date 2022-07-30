import json


filename = 'user_input.json'
with open(filename) as f:
	fav_num = json.load(f)
	print(fav_num)