'''
# While loop
spam = 0
while spam < 5:
    print('Hello world!')
    spam = spam + 1

# While loop Input Validation
name = ''
while name != 'your name':
    print('Please type your name.')
    name = input()
print('Thank you! ' + name)

# While Loop with break statement
name = ''
while True:
    print('Please type your name.')
    name = input()
    if name == 'your name':
        break
print('Thank you! ' + name)

'''

spam = 0
while spam < 5:
    spam = spam + 1
    if spam == 3:
        continue
    print('spam is ' + str(spam))