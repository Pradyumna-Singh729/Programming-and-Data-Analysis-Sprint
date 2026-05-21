# 3-5 Changing Guest List: You just heard that one of your guests can't make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.
# Start with your program from Exercise 3-4. Add a print statement at the end of your program stating the name of the guest who can’t make it.  Then modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting. Finally, print a second set of invitation messages, one for each person who is still in your list.
invited = ["Furina", 'King', 'Euclid', 'Euler']
print(f'Hello, {invited[0]}, you are invited to dinner!')
print(f'Hello, {invited[-3]}, you are invited to dinner!')
print(f'Hello, {invited[2]}, you are invited to dinner!')
print(f'Hello, {invited[-1]}, you are invited to dinner!')
print(f"Oh, due to some issue, {invited[2]} can't make it for the dinner today")
invited.pop(2)
invited.insert(2, 'Denia')
print('The new set of invitation letters are...')
print(f'Hello, {invited[0]}, you are invited to dinner!')
print(f'Hello, {invited[-3]}, you are invited to dinner!')
print(f'Hello, {invited[2]}, you are invited to dinner!')
print(f'Hello, {invited[-1]}, you are invited to dinner!')