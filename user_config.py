import os.path

def user_data_exit():
    if not (os.path.isfile('logindata.txt') and os.path.getsize('logindata.txt') != 0):
        print('No login data found')
        print('Creating new profile...')
        config_user_data()
        
def get_data():
    with open('logindata.txt', 'r') as data:
        user_data = data.readline().split(':')
        # print(user_data)

        return user_data

def config_user_data():
    # print('You are required to enter all login information again. ')
    print('Enter your user name: ')
    user_ac = input()
    print('Enter your password: ')
    user_pwd = input()

    with open('logindata.txt', 'w+') as f:
        dataset = user_ac + ":" + user_pwd
        f.write(dataset)
        f.close()