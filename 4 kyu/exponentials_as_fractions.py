# https://www.codewars.com/kata/54f5f22a00ecc4184c000034/train/python
from math import gcd, factorial

start = time()

def convertTofraction(x):
    num = int(x*10)
    den = 10
    num, den = num//gcd(num, den), den//gcd(num, den)
    return num, den

def sumtwofractions(x,y):
    num1, den1 = x  # numerator and denominator
    num2, den2 = y
    num3, den3 = den1*num2+den2*num1, den1*den2
    num3,den3 = num3//gcd(num3,den3), den3//gcd(num3,den3)
    return num3,den3

def expand(x, digit):
    print(x, digit)
    num = 1
    den = 1
    k = 1
    while len(str(num)) < digit:
        numx, denx = convertTofraction(x)
        num, den = sumtwofractions((num, den), (int(numx**k), int(denx**k)*factorial(k)))
        k += 1
    print(num, den)
    return [num, den]

print(time()-start)
