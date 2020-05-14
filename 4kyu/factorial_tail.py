# Factorial Tail
# https://www.codewars.com/kata/55c4eb777e07c13528000021/train/python

'''
v_{p}(n!) = sum_{k>=1} floor(n/p^k)
And
v_{p^k}(n!) = v_{p}(n!) // k
'''
def legendre_formula(number, prime, power):
    b = prime
    n = number
    s = 0
    i = 1
    while n >= b**i:
        s += n // b**i
        i += 1
    return s//power

def prime_factorization(n):
    output = []
    counter = 0
    number = n
    while number % 2 == 0:
        number = number // 2
        counter += 1
    if counter != 0:
        output.append((2, counter))

    prime = 3
    while number != 1:
        counter = 0
        while number % prime == 0:
            number = number // prime
            counter += 1
        if counter != 0:
            output.append((prime, counter))
        prime += 2
    return output

def zeroes(base, number):
    return min(legendre_formula(number, prime, power) for prime, power
    in prime_factorization(base))

