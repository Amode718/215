#Andrei Modiga
#12-03-2020
#215
# A very simple Bottle Hello World app for you to get started with...
from bottle import default_app, route

sauUsername = 'amodiga'
paUsername = 'amodiga'

@route('/hello')
def hello_world():
    return 'Hello from your favorite, Andrei!'

@route('/misc/caesar_cipher/<off>/<message>')
def caesar_cipher(off,message):
    """
   >>>caesar_cipher(5, "HeyBuddy")
   'MjdGziid'
   >>> caesar_cipher(0, "i like pie")
   'i like pie'
   >>> caesar_cipher(-3, "Tehyareliketheresy")
   'Qbevxobifhbqebobpv'
   """
    result = ""
    offset = int(off)
    for i in range(len(message)):
        char = message[i]

        if (char.isupper()):
            result += chr((ord(char) + offset-65) % 26 + 65)

        else:
            result += chr((ord(char) + offset - 97) % 26 + 97)

    return result


@route('/misc/roman_math/<rom1>/<op>/<rom2>')
def roman_math(rom1, op, rom2):
    """
    >>> roman_math('III', '+', 'I')
    'IV'
    >>> roman_math('C', 'x', 'IV')
    'CD'
    """
    num1 = romanNumeral(rom1)
    num2 = romanNumeral(rom2)

    if op == "+":
        return str(num1 + num2)
    elif op == "-":
        return str(num1 - num2)
    else:
        return str(num1 * num2)

def romanNumeral(romanNum):
    """
    Converts roman numerals to corresponding integers.
    >>> roman_to_int("XIII")
    13
    >>> roman_to_int("IV")
    4
    >>> roman_to_int("MXIX")
    1019
    >>> roman_to_int("MDCLIV")
    1654
    """
    numeralList = [char for char in romanNum]
    charList = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    charDict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    numList = []

    for chr in romanNum:
        numList.append(charDict[chr])

    print(numList)

    addNum = 0
    tmpLst = []
    counter = 0
    for num in numList:
        counter += 1

        if counter < len(numList):
            if num == numList[counter]:
                addNum += num

            elif num < numList[counter]:
                addNum += num
                tmpLst.append(addNum)
                addNum = 0

            elif num > numList[counter]:
                addNum += num
                tmpLst.append(addNum)
                addNum = 0

        elif counter == len(numList):
            if num == numList[counter - 2]:
                addNum += num
                tmpLst.append(addNum)
                addNum = 0

            elif num > numList[counter - 2]:
                if addNum > 0:
                    tmpLst.append(addNum)
                tmpLst.append(num)
                addNum = 0

            else:
                tmpLst.append(num)

    counter = 0
    finalNum = 0
    for num in tmpLst:
        counter += 1
        if counter < len(tmpLst):
            if num > tmpLst[counter] or num == tmpLst[counter]:
                finalNum += num
            else:
                finalNum -= num
        else:
            finalNum += num

    return int(finalNum)


@route('/misc/month_calendar/<yr>/<mth>')
def monthly_calendar(yr, mth):
    """
    >>> calendar(2020, 3, 12)
    '     March 2020
    Su Mo Tu We Th Fr Sa
    1  2  3  4  5  6  7
    8  9  10 11 12 13 14
    15 16 17 18 19 20 21
    22 23 24 25 26 27 28
    29 30 31            '
    >>> calendar(1980, 1, 1)
    '    January 1980
    Su Mo Tu We Th Fr Sa
           1  2  3  4  5
    6  7  8  9  10 11 12
    13 14 15 16 17 18 19
    20 21 22 23 24 25 26
    27 28 29 30 31      '
    """
    year = int(yr)
    month = int(mth)

    isLeapYear = is_leap_year(year)
    dayOfWeek = day_of_weekNum(year, month, 1)
    daysInMonth = {"1": 31, "2": 28, "3": 31, "4": 30, "5": 31, "6": 30, "7": 31, "8": 31, "9": 30, "10": 31, "11": 30, "12": 31}
    finalList = []

    row1 = str(center(month, year))
    row2 = "Su Mo Tu We Th Fr Sa "
    row3 = ""
    row4 = ""
    row5 = ""
    row6 = ""
    row7 = ""
    row8 = ""

    totalDays = 0
    row3 += " " * (3 * (dayOfWeek - 1))
    for i in range((7 - (dayOfWeek - 1))):
        row3 += " " + str(i + 1) + " "
        totalDays += 1


    row4TD = totalDays
    for i in range(7):
        if (i + (row4TD + 1) >= 10):
            row4 += str(i + (row4TD + 1)) + " "
        else:
            row4 += " " + str(i + (row4TD + 1)) + " "
        totalDays += 1

    row5TD = totalDays
    for i in range(7):
        if (i + (row5TD + 1) >= 10):
            row5 += str(i + (row5TD + 1)) + " "
        else:
            row5 += " " + str(i + (row5TD + 1)) + " "
        totalDays += 1

    row6TD = totalDays
    for i in range(7):
        if (i + (row6TD + 1) >= 10):
            row6 += str(i + (row6TD + 1)) + " "
        else:
            row6 += " " + str(i + (row6TD + 1)) + " "
        totalDays += 1

    if totalDays >= daysInMonth[str(month)]:
        row7 = "                     "
        row8 = "                     "

    elif (totalDays + 7) < daysInMonth[str(month)]:
        row7TD = totalDays
        for i in range(7):
            if (i + (row7TD + 1) >= 10):
                row7 += str(i + (row7TD + 1)) + " "
            else:
                row7 += " " + str(i + (row7TD + 1)) + " "
            totalDays += 1


        row8TD = totalDays
        for i in range(7):
            if (i + 1) <= daysInMonth[str(month)] - totalDays:
                row8 += str(i + (row8TD + 1)) + " "
            else:
                row8 += "   "


    elif (totalDays + 7) >= daysInMonth[str(month)]:
        row7TD = totalDays
        for i in range(7):
            if (i + 1) <= daysInMonth[str(month)] - totalDays:
                row7 += str(i + (row7TD + 1)) + " "
            else:
                row7 += "   "
        row8 = "                     "

    finalString = row1 + "\n" + row2 + "\n" + row3 + "\n" + row4 + "\n" + row5 + "\n" + row6 + "\n" + row7 + "\n" + row8
    return finalString

