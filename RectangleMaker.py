size = int(input("please enter size: "))
inner_size = size - 2
print ('*' * size)
for i in range(inner_size):
    print ('*' + ' ' * inner_size + '*')
print ('*' * size)