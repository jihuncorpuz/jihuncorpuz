'''
# IF Condition
name = 'Jihun'
if name == 'Jihun':
    print('Hello ' + name)
print('Done')


 # IF ELSE Condition
password = 'swordfish'
if password == 'swordfish':
    print('Access granted.')
else:
    print('Wrong password.')


# ELIF Condition
name = 'Jihun'
age = 3000
if name == 'Alice':
    print('Hi Alice')
elif age < 12:
    print('You are not Alice, kiddo.')
elif age > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire.')
elif age > 100:
    print('You are not Alice, granny')
'''

print('Enter a name')
name = input()
if name: # if name != ''
    print('Thank you for entering your name: ' + name)
else:
    print('You did not enter a name.')