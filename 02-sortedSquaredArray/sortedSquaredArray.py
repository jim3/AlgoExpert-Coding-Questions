def sortedSquaredArray(array):
    # arr = array[:]
    lst = []
    for a in array:
        lst.append(a * a)
        lst.sort()
    return lst

array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = sortedSquaredArray(array)
