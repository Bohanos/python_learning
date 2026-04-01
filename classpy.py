name = 'Bohanos'
institute = 'Jengatech'
score = 99
address = 'So estate'
price = 7000000.99
active = True

print(name)

name = input('Enter your name: ')
print('Hello,', name)
print('Hello ', name)
institute = input('Where do you study? ')
score = input('What is your score? ')
address = input('Where do you live? ')
price = input('How much did you pay? ')
active = input('Are you serious in Jengatech? ')

print('Hello ' + name + '.' + ' You study at ' + institute + '.' + ' Your score is ' + score + '.' + ' You live at ' + address
      + '.' + ' You paid ' + price + '.' + ' Your active status in jengatech is ' + active + '.') 
