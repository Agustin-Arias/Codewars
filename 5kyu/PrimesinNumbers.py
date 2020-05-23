def primeFactors(number):
    output,n="",number
    if n%2==0:
        power=0
        while n%2==0:n,power=n//2,power+1
        output += f"({2}**{power})" if power>1 else f"({2})"
    prime=3
    while n!=1:
        if n%prime==0:
            power=0
            while n%prime==0:n,power=n//prime,power+1
            output += f"({prime}**{power})" if power>1 else f"({prime})"
        prime+=2
    return output
