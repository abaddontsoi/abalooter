import os

def get_dir_name():
    remove_list = ['.git', '.idea', '__pycache__']
    all_dir = os.scandir()
    dir_list = []
    for d in all_dir:
        if d.is_dir():
            dir_name = d.path.split('.\\')[1]
            #print(dir_name)
            dir_list.append(dir_name)
            # print(list(dir_list))
            
    for s in remove_list:
        try:
            dir_list.remove(s)
        except ValueError:
            pass
    
    # print(dir_list)
    return dir_list


# print(get_dir_name())
