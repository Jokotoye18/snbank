import random
import os
import datetime

def get_opening_balance():
    opening_balance = input('Enter the amount you wish to deposit in order to create your accout :: ')
    try:
        opening_balance = int(opening_balance)
    except ValueError:
        print('Invalid digit. Enter a digit')
        return get_opening_balance()
    else:
        return opening_balance

def get_account_type():
    keys = ['savings', 'current']
    prompt = input('Select the type of account you wish to create. Enter "savings" for savings account and "current" for current account. ')
    if prompt not in keys:
        print('Invalid key! Enter "savings" or "current".')
        return get_account_type()
    else:
        return prompt

def get_account_number():
    password = ''
    for x in range(1, 11):
        key = random.randint(0, 9)
        key = str(key)
        password += key
    return password

def get_login_time():
    now = datetime.datetime.now()
    now = now.strftime("%b-%d-%Y %H:%M")
    return now

def auth_staff():
    username = input('Enter your username :: ').strip()
    username = username.lower()
    password = input('Enter your password :: ').strip()
    password = password.lower()
    with open('staff.txt') as staff_data:
        staffs = staff_data.readlines()
        for line in staffs:
            line = line.strip().split(', ')
            if username == line[0] and password == line[1]:
                return True
        return False


def welcome():
    print('You are welcome to SNG Bank!')
    prompt = input('Enter "1" to Create new bank account, "2" to Check Account Details or "3" to Logout :: ' )
    try:
        prompt = int(prompt)
    except ValueError:
        print('You can only enter a digit, e.g "1" to Create new bank account, "2" to Check Account Details or "3" to Logout :: ')
        return welcome()
    else:
        keys = [1, 2, 3]
        if prompt not in keys:
            print('Invalid key! Ensure you enter "1, 2, 3".')
            return welcome()

        else:
            if prompt == 1:
                account_name = input('Enter your account name :: ')
                opening_balance = get_opening_balance()
                acount_type = get_account_type()
                account_mail_address = input('Enter a valid Mail address.')
                account_number = get_account_number()
                
                print(f'Account name is {account_name}')
                print(f'Account balance is {opening_balance}')
                print(f'Account type is {acount_type}')
                print(f'Account mail is {account_mail_address}')
                print(f'Account number is {account_number}')
                with open('customer.txt', 'a') as customer_file:
                    customer_file.write(f'{account_name}, {opening_balance}, {acount_type}, {account_mail_address}, {account_number}\n')
                    return welcome()


            elif prompt == 2:
                acc_number = input('Enter your account number :: ')
                with open('customer.txt') as customer_file:
                    customers = customer_file.readlines()
                    for customer in customers:
                        customer = customer.split(', ')
                        customer = (" ").join(customer).strip()
                        customer = customer.split(' ')
                        if acc_number == customer[4]:
                            print('Your account details is below :: ')
                            print(f'Account Name: {customer[0]}')
                            print(f'Account Balance: {customer[1]}')
                            print(f'Account Type: {customer[2]}')
                            print(f'Mail Address: {customer[3]}')
                            print(f'Account Number: {customer[4]}')
                            welcome()
            else:
                if os.path.exists("session.txt"):
                    print('Logged out successfully')
                    os.remove("session.txt")
                    return main()
                else:
                    pass


def main():
    prompt = input('Enter "Login" to login and "Close" to close app. :: ')
    prompt = prompt.lower()
    if prompt != 'login' and prompt != 'close':
        print('Invalid key! Ensure you enter the correct key.')
        return main()

    if prompt == 'login':
        if not auth_staff():
            print('Incorrect parameters. Try again!')
            return auth_staff()
        else:
            print('You have logged in succesfully!')
            time = get_login_time()
            with open('session.txt', 'w') as session:
                session.write(f'You have logged in successfully! Logged in time was {time}.')
            welcome()

    else:
        print('The app has been terminated.')

main()