def day_of_weekNum(year, month, day):
    """Determine the day of the week this date fell on
    (0 = Saturday, 1 = Sunday, ... 6 = Friday).
    int, int, int -> int
    Formula from https://en.wikipedia.org/wiki/Zeller%27s_congruence
    >>> day_of_week(2020, 9, 7)
    2
    >>> day_of_week(1752, 9, 14)
    5
    >>> day_of_week(2000, 2, 29)
    3
    >>> day_of_week(1776, 7, 4)
    5
    """

    if month == 1 or month == 2:
        month += 12
        year -= 1
    day = ((day + (13*(month + 1) // 5) +
            year + (year // 4) -
            (year // 100) + (year // 400) ) % 7)

    if day == 0:
        return 7
    else:
        return day

def is_leap_year(year):

    """
    >>> is_leap_year(2020)
    True
    >>> is_leap_year(1950)
    False
    >>> is_leap_year(1944)
    True
    >>> is_leap_year(1844)
    True
    >>> is_leap_year(1934)
    False
    """

    if (year % 4 != 0):
        return False
    elif (year % 4 == 0) and (year % 100 != 0):
        return True
    elif (year % 4 == 0) and (year % 100 == 0) and (year % 400 != 0):
        return False
    elif (year % 4 == 0) and (year % 100 == 0) and (year % 400 == 0):
        return True

def center(month, year):
    """
    >>> center(3, 2020)
    '     March 2020     '
    >>> center(5, 1999)
    '      May 1999      '
    """

    length = len(monthName(month)) + (len(str(year)) + 1)
    spacing = (20 - length) // 2
    cntr = ((" " * (int(spacing) + 1)) + monthName(month) + " " + str(year))
    for i in range(21 - len(cntr)):
        cntr += " "

    return cntr

def monthName(month):
    """Matches the name of the month to the number of the month
    >>> monthName(7)
    'July'
    >>> monthName(1)
    'January'
    >>> monthName(10)
    'October'
    """


    if month == 1:
        return "January"
    elif month == 2:
        return "February"
    elif month == 3:
        return "March"
    elif month == 4:
        return "April"
    elif month == 5:
        return "May"
    elif month == 6:
        return "June"
    elif month == 7:
        return "July"
    elif month == 8:
        return "August"
    elif month == 9:
        return "September"
    elif month == 10:
        return "October"
    elif month == 11:
        return "November"
    elif month == 12:
        return "December"
    else:
        return("Incorrect month")


@route('/misc/day_of_week/<yr>/<mnth>/<dy>')
def day_of_week(yr, mnth, dy):
    """Determine the day of the week this date fell on
    (0 = Saturday, 1 = Sunday, ... 6 = Friday).
    int, int, int -> int
    Formula from https://en.wikipedia.org/wiki/Zeller%27s_congruence
    >>> day_of_week(2020, 9, 7)
    2
    >>> day_of_week(1752, 9, 14)
    5
    >>> day_of_week(2000, 2, 29)
    3
    >>> day_of_week(1776, 7, 4)
    5
    """
    year = int(yr)
    month = int(mnth)
    day = int(dy)
    dayDict = {'1':"Sunday", '2':'Monday', '3':'Tuesday', '4':'Wednesday', '5':'Thursday', '6':'Friday', '7':'Saturday'}

    if month == 1 or month == 2:
        month += 12
        year -= 1
    day = ((day + (13*(month + 1) // 5) +
            year + (year // 4) -
            (year // 100) + (year // 400) ) % 7)

    finalDay = 0
    if day == 0:
        finalDay = 7
    else:
        finalDay = day

    return dayDict[str(finalDay)]


@route('/misc/is_leap_year/<yr>')
def is_leap_yr(yr):
    """
    >>> is_leap_year(2020)
    True
    >>> is_leap_year(1971)
    False
    >>> is_leap_year(1944)
    True
    >>> is_leap_year(1844)
    True
    >>> is_leap_year(1990)
    False
    """
    year = int(yr)

    if (year % 4 != 0):
        return json.dumps(False)
    elif (year % 4 == 0) and (year % 100 != 0):
        return json.dumps(True)
    elif (year % 4 == 0) and (year % 100 == 0) and (year % 400 != 0):
        return json.dumps(False)
    elif (year % 4 == 0) and (year % 100 == 0) and (year % 400 == 0):
        return json.dumps(True)


application = default_app()


