from my_main_script import coffee_bot

def test_coffee_bot():
    # Simulate user input
    user_input = ['l', 'a', 'n', 'y']
    
    # Simulate expected output
    expected_output = [
        'Alright, that\'s a large latte!',
        'Would you like to order another drink? (y/n) ',
        'Okay, so I have:',
        '- large latte',
        'Can I get your name please? \n> ',
        'Thanks, N! Your order will be ready shortly.'
    ]
    
    # Override input() to simulate user input
    def mock_input(prompt):
        return user_input.pop(0)
    
    # Override print() to capture output
    captured_output = []
    def mock_print(message):
        captured_output.append(message)
    
    # Run the function
    coffee_bot(input=mock_input, print=mock_print)
    
    # Check the output
    assert captured_output == expected_output
