short_messages = ['Hello World', 'This is Python', 'Very nice to meet you']
complete_messages = []
def show_message(messages):
	for message in messages:
		print(message)
#show_message(short_message)

def send_message(current_messages, sent_messages):
	while current_messages:
		current_message = current_messages.pop()
		print(f'Printing Message: {current_message}')
		sent_messages.append(current_message)
send_message(short_messages[:], complete_messages)
show_message(short_messages)
show_message(complete_messages)