# Product of consecutive Fib numbers
# https://www.codewars.com/kata/5541f58a944b85ce6d00006a
def productFib(prod):
    def prod_fib(n):
        fib = [0, 1]
        if n == 0:
            return (fib[0], fib[1], fib[0]*fib[1])  # 0*1
        m = 1
        while m <= n:
            fib.append(fib[0] + fib[1])
            del fib[0]
            m += 1
        return (fib[0], fib[1], fib[0]*fib[1])
    m = 0
    while prod_fib(m)[2] <= prod:
        z = prod_fib(m)
        if z[2] == prod:
            return [z[0], z[1], True]
        m += 1
    z = prod_fib(m)
    return [z[0],z[1],False]
