# https://www.codewars.com/kata/5547cc7dcad755e480000004
def removNb(n):
    # a*b = 1+2+...+n -a -b --> a*b+a+b = n*(n+1)/2 --> (a+1)(b+1)=n(n+1)/2+1
    # --> a*b = n(n+1)/2 + 1 , 1 <= b <= n(n+1)/2 + 1, 1 <= a <= n(n+1)/2 + 1 
    result = []
    s = n*(n+1) // 2 + 1
    for a in range(1,n + 1):
        if s % a == 0 and (s // a) in range(1, n+1):
            result.append((a-1, s//a - 1))  # we need to subtract 1
    return result
