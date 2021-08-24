# This is abalooter, grab your target's photos and videos posted on IG.

## Preparations
THIS PYTHON PROGRAM IS ONLY AVAILABLE ON WINDOWS AT THIS TIME
You can only download **ALL** pictures and videos from that IG account.
You must install **Instalooter** module by using: 

`pip install instalooter`

For the first time of using the application, it will ask you entering your Instagram account and password.

Those login data will be stored in `logindata.txt`, in the form of:

```
instagram_account:password
```

Private accounts that you have not followed are **NOT** applicable for this program

## Operation
Run the py file using:

`python main.py`

The program first of check your login data in `logindata.txt`, if the file dosen't exists or size == 0, it starts configure progress.

```
No login data found
Creating new profile...
Enter your user name:
```

The Application offers 3 option of operation, the first one is downloading profiles one-by-one, user should enter "1" to continue.

Those downloaded media will be stored in a folder that named as Instagram user name

```
[1] -> Download posts from a user profile
[2] -> Update all downloaded media
[3] -> Configure user login information
Input:
1
Enter user name :
testing
```

The second function is to update all downloaded profiles, in other words, gaining all new media they've post and you haven't get yet.

```
Input:
2
'target_user_name'
profile exists, updating media files...
```

Last function of the application is to reset your login data, it will be useful when you changed your own password.

```
Input:
3
You are required to enter all login information again.
Enter your user name:
test_ac_user_name
Enter your password:
test_ac_user_password
```

