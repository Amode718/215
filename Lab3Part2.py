#LAB 3 Warmup

def counter(element, iterable) -> int:
    '''
    >>> counter (5, [5, 4, 3, 2, 2, 7, 8])
    1
    >>> counter (7, [4, 4, 4, 7, 7, 7, 6, 1, 1, 2, 3])
    3
    >>> counter (8, [1, 4, 7, 9, 9, 3, 1])
    0
    '''
    count = 0
    for item in iterable:
        if element == item:
            count += 1
    return count

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose = True)




def counter(string) -> dict:
    '''
    >>> counter ('You are the One and Only')
    {'lower': 16, 'upper': 3}
    >>> counter (' ')
    {'lower': 0, 'upper': 0}
    >>> counter ('I LIKE SUPERMAN')
    {'lower': 0, 'upper': 13}
    '''
    chara_case_counter = {'lower': 0, 'upper': 0}
    for char in string:
        if char.isupper():
            chara_case_counter['upper'] += 1
        elif char.islower():
            chara_case_counter['lower'] += 1
    return chara_case_counter

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose = True)



def in_list(lst, obj):
    '''
    >>> in_list ([0, 5, 6, 3, 1], 5)
    True
    >>> in_list ([0, 5, 6, 3, 1], "Hi")
    False
    >>> in_list ([0, 5, 6, 3, 1], -453)
    False
    '''
    hasObj = False
    for item in lst:
        if item == obj:
            hasObj = True
    return hasObj

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose = True)




def word_count(string) -> dict:
    '''
    >>> word_count ("Hey buddy hows it going?")
    {'hey': 1, 'buddy': 1, 'hows': 1, 'it': 1, 'going?': 1}
    >>> word_count (" ")
    {}
    >>> word_count ("I LIKE PIE I LIKE to Eat PiE")
    {'i': 2, 'like': 2, 'pie': 2, 'to': 1, 'eat': 1}
    '''
    string = string.lower()
    words = {}
    for i in string.split():
        words[i] = string.split().count(i)
    return words

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose = True)
