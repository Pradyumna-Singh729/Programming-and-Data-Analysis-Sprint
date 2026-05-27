# 5-9 Checking Usernames: Do the following to create a program that simulates how websites ensure that everyone has a unique username.
# Make a list of five or more usernames called current_users.
# Make another list of five usernames called new_users. Make sure one or two of the usernames are also in the current_users list.
# Loop through the new_users list to see if each new username has already been used. If it has, print a message that the person will need to enter a new username. If a username has not been used, print a message saying the username is available.
# Make sure your comparison is case insensitive. If 'John" has been used, 'JOHN' should not be accepted. (To do this, you'll need to make a copy of current_users containing the lowercase version of all existing users.)

current_users = ['JOHNpork', 'lirililarila', 'Sattire', 'buttery', 'wheytheDESTROYER', 'loserthecat']
new_users = ['gorilla', 'JohnPork', 'loserthecat', 'larpy', 'PythonWorld']

lower_current_users = []

for current_user in current_users:
    lower_current_users.append(current_user.lower())

for new_user in new_users:
    if new_user.lower() in lower_current_users:
        print(f"The username {new_user} is already taken, please enter a new username")
    else:
        print(f"The username {new_user} is available")

