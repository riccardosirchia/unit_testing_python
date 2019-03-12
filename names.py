from name_functions import get_formated_name

print('Enter "q" to quit the program')

while True:
	first = input("Enter your first name: ")
	if first == 'q':
		break
	last = input("Enter your last name: ")
	if last == 'q':
		break

	formatted_name = get_formated_name(first , last)

	print(formatted_name)
