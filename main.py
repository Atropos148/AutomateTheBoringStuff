
birthdays = {'Alice': '1. Apr', 'Bob': '12. Dec', 'Carol': '4. Mar'}

if 'Alice' in birthdays:
    print('True')

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated')
