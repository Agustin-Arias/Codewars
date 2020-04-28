# https://www.codewars.com/kata/56c04261c3fcf33f2d000534/train/python
def doubles(maxk, maxn):
    result = 0
    for k in range(1, maxk + 1):
        for n in range(1, maxn + 1):
            result += 1/(k*(n+1)**(2*k))
    return result
