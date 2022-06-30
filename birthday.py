birthdays = {'Allice': '1 April', 'Bartek': '12 december', 'Celina': '4 mar'}
while True:
    print('Enter a name: (leave emty to end)')
    name = input()
    if name == '':
        breake

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name + '.')
    else:
        print('I do not have birthday information for ' + name +'.')
        print('What is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated.')