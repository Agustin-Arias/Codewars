## https://www.codewars.com/kata/584daf7215ac503d5a0001ae/train/python
import re
def is_constant(s): return s.count('x') == 0 and s.count('(') == 0

def separate(expression):
    # print(f"\n\n\nexpression: {expression}")
    if is_constant(expression) or expression == 'x': return [expression]

    rexOp = r"^\(([\+\-\*\/\^]) (.*)\)$"
    rexFunc = r"^\((cos|sin|tan|exp|ln) (.*)\)$"

    matchOp = re.search(rexOp, expression)
    matchFunc = re.search(rexFunc, expression)

    if matchFunc:
        opFunc, args = matchFunc.groups()[0], matchFunc.groups()[1:]
    else:
        opFunc, args = matchOp.groups()[0], matchOp.groups()[1]
        # print(opFunc)
        # print(f"args: {args}")
        # rexNoPar = r"^(-?[\dx]) (.*)$|^(.*) ([\dx])$"
        rexNoPar = r"^(-?\d*|x) (.*)$|^(.*) (-?\d*|x)$"
        matchNoPar = re.search(rexNoPar, args)
        if matchNoPar:
            groups = [match for match in matchNoPar.groups() if match != None]
            # print(matchNoPar.groups())
            # print(groups)
            arg1, arg2 = groups[0], groups[1]
            # print(f"arg1: {arg1}")
            # print(f"arg2: {arg2}")
        else:
            index = 1
            par_count = 1
            while index < len(args) and par_count != 0:
                char = args[index]
                if char == '(': par_count+=1
                elif char == ')': par_count-=1
                index+=1
            arg1 = args[:index]
            arg2 = args[index+1:]
        args = (arg1, arg2)
    return opFunc, args

def simplify(expression):
    # print("\n"*5)
    # print(f"expression: {expression}")
    if len(expression) == 1 or (expression[0] == '-' and len(expression) == 2): return expression

    g = separate(expression)
    if len(g) == 1: return expression
    opFunc, args = g

    # print(f"opFunc: {opFunc}")
    # print(f"args: {args}")
    if len(args) == 2:
        operator = opFunc

        # print(f"operator: {operator}")
        # print(f"args: {args}")
        arg1, arg2 = list(map(simplify, args))

        # is operator
        # print(f"arg1: {arg1}")
        # print(f"expression:{expression}")
        # print(f"arg2: {arg2}")
        if is_constant(arg1) and is_constant(arg2):
            # print(expression)
            # print(f"constant-exp: {str(eval(f'{arg1}{operator}{arg2}'))}")
            if operator != '^':
                return str(eval(f"{arg1}{operator}{arg2}"))
            else:
                return str(eval(f"{arg1}**{arg2}"))
        else:
            if operator == '+':
                if arg1 == '0':
                    return arg2
                elif arg2 == '0':
                    return arg1
                else:
                    return f"(+ {arg1} {arg2})"
            elif operator == '-':
                if arg2 == '0': return arg1
                elif arg1 == '0': return f"(* -1 {arg2})"
                else:
                    return f"(- {arg1} {arg2})"
            elif operator == '*':
                if arg1 == '1':
                    return arg2
                elif arg2 == '1':
                    return arg1
                elif arg1 == '0' or arg2 == '0':
                    return '0'
                else:
                    return f"(* {arg1} {arg2})"
            elif operator == '/':
                if arg1 == '0': return '0'
                elif arg2 == '1': return arg1
                else:
                    return f"(/ {arg1} {arg2})"
            elif operator == '^':
                # print('################################')
                # print(f"arg1: {arg1}")
                # print(f"arg2: {arg2}")
                if arg1 == '0': return '0'
                elif arg2 == '1': return arg1
                else:
                    # print(f'value: {f"(^ {arg1} {arg2})"}')
                    return f"(^ {arg1} {arg2})"
    else:
        function = opFunc
        arg = simplify(args[0])
        # print(f'value: {f"({function} {arg})"}')
        return f"({function} {arg})"

