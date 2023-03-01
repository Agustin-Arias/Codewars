# https://www.codewars.com/kata/540d0fdd3b6532e5c3000b5b
import re, math


def expand(expr, readable=False):
    def comb(n, k):
        return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))

    pattern = r"\((\-?\d*?)(\w)\+?(\-?\d*)\)\^(\d*)"
    a, x, b, n = re.match(pattern, expr).groups()
    if a == "":
        a = 1
    elif a == "-":
        a = -1
    else:
        a = int(a)
    a = int(a) if a != "" else 1
    b = int(b)
    n = int(n)
    if n == 0:
        return "1"
    expansion = ""
    if a == 0:
        expansion += str(b ** n)
    if b != 0 and a != 0:
        if a == 1:
            first_term = ""
        elif a == -1:
            first_term = "-"
        else:
            first_term = str(int(a ** n))
        expansion += first_term + (
            ""
            if n == 0
            else (f" {x}" if readable else x) + ("" if n == 1 else "^" + str(n))
        )
        k = n - 1
        while k >= 0:
            coefficient = int(a ** k * b ** (n - k) * comb(n, k))
            if coefficient > 0:
                expansion += "  +  " if readable else "+"
            expansion += str(coefficient) + (
                ""
                if k == 0
                else (f" {x}" if readable else x) + ("" if k == 1 else "^" + str(k))
            )
            k -= 1

    return expansion


print(expand("(5x+3)^7", True))
