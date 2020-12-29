import string, random, pyperclip

choices = set()
password = list()
my_pass = ''
choice = None

# Create lists with lower and uppercase letters, numbers and symbols
lower = string.ascii_lowercase
upper = string.ascii_uppercase
punct = string.punctuation
num = string.digits


# Function that creates the password by using the generated lists

def create_password(pass_length, user_choice):
    if 1 in user_choice:
        password = lower
    if 2 in user_choice:
        password = upper
    if 3 in user_choice:
        password = punct
    if 4 in user_choice:
        password = num
    if 1 and 2 in user_choice:
        password = lower + upper
    if 1 and 3 in user_choice:
        password = lower + punct
    if 1 and 4 in user_choice:
        password = lower + num
    if 2 and 3 in user_choice:
        password = upper + punct
    if 2 and 4 in user_choice:
        password = upper + num
    if 3 and 4 in user_choice:
        password = num + punct
    if 5 in user_choice:
        password = lower + upper + punct + num
    global my_pass
    for i in range(pass_length):
        my_pass += random.choice(password)
    print(my_pass)


# Requests the password length and format from the user
def request_password():
    length = int(input('Give password length: '))
    print('\nPlease choose from the options bellow')
    print('\n1. Include lowercase characters')
    print('2. Include uppercase characters')
    print('3. Include symbols')
    print('4. Include numbers')
    print('5. Include all the above')
    print('6. Exit\n')
    while True:
        try:
            choice = int(input('\n'))
            if 0 < choice < 6:
                choices.add(choice)
                continue
            elif choice == 6:
                break
            else:
                print('Try again. Choice must be between 1 and 6')
                continue
        except ValueError:
            print('Please give only numbers\n')
            continue
    create_password(length, choices)


request_password()
question = input('Do you want to copy to clipboard? y or n ')
if question.lower() == 'y':
    pyperclip.copy(my_pass)
    print('*--Copied to clipboard--*')
