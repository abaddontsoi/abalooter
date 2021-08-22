from instalooter.looters import * # import instalooter
from login import * # login.py is a file storing ur login info
import os # it works for folder operations

def scrap():
    print("Enter user name :")

    target = input() 

    looter = ProfileLooter(str(target), get_videos=True)
    looter.login(username=ac, password=passwd)
    looter.download(target) # download the whole profile with the user name just entered.