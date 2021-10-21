number = int(input('Enter a non-negative number at which I should start the countdown:\n'))
print('Countdown:')
while number > 0:
  print(number)
  number -= 1 
if number == 0:
  print('Blastoff!')
if number < 0:
  print('Enter a positive number')