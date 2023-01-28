from time import sleep
from DB_func import *



        

def start_ATM():
    global user_list
    user_list = []
    user_list = load_db(user_list)
    print('Welcome to ELDE ATM\n')
    while True:
        sleep(1)
        print('What do you want to do?')
        sleep(0.3)
        print('Type: 1 - to sign up')
        sleep(0.3)
        print('Type: 2 - to log in')
        sleep(0.3)
        print('Type: 3 - to exit and turn off ATM')
        command = input()
        try:
            int_command = int(command)
            if int_command == 1:
                sign_up()
            elif int_command == 2:
                log_in()
            elif int_command == 3:
                cancel()
                break
            else:
                print('Input was not accepted. Type 1, 2 or 3 - depending on what you want to do. Please try again.')
        except:
             print('Input was not accepted. Type 1, 2 or 3 - depending on what you want to do. Please try again.')

        

def sign_up():
    print('\nCreate your user')
    sleep(1)
    print('Username:')
    type_username = input()
    sleep(1)
    print('\nPassword:')
    type_password = input()
    #print('*'*len(type_password))
    user_1 = user(type_username, type_password, 0)
    user_list.append(user_1)
    sleep(1)
    print('\nUser succesfully created')
    print('\n\n')
    

def log_in():
    sleep(1)
    print('\nUsername:')
    login_username = input()
    global login_index
    login_index = 0
    for i in range(len(user_list)):
        if login_username == user_list[i].username:
            sleep(1)
            print('\nPassword:')
            login_password = input()
            #print('*'*len(login_password))
            if login_password == user_list[i].password:
                sleep(1)
                print('Access granted')
                login_index = i
                bank_actions()
                break
            else:
                sleep(1)
                print('Wrong password')
                print('\n\n')
                break
        elif i == len(user_list)-1:
            sleep(1)
            print('This user does not exist')
            print('\n\n')

def cancel():
    save_db(user_list)
    print('\nThanks for using ELDE ATM')
    sleep(0.3)
    print('Turning off ATM ...')



def bank_actions():
    print('\nLogged into user: ',user_list[login_index].username)
    while True:
        sleep(1)
        print('What do you want to do next?')
        sleep(0.3)
        print('\nType: 1 - to check your balance')
        sleep(0.3)
        print('Type: 2 - to whitdraw cash')
        sleep(0.3)
        print('Type: 3 - to deposit money')
        sleep(0.3)
        print('Type: 4 - to log out')
        ba_command = input()
        if ba_command.isdigit():
            int_command = int(ba_command)
            if int_command == 1:
                balance()
                sleep(0.3)
            elif int_command == 2:
                whitdraw()
                sleep(0.3)
            elif int_command == 3:
                deposit()
                sleep(0.3)
            elif int_command == 4:
                log_out()
                break
            else:
                sleep(0.3)
                print('Input was not accepted. Type 1, 2, 3 or 4 - depending on what you want to do. Please try again.')
        else:
            sleep(0.3)
            print('Input was not accepted. Type 1, 2, 3 or 4 - depending on what you want to do. Please try again.')


def balance():
    print('\nYour balance is currently: ', end='')
    sleep(0.3)
    print(user_list[login_index].balance,'\n')

def whitdraw():
    print('\nHow much do you want to whitdraw?\n')
    whitdraw_amount = int(input('Type in amount you want to whitdraw: '))
    if whitdraw_amount <= user_list[login_index].balance and whitdraw_amount > 0:
        user_list[login_index].balance -= whitdraw_amount
        print(whitdraw_amount, 'sucsessfully whitdrawn. You have ', user_list[login_index].balance, 'left in your account')
    elif whitdraw_amount > user_list[login_index].balance:
        print('Insuficcient funds on account. Try to whitdraw a lower amount.')
    else:
        print('Input was not accepted. Type in the amount you want to whitdraw. Please try again.')

def deposit():
    print('\nHow much do you want to deposit?\n')
    deposit_amount = int(input('Type in amount you want to deposit: '))
    if deposit_amount > 0:
        user_list[login_index].balance += deposit_amount
        print(deposit_amount,'succsesfully deposited. You now have ', user_list[login_index].balance, 'in your account')
    else:
        print('Input was not accepted. Type in the amount you want to deposit. Please try again.')
    
def log_out():
    print('\nLogging out of user: ', user_list[login_index].username,'\n')



print('\n\n\n')
start_ATM()