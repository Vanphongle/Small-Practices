# Define the letters and their corresponding point values
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# create a dictionary that maps letters to their point values
letter_to_points = {key:value for key, value in zip(letters, points)}
# add an entry for blank tiles with a point value of 0
letter_to_points[""] = 0

# Create a dictionary that maps each player to the list of words they played
players = ["player1", "wordNerd", "Lexi Con", "Prof Reader"]
words = [["BLUE", "TENNIS", "EXIT"], ['EARTH', 'EYES', 'MACHINE'], ['ERASER', 'BELLY', 'HUSKY'], ['ZAP', 'COMA', 'PERIOD']]
player_to_words = {player:word for player, word in zip(players, words)}

# Create a dictionary that maps each player to their total score
player_to_points = {}

# Define a function that takes a word as input and returns its point value
def score_word(word):
  point_total = 0
  # Convert the word to uppercase to handle lowercase input
  for letter in word.upper():
    # Look up the point value for the letter in the letter_to_points dictionary
    # If the letter is not in the dictionary, return 0
    point_total += letter_to_points.get(letter, 0)
  return point_total

# Loop through each player and their list of words, and calculate their total score
for player, words in player_to_words.items():
  player_points = 0
  for word in words:
    # Call the score_word function to calculate the point value of each word
    player_points += score_word(word)
  # Add the player's name and total score to the player_to_points dictionary
  player_to_points[player] = player_points

# Test the dictionaries and score_word function
print(player_to_points)
print(letter_to_points)
print(score_word('Brownie'))
