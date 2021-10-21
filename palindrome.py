#Andrei Modiga
#10-22-2020
def palindrome():
    userInput = input("Enter a string : ")
    userString = ""
    for letter in userInput:
        if letter.isalpha():
            userString += letter.lower()

    userList = list(userString)
    reverseList = list(reversed(userString))

    if userList == reverseList:
        return True
    else:
        return False

print(palindrome())

