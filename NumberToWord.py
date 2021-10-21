#Andrei Modiga
def words_from_number(num,join=True):
    """
    #test the numbers
    >>> words_from_number(5)
    'five'
    >>> words_from_number(6)
    'six'
    >>> words_from_number(454345345100)
    'four hundred fifty-four billion three hundred forty-five million three hundred forty-five thousand one hundred'
    """
  
    ones = ['','one','two','three','four','five','six','seven','eight','nine']
    

    two_digits = ['','eleven','twelve','thirteen','fourteen','fifteen','sixteen', \
             'seventeen','eighteen','nineteen']
    
    tens = ['','ten','twenty','thirty','forty','fifty','sixty','seventy', \
            'eighty','ninety']

 
    tenpower = ['',' thousand',' million',' billion',' trillion',' quadrillion', \
                 ' quintillion',' sextillion',' septillion',' octillion', \
                 ' nonillion',' decillion',' undecillion',' duodecillion', \
                 ' tredecillion',' quattuordecillion',
                 ' quindecillion']
    
    wordsnumber = []
    if num == 0: wordsnumber.append('zero')
    else:
        numStr = '%d'%num
        numStrLen = len(numStr)

        groups = int((numStrLen+2)/3)

        numStr = numStr.zfill(groups*3)
        
        finalCount = groups * 3
        counter = 0
        for i in range(0,groups * 3,3):
            hundred = int(numStr[i])
            ten = int(numStr[i+1])
            one = int(numStr[i+2])
            g = groups-int(i/3+1)
            counter += 1

            if hundred >= 1:
                
                wordsnumber.append(ones[hundred])
                
                if finalCount == counter:
                    wordsnumber.append(" hundred")
                else:
                    wordsnumber.append(" hundred ")
                
            if ten > 1:
                
                if one == 0:
                    wordsnumber.append(tens[ten])
                else:
                    wordsnumber.append(tens[ten]+"-")
                
                if one >= 1:
                    
                    wordsnumber.append(ones[one])
                
            elif ten == 1:
                
                if one >= 1:
                    
                    wordsnumber.append(two_digits[one])
                
                else:
                    
                    wordsnumber.append(tens[ten])
                
            else:
                
                if one >= 1:
                    
                    wordsnumber.append(ones[one])

            if (g >= 1) and ((hundred+ten+one) > 0): wordsnumber.append(tenpower[g]+" ")
    words = ''.join(wordsnumber)
    return words.strip()
print(words_from_number(454345345100))



if __name__ == "__main__":
    import doctest
    doctest.testmod()


