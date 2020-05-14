# Simple Fun #159: Middle Permutation
# https://www.codewars.com/kata/58ad317d1541651a740000c5/train/python
from itertools import permutations
from math import factorial


def middle_permutation(string):
    n = len(string)
    perms = [''.join(a) for a in permutations(string)]
    print(perms)
    perms.sort()
    print(perms)
    print(perms.index("cxgdba"))
    return perms[factorial(n)//2-1]


string = "abcdxg"
print(middle_permutation(string))