def diff(s):
    # print(s)
    if is_constant(s):
        return '0'
    elif s == 'x':
        return '1'

    opFunc, args = separate(s)

    if len(args) == 2:
        operator = opFunc
        arg1Diff, arg2Diff = list(map(diff, args))
        arg1, arg2 = args
        # print(f"arg1: {arg1}")
        # print(f"arg2: {arg2}")
        if operator == '+':
            expression = f"(+ {arg1Diff} {arg2Diff})"
            # print(f"derivative: {expression}")
            return simplify(expression)
        elif operator == '-':
            expression = f"(- {arg1Diff} {arg2Diff})"
            # print(f"derivative: {expression}")
            return simplify(expression)
        elif operator == '*':
            expression = f"(+ (* {arg1Diff} {arg2}) (* {arg1} {arg2Diff}))"
            # print(f"expression: {expression}")
            return simplify(expression)
        elif operator == '/':

            a, b = arg1, arg2
            aDiff, bDiff = arg1Diff, arg2Diff
            expression = f"(/ (+ (* {aDiff} {b}) (* -1 (* {a} {bDiff}))) (^ {b} 2))"
            # print(expression)
            return simplify(expression)
        elif operator == '^':
            a, b = arg1, arg2
            aDiff, bDiff = arg1Diff, arg2Diff

            # print(f"a: {a}")
            # print(f"b: {b}")
            # print(f"aDiff: {aDiff}")
            # print(f"bDiff: {bDiff}")

            firstTerm = f"* {b} (* {aDiff} (^ {a} (+ {b} -1)))"
            secondTerm = f"* {bDiff} (* (ln {a}) (^ {a} {b}))"
            expression = f"(+ ({firstTerm}) ({secondTerm}))"
            # print(expression)

            return simplify(expression)
    else:
        function = opFunc
        # print()
        # print(f"args: {args}")
        arg = simplify(args[0])
        if function == 'cos':
            expression = f"(* {diff(arg)} (* -1 (sin {arg})))"
            # print(expression)
            return simplify(expression)
        elif function == 'sin':
            expression = f"(* {diff(arg)} (cos {arg}))"
            return simplify(expression)
        elif function == 'tan':
            expression = f"(* {diff(arg)} (^ (cos {arg}) -2))"
            return simplify(expression)
        elif function == 'exp':
            expression = f"(* {diff(arg)} (exp {arg}))"
            return simplify(expression)
        else:  # ln
            expression = f"(* {diff(arg)} (^ {arg} -1))"
            expression = f"(/ {diff(arg)} {arg})"
            return simplify(expression)

# examples = [
#     ("(+ x 2)", "1"),
#     ("(* 1 x)", "1"),
#     ("(^ x 3)", "(* 3 (^ x 2))"),
#     ("(cos x)", "(* -1 (sin x))"),
#     ("(sin x)", "(cos x)"),
#     ("(tan x)", "(^ (cos x) -2)"),
#     ("(exp x)", "(exp x)"),
#     ("(ln x)" , "(/ 1 x)"),
#     ("(+ x x)", "2"),
#     ("(/ 2 (+ 1 x))", "(/ -2 (^ (+ 1 x) 2))"),
#     ("(tan (* 2 x))", "(* 2 (^ (cos (* 2 x)) -2))"),
#     ("(cos x)", "(* -1 (sin x))"),
#     ("(- x x)", "0"),
#     ("(/ x 2)", "0.5"),
#     ("(- (+ x x) x)", "1"),
#     ("(cos (* 2 x))", "(* 2 (* -1 (sin (* 2 x))))"),
#     ("(* x 93)", "93")
# ]
# N = 0
# for i in range(N):
#     z = examples[i][0]
#     # print(f"Analysing: {z}")
#     x = diff(z)
#     y = examples[i][1]
#     if x != y:
        print("Wrong Result")
        print(f"actual: {x}")
        print(f"expected: {y}")
#     else:
        print("....Right Result")
    print()

# if N == 0:
#     s = examples[16][0]
    # print(s)
    # print(diff(s))
#     # print(simplify("(+ (* 1 93) (* x 0))"))
#     # print(separate("93"))
#     # print(simplify("(^ 2 2)"))
#     # print(simplify("(/ (+ (* 1 2) (* -1 (* x 0))) (^ 2 2))"))
#     # print(separate(s))
#     # print(simplify("(/ (+ (* 0 (+ 1 x)) (* -1 (* 2 1))) (^ (+ 1 x) 2))"))
#     # print(separate("(^ (+ 1 x) 2)"))
# # (* 2 (* -1 (sin (* 2 x))))
# # (* -2 (sin (* 2 x)))
