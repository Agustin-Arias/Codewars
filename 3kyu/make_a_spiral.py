# Make a spiral
# https://www.codewars.com/kata/534e01fbbb17187c7e0000c6
import numpy as np
import itertools


def create_spiral(m):
    a = np.zeros(shape=(m,m))

    a[[0],0:m] = np.ones(shape = (1,m))

    a[1:,[m-1]] = np.ones(shape = (m-1,1))

    a[[m-1],:(m-1)] = np.ones(shape=(1,m-1))

    a[2:m-1,[0]] = np.ones(shape = (m-3,1))

    a[2,1] = 1
    return a


def spiralize(size):
    m = size
    a = create_spiral(m)
    for k in range(2,(m-1)//2,2):
        a[k:m-k,k:m-k] = create_spiral(m-2*k)
    if m % 4 == 2:
        k = m//2-1
        a[k:m-k,k:m-k] = [[1,1], [0,1]]
    elif m % 4 == 0:
        k = m//2
        a[k,k-1] = 0
    elif m % 4 == 1:
        k = m //2
        a[k,k] = 1
    f = np.vectorize(int)
    a = f(a)
    return a.tolist()
