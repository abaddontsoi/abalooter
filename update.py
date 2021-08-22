from instalooter.looters import * # import instalooter
from login import * # login.py is a file storing ur login info
import os # it works for folder operations


def update():
    with open('download.txt', 'r') as file: # read the download list called "download.txt"
        targets = file.readlines() # read all lines from the "download.txt" to array targets
        print(targets)
        for lines in targets:
            lines_str = lines.strip('\n') # import one of the lines from the "targets" array
            print(lines_str)
            if os.path.exists(lines_str): # check if the path was exits
                print("profile exists, updating media files...")
                looter = ProfileLooter(str(lines_str), get_videos=True) # load the profile with those exist
                looter.login(username=ac, password=passwd)  # log in to the ig
                                                            # the idea is to access ur frd list
                                                            # so u can download some users' profile u have followed but it is private originally


                looter.download(lines_str, new_only=True)   # download the new posts of the target profile to folder lines_str, the function will not download the posts that exist
            else:
                looter = ProfileLooter(str(lines_str), get_videos=True)
                looter.login(username=ac, password=passwd)
                looter.download(lines_str) # download all post