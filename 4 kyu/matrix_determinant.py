import numpy as np

# https://www.codewars.com/kata/52a382ee44408cea2500074c

def determinant(matrix):
    array = np.array(matrix)
    if len(array) == 1:
        return array[0][0]
    elif len(array) == 2:
        return array[0][0]*array[1][1]-array[0][1]*array[1][0]
    def matrix_minor(arr, i, j):
        return np.delete(np.delete(arr,i,axis=0), j, axis=1)
    result = 0
    k = 0
    for elem in array[0]:
        if elem != 0:
            if k % 2 == 0:
                result += elem*determinant(matrix_minor(array,0,k))
            else:
                result -= elem*determinant(matrix_minor(array,0,k))
        k += 1
    return result
