import string

num = list()

# Create lists with lower and uppercase letters, numbers and symbols
lower = string.ascii_lowercase
upper = string.ascii_uppercase
punct = string.punctuation
for i in range(10):
	num.append(i)

while(True):
	length = int(input('Give password length: '))
	print('\nPlease choose from the options bellow')
	print('\n1. Include lowercase characters')
	print('2. Include uppercase characters')
	print('3. Include symbols')
	print('4. Include numbers')
	print('5. Include all the above')
	print('6. Quit the program\n')
	while(True):
		try:
			choise = int(input('\n'))
			break
		except ValueError:
			print('Please give only numbers\n')
		if choise > 0 and choise < 7:
			break
		else:
			print('Try again. Choise must be between 1 and 6')
			continue
	if choise == 6:
		break
		