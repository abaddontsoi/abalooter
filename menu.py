import downloader
import update
import user_config
import walk_file

def start_menu():
    user_config.user_data_exit()
    file_list = walk_file.get_dir_name()
    update.update_list(file_list)

    print("[1] -> Download posts from a user profile")
    print("[2] -> Update all downloaded media")
    print("[3] -> Configure user login information")
    print("Input: ")

    choice = input()

    if choice == "1":
        downloader.scrap()

    if choice == "2":
        update.update()

    if choice == "3":
        print('You are required to enter all login information again. ')
        user_config.config_user_data()