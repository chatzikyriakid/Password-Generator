import string, sys

num = list()
choice = None

# Create lists with lower and uppercase letters, numbers and symbols
lower = string.ascii_lowercase
upper = string.ascii_uppercase
punct = string.punctuation
for i in range(10):
    num.append(i)


def create_password(pass_length, user_choice):
    pass


while True:
    length = int(input('Give password length: '))
    print('\nPlease choose from the options bellow')
    print('\n1. Include lowercase characters')
    print('2. Include uppercase characters')
    print('3. Include symbols')
    print('4. Include numbers')
    print('5. Include all the above')
    print('6. Quit the program\n')
    while True:
        try:
            choice = int(input('\n'))
            if 0 < choice < 7:
                break
            else:
                print('Try again. Choice must be between 1 and 6')
                continue
        except ValueError:
            print('Please give only numbers\n')
            continue
    if choice == 6:
        sys.exit(-1)
