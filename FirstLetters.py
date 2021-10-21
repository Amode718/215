def first_letters(sentence):
    """
    >>> first_letters(“She sold six buns today”)
    {‘s’: 3, ‘b’: 1, ‘t’: 1}
    """

    lettersIn = {}
    
    wordsInSentence = sentence.lower()
    wordsInSentence = wordsInSentence.split()
    
    for word in wordsInSentence:
        letter = word[0]
        if letter in lettersIn:
            lettersIn[letter] += 1
        else:
            lettersIn[letter] = 1
    return lettersIn


if __name__ == "__main__":
    import doctest
    doctest.testmod()