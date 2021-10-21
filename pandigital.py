#Andrei Modiga
#10-22-2020
def pandigital():
    userNum = input("Enter some numbers: ")
    for num in '123456789':
        if num in userNum:
            continue
        else:
            return False
        
    return True
print(pandigital())
