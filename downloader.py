from instalooter.looters import * # import instalooter
import user_config

def scrap():
    login_data = user_config.get_data()

    print("Enter user name :")

    target = input() 

    looter = ProfileLooter(str(target), get_videos=True)
    looter.login(username=login_data[0], password=login_data[1])
    looter.download(target) # download the whole profile with the user name just entered.