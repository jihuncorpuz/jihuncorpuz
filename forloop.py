'''
# For Loop
print('My name is')
for i in range(5):
    print('Jihun Five Times' + str(i))

# Sum total from 0 to 100, e.g. 0+1+2+3+4+5...+100
total = 0
for num in range(101):
    total = total + num
print(total)

# While loop equivalent of For loop above
print('My name is')
i = 0
while i < 5:
    i = i + 1
    print('Jimmy Five Time' + str(i))


# For Loop with range function of 2 arguments
print('My name is')
for i in range(12, 16):
    print('Jihun Five Times' + str(i))
'''

# For Loop with range function of three argumetns
print('My name is')
for i in range(0, 10, 2): #range(5, -1, -1):
    print('Jihun Five Times' + str(i))
    