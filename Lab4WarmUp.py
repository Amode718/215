#LAB 4 Warmup

#Andrei Modiga
#09-24-2020
def is_pangram(sentence):
    '''takes a string and returns a Boolean 
    indicating whether that sentence is a pangram
    https://examples.yourdictionary.com/reference/examples/examples-of-pangrams.html
    >>> is_pangram("How vexingly quick daft zebras jump!") 
    True
    >>> is_pangram("Jackdaws love my big sphinx of quartz.")
    False
    >>> is_pangram("")
    
    '''
    alphabet="abcdefghijklmnopqrstuvwxyz"

    for b in alphabet:
        if b not in sentence.lower():
            return False
    return True

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose = True)
    
# Andrei Modiga
# 09-22-2020
def are_anagrams(word1, word2):
    '''takes two strings and returns a Boolean indicating
    whether the strings are anagrams of each other
    >>> are_anagrams("", "")
    
    >>> are_anagrams("ton", "Not")
    True
    >>> are_anagrams("tar", "rat")
    False
    '''
    list_word1 = list(word1.lower()) 
    list_word1 = sorted(list_word1)
    list_word2 = list(word2.lower()) 
    list_word2 = sorted(list_word2)
    return (list_word1 == list_word2) 

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose = True)
    
    
