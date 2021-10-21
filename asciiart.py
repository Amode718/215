drawing = input('Please pick one of the following menu of choices: \n\nHorizontal line \nVertical line \nSquare \nRectangle \nTriangle\n')

size = int(input('Please specify how big the drawing should be(Pick a number): \n'))



#Horizontal line
if drawing == 'H':
    print('* '*size)
    
#Vertical line
if drawing =='V':
    for i in range(size):
        print('* ')
    
#Square    
if drawing == 'S':
    print('* '*size)
    for i in range(size-2):
        print('* ' + ' ' *((size-2) *2) + '* ')
    print('* '*size)

    
#Rectangle    
if drawing == 'R':
    print('* '* (size * 2))
    for i in range(size-2):
        print(('* ' + ('  ' * ((size * 2) -2)) + '* '))
    print('* ' * (size*2))
    
    
#Triangle
space = 0
if drawing == 'T':
    print('\n* ')
    for i in range(size - 2):
        print('* ' +('  ' * space) +'* ')
        space += 1
    print('* ' * size)
    
else:
    print('Error')
print("Goodbye! please come again")
# Exit the program
exit(drawing)