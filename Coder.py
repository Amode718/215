def helper(message, shift):
    message = message.lower()
    secret = ""
    for c in message:
        if c in "abcdefghijklmnopqrstuvwxyz":
            num = ord(c)
            num += shift
            if num > ord("z"):     
                num -= 26
            elif num < ord("a"):
                num += 26
            secret = secret + chr(num)
        else:
           
            secret = secret + c
    return secret


def encrypt(message):
    return helper(message, 3)


def decrypt(message):
    return helper(message, -24)



msg = input("Your message to encode? ")
if len(msg) > 0:
  
    secret = encrypt(msg)
    print("The encoded message is:", secret)
else:
 
    secret = input("Your message to decode? ")
    if len(secret) > 0:
        msg = decrypt(secret)
        print("The decoded message is:", msg)