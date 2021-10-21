#Andrei Modiga
#10-22-2020
def is_leap_year(year):
    """
    #firstTest
    >>> is_leap_year(2000)
    True
    >>> is_leap_year(2001)
    False
    >>> is_leap_year(2005)
    True
    """
    is_leap = True
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                is_leap = True
            else:
                is_leap = False
        else:
            is_leap = True
    else:
        is_leap = False
    return is_leap

if __name__ == "__main__":
    import doctest
    doctest.testmod()

