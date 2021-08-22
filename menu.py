import downloader
import update
import user_config

def start_menu():
    print("[1] -> Download posts from a user profile")
    print("[2] -> Update all downloaded media")
    print("[3] -> Configure user login information")
    print("Input: ")

    choice = input()

    if choice == 1:
        downloader.scrap()

    if choice == 2:
        update.update()

    if choice == 3:
        user_config.config_user_data()