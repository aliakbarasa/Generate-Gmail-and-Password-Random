import string
import random

def create_random_gmail(length):
    char = string.ascii_letters + string.digits
    return ''.join(random.choice(char) for _ in range(length)) + '@gmail.com'

def create_random_password(length):
    char = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(char) for _ in range(length))

def generate_gmail_name_based(name, surname):
    return f'{name}_{surname}@gmail.com'

def generate_gmail_random():
    while True:
        print()
        print('''R || r : Create Random Gmail for You.\n\nD || d : Create Gmail Your Name And Surname.\n\nP || p : Create Random Password\n\nQ || q : Quit''')
        print()
        user = input('Random Or Default [r || d] / Generate Password[p] / Quit[q]: ').strip().lower()

        if user == 'q':
            return 'Exiting the program.'
        
            

        if user == 'r':
            print()
            number_user = input('Your Len Number Gmail: ').strip()
            print()
            if number_user.isdigit() and 0 < int(number_user) <= 10:
                gmail = create_random_gmail(int(number_user))
                print(25*'=')
                print(f'Your Gmail: "{gmail}"')
                print(25*'=')
                generate_password = input('Generate Password for Your Gmail [y | n]: ').strip().lower()
                print()
                if generate_password == 'y':
                    print()
                    len_pass = input('Your Len Number Password: ').strip()
                    print()
                    if len_pass.isdigit() and 0 < int(len_pass) <= 10:
                        password = create_random_password(int(len_pass))
                        print(25*'=/')
                        print(f'Your Password: "{password}"')
                        print(25*'=/')
                else:
                    print(25*'=')
                    print('Your Password: ??')
                    print(25*'=')
            else:
                print('Please Type Number Between 1-10')
        
        elif user == 'd':
            print()
            name = input('Type Your Name: ').strip()
            print()
            surname = input('Type Your Surname: ').strip()
            print()
            gmail = generate_gmail_name_based(name, surname)
            print(25*'=')
            print(f'Your Gmail: "{gmail}"')
            print(25*'=')
        
        elif user == 'p':
            print()
            len_pass = input('Your Len Number Password: ').strip()
            print()
            if len_pass.isdigit() and 0 < int(len_pass) <= 10:
                password = create_random_password(int(len_pass))
                print(25*'=')
                print(f'Your Password: "{password}"')
                print(25*'=')
            else:
                print(25*'=')
                print('Please Type Number Between 1-10')
                print(25*'=')
        
        else:
            print(25*'=')
            print('Please Type [r | d | p | q]')
            print(25*'=')

print(generate_gmail_random())
