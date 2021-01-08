# This is abalooter, grab your target's photos and videos posted on IG.

## Preparations
You can only download **ALL** pictures and videos from that IG account.
You must install **Instalooter** module by using: 

`pip install instalooter`

Then you have to set your log in account and passwd in login.py, like:
```
ac = 'my ig account'
passwd = 'my ig passwd'
```

### Private accounts that you have not followed are **NOT** applicable for this program

## Operation
Run the py file using:

`python main.py`

Then it will prompt for user input, enter your target ig name in the area

The program will generate a new folder, storing the posts just downloaded.

If there is/are same folder(s) exist, the program will execute update procedure.
### Tips
Copy the name directly can save your time

## Want to update the photos with only **1** command ?
First of all, open the download.txt with any text editor

Then enter you target user's IG name in a new line

For example, "hello_world" and "cuNextTime" are the users u want to download their posts, edit the .txt file like this:
```
hellow_world
cuNextTime
```

Now start the program, and enter 'update' as the input of IG username.
The program will download those new posts immediately
# ALL DONE!!!!
