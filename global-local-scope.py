'''

spam = 42 #global vairable

def egg(): 
    spam = 42 #local variable

print('Some code here')
print('Some more code.')


# Code in the global scope cannot use any local variables
def spam():
    eggs = 99
    bacon()
    print(eggs)

def bacon():
    ham = 101
    eggs = 0

spam()

# Code in a local scope can access global variable.
def spam():
    print(eggs)

eggs = 42
spam()

def spam():
    eggs = 'Hello'
    print(eggs)

eggs = 42
spam()
print(eggs)
'''
def spam():
    global eggs
    eggs = 'Hello'
    print(eggs)

eggs = 42
spam()
print(eggs)