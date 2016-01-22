#! python3
# strongPassword.py - checks if your password is strong

import re


# start
print("Welcome to Password Checker")
print('Strong password has:')
print(' at least 8 characters')
print(' both lower and uppercase characters')
print(' at least one number')

while True:
    length = 0
    print('')
    print("Type in your password to check if it is strong:")
    password = input('')
    if password == '':
        break
    print('Your password:')
    # check how long PW is
    passwordLengthRX = re.compile(r'[\d\w]+?')
    for match in passwordLengthRX.findall(password):
        length += 1

    if length < 8: print(' is shorter than 8 characters.')
    elif length == 8: print(' has 8 characters.')
    else: print(' is ' + str(length) + ' characters long.')

    # check for lowercase and UPPERCASE characters
    lowerCaseCheckRX = re.compile(r'[a-z]')
    upperCaseCheckRX = re.compile(r'[A-Z]')

    lowerCaseCheck = lowerCaseCheckRX.search(password)
    upperCaseCheck = upperCaseCheckRX.search(password)

    lowerAndUpper = '  has both upper and lowercase characters.'
    if lowerCaseCheck and upperCaseCheck:
        print(lowerAndUpper)

    else:
        if lowerCaseCheck: print('  has only lowercase characters.')
        if upperCaseCheck: print('  has only uppercase characters.')

    if not lowerCaseCheck or upperCaseCheck:
        print('  has no letters. What?')

    # check for numbers
    numbersCheckRX = re.compile(r'\d')
    numbersCheck = numbersCheckRX.search(password)
    if numbersCheck:
        print('   has a number in it.')
    else:
        print('   does not have a number in it.')
