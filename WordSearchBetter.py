#Andrei Modiga
#10-22-2020
import random



words = ["Bubble", "Tea", "honey", "lambo", "cars", "Profo"]



def empty_puzzle(height: int, width: int):

    """

    Returns an empty puzzle with a specified number of rows (height) and a specified number of columns (width) with spaces instead of letters.



    >>> empty_puzzle(5, 5)

    [[' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ']]

    >>> empty_puzzle(10, 5)

    [[' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ']]

    >>> empty_puzzle(0, 0)

    []

    """

    return [[' ' for i in range(width)] for x in range(height)]





def fit_check(height: int, width: int, word: str) -> bool:

    """

    Checks if the word fits within the parameters specified for the word puzzle.



    >>> fit_check(5, 5, 'hello')

    True

    >>> fit_check(2, 5, 'length')

    False



    """

    if len(word) > height and len(word) > width:

        return False

    else:

        return True



def valid_random_check(word: str, puzzle: list, height: int, width: int) -> list:

    """

    Checks if pseudo-randomly generated offset and starting position is valid 

    (fits in puzzle and word overlaps with the same letter only).

    """

    result = []



    row_ofst = random.randint(-1, 1) #chooses randomly between 3 numbers [-1, 0, 1]

    col_ofst = random.randint(-1, 1) #chooses randomly between 3 numbers [-1, 0, 1]

    row_strt = random.randrange(len(puzzle))

    col_strt = random.randrange(len(puzzle[0]))



    valid = False



    while(valid != True):

        for pos in range(len(word)):

            while (row_ofst == 0 and col_ofst == 0) == True:

                row_ofst = random.randint(-1, 1) 

                col_ofst = random.randint(-1, 1)

            if 0 <= row_strt + row_ofst * (len(word)-1) < height and 0 <= col_strt + col_ofst * (len(word)-1) < width:

               valid = True

            else:

                row_strt = random.randrange(5)

                col_strt = random.randrange(5)

                row_ofst = random.randint(-1, 1) 

                col_ofst = random.randint(-1, 1)

                break



    result.append(row_strt)

    result.append(row_ofst)

    result.append(col_strt)

    result.append(col_ofst)



    return result





def pos_check(letter: str, puzzle: list, row: int, col: int) -> bool:

    """

    Checks if position in puzzle is filled by a letter of a space.



    >>> pos_check('a', [['A'], []], 0, 0)

    True

    >>> pos_check('a', [[' '], [' ']], 0, 0)

    True

    >>> pos_check('a', [['B'], ['C']], 0, 0)

    False

    """

    if letter.upper() == puzzle[row][col]:

        return True

    elif puzzle[row][col] == ' ':

        return True

    else:

        return False



def generate_key(height: int, width: int, words: list) -> list:

    """

    Takes paramaters of height and width and generates an empty "puzzle" (list of lists) 

    that contains all of the words found in the list words.



    """

    puzzle = empty_puzzle(height, width)

    count = 0



    

    for word in sorted(words, key=len, reverse=True):

        count = 0

        pos_list = valid_random_check(word, puzzle, height, width)

        if fit_check(height, width, word) == False:

            continue

        else:

            while count != len(word):

                for pos in range(len(word)):

                    if pos_check(word[pos], puzzle, pos_list[0] + pos_list[1] * pos, pos_list[2] + pos_list[3] * pos) == True:

                        count += 1

                    else:

                        count = 0

                        pos_list = valid_random_check(word, puzzle, height, width)

                        break



        if fit_check(height, width, word) == False:

            continue

        else:

            for pos in range(len(word)):

                puzzle[pos_list[0] + pos_list[1] * pos][pos_list[2] + pos_list[3] * pos] = word[pos].upper()



    return puzzle



def fill_puzzle(key: list) -> list:

    """

    Takes the generated key with the list of words in it and returns a complete puzzle. All empty spaces will be filled with pseudorandom letters.

    """

    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    for i in range(len(key)):

        for j in range(len(key[0])):

            if key[i][j] == ' ':

                key[i][j] = letters[random.randint(0, len(letters) - 1)]

    return key



def calculate(x: int, y: int, z: int):

    return x + (y * z)



"""

5 6 7

4 X 0

3 2 1

reference

0 = 0,0

1 = 1,0

2 = 1,1

3 = 0,1

4 = -1,1

5 = -1, 0

6 = -1,-1

7 = 0,-1

8 = 1,-1

"""



for line in generate_key(10, 10, words):

    print(line)



# if __name__ == "__main__": 
# 
#     import doctest
# 
#     doctest.testmod()

