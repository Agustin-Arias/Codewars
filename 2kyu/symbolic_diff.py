## https://www.codewars.com/kata/584daf7215ac503d5a0001ae/train/python
def is_constant(s): return s.count('x') == 0 and s.count('(') == 0



import re
def simplify(expression):
    # print("\n"*5)
    # print(f"expression: {expression}")
    if len(expression) == 1 or (expression[0] == '-' and len(expression) == 2): return expression

    rexOp = r"([+-^*]) (\(.*?\)|[^\ ]*) (\(.*\)|[^\ \)]*)"
    rexFunc = r"(cos|sin|tan|exp|ln) (\(.*\)|[^\ \)]*)"

    matchOp = re.search(rexOp, expression)
    matchFunc = re.search(rexFunc, expression)

    if matchOp:
        operator, args = matchOp.groups()[0], matchOp.groups()[1:]
        # print(f"operator: {operator}")
        # print(f"args: {args}")
        arg1, arg2 = list(map(simplify, args))

        # is operator
        # print(f"arg1: {arg1}")
        # print(f"expression:{expression}")
        # print(f"arg2: {arg2}")
        if operator == '+':
            if is_constant(arg1) and is_constant(arg2):
                # print(f'value: {str(eval(f"{arg1}{operator}{arg2}"))}')
                return str(eval(f"{arg1}{operator}{arg2}"))
            elif arg1 == '0':
                return arg2
            elif arg2 == '0':
                return arg1
            else:
                return f"(+ {arg1} {arg2})"
        elif operator == '*':
            if is_constant(arg1) and is_constant(arg2):
                return str(eval(f"{arg1}{operator}{arg2}"))
            elif arg1 == '1':
                return arg2
            elif arg2 == '1':
                return arg1
            elif arg1 == '0' or arg2 == '0':
                return '0'
            else:
                return f"(* {arg1} {arg2})"
        elif operator == '^':
            if arg1 == '0' or arg2 == '1':
                return str(eval(f"{arg1}{opFunc}{arg2}"))
            else:
                # print(f'value: {f"(^ {arg1} {arg2})"}')
                return f"(^ {arg1} {arg2})"
    elif matchFunc:
        function, args = matchFunc.groups()[0], matchFunc.groups()[1:]
        arg = simplify(args[0])
        # print(f'value: {f"({function} {arg})"}')
        return f"({function} {arg})"

def diff(s):

    if is_constant(s):
        return '0'
    elif s == 'x':
        return '1'

    lis = s[1:-1].split(" ")
    # print(f"lis: {lis}")
    opFunc, args = lis[0], lis[1:]
    if len(args) == 2:
        arg1Diff, arg2Diff = list(map(diff, args))
        arg1, arg2 = args
        if opFunc == '+':
            expression = f"+ {arg1Diff} {arg2Diff}"
            # print(f"derivative: {expression}")
            return simplify(expression)
        elif opFunc == '*':
            expression = f"+ (* {arg1Diff} {arg2}) (* {arg1} {arg2Diff})"
            # print(f"derivative: {expression}")
            return simplify(expression)
        elif opFunc == '^':
            # print(expression)
            a, b = arg1, arg2
            aDiff, bDiff = arg1Diff, arg2Diff

            firstTerm = f"* {b} (* {aDiff} (^ {a} (+ {b} -1)))"
            secondTerm = f"* {bDiff} (* (ln {a}) (^ {a} {b}))"
            expression = f"+ ({firstTerm}) ({secondTerm})"

            return simplify(expression)
    else:
        # print()
        # print(f"args: {args}")
        arg = simplify(args[0])
        if opFunc == 'cos':
            expression = f"(* -1 (* {diff(arg)} (sin {arg})))"
            return simplify(expression)
        elif opFunc == 'sin':
            expression = f"(* {diff(arg)} (cos {arg}))"
            return simplify(expression)
        elif opFunc == 'tan':
            expression = f"(* {diff(arg)} (^ (cos {arg}) -2))"
            return simplify(expression)
        elif opFunc == 'exp':
            expression = f"(* {diff(arg)} (exp {arg})"
            return simplify(expression)
        else:  # ln
            # print(arg)
            expression = f"(* {diff(arg)} (^ {arg} -1) )"
            return simplify(expression)

examples = [
    "(+ x 2)",
    "(* 1 x)",
    "(^ x 3)",
    "(cos x)",
    "(sin x)",
    "(tan x)",
    "(exp x)",
    "(ln x)",
]
s = examples[7]
print(s)
print(diff(s))
# print(simplify("(* 0 (* (ln x) (^ x 3)))"))
