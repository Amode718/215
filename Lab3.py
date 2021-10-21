#LAB 3

#Andrei Modiga
#09-22-2020

def mean(numbers: list) -> float:
    '''
    >>> mean([1, 2, 3, 4, 5])
    3.0
    >>> mean([])
    
    >>> mean([4, 6, 1, 32, 54])
    19.4
    '''
    if len(numbers) > 0:
        total = 0
        for x in numbers:
            total += x
        return total/len(numbers)
    
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose = True)
    
    
    
#Andrei Modiga
#09-22-2020

def median(num: list) -> float:
    """W
    >>> median([])
    
    >>> median([5, 20, 8, 12, 23])
    12
    >>> median([1, 2, 3, 4, 5])
    3
    """
    mid = len(num) // 2
    num = sorted(num)
    if num == []:
        return None
    elif len(num) % 2 == 0:
        return (num[mid] + num[mid - 1])/ 2
    else:
        return num[mid]
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose = True)
    
    
    
#Andrei Modiga
#09-22-2020    
    
def counter(number: float) -> dict:
    '''
    >>> counter([1.332])
    {1: 1, 2: 1, 3: 2}
    >>> counter([])
    
    >>> counter([6.45])
    {1: 3, 3: 0, 5: 1}
    ''' 
    intCount = {}
    for integer in str(number):
        if integer == '.':
            continue
        else:
            intCount[int(integer)] = str(number).count(integer)
    return intCount    


#Andrei Modiga
#09-22-2020

mat1 = [ [-1, 7, 4, 4], [11, 8, 7, 8], [-10, -3, 11, -7], [10, -2, 1, 10], [6, 10, -4, 5]]
mat2 = [[-7, 11, 6], [4, -6, -10], [9, -2, 3], [-1, -3, -3]]
def matrix_multiply(mat1: list, mat2: list):
    """
    >>> matrix_multiply([[]], [[]])
    []
    >>> matrix_multiply([[]], [[]])
    """
    mat_result = []
    lst = []
    result = []
    for row in mat1:
        for j in range(len(mat2[0])):
            temp_result = 0
            for i in range(len(row)):
                temp_result += row[i]*mat2[i][j]
            mat_result.append(temp_result)
    for i in range(len(mat_result)):
        lst.append(mat_result[i])
        if len(lst) == len(mat2[0]):
            result.append(lst)
            lst = []
    return result

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose = True)
    