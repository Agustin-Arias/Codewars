## https://www.codewars.com/kata/584daf7215ac503d5a0001ae/train/python
import re
def is_constant(s): return s.count('x') == 0 and s.count('(') == 0

def separate(expression):
    if is_constant(expression) or expression == 'x': return [expression]

    rexOp = r"^\(([\+\-\*\/\^]) (.*)\)$"
    rexFunc = r"^\((cos|sin|tan|exp|ln) (.*)\)$"

    matchOp = re.search(rexOp, expression)
    matchFunc = re.search(rexFunc, expression)

    if matchFunc:
        opFunc, args = matchFunc.groups()[0], matchFunc.groups()[1:]
    else:
        opFunc, args = matchOp.groups()[0], matchOp.groups()[1]
        rexNoPar = r"^(-?\d*|x) (.*)$|^(.*) (-?\d*|x)$"
        matchNoPar = re.search(rexNoPar, args)
        if matchNoPar:
            groups = [match for match in matchNoPar.groups() if match != None]
            arg1, arg2 = groups[0], groups[1]
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
    if len(expression) == 1 or (expression[0] == '-' and len(expression) == 2): return expression

    g = separate(expression)
    if len(g) == 1: return expression
    opFunc, args = g

    if len(args) == 2:
        operator = opFunc

        arg1, arg2 = list(map(simplify, args))

        if is_constant(arg1) and is_constant(arg2):
            if operator != '^': return str(eval(f"{arg1}{operator}{arg2}"))
            else: return str(eval(f"{arg1}**{arg2}"))
        else:
            if operator == '+':
                if arg1 == '0': return arg2
                elif arg2 == '0': return arg1
                else: return f"(+ {arg1} {arg2})"
            elif operator == '-':
                if arg2 == '0': return arg1
                elif arg1 == '0': return f"(* -1 {arg2})"
                else: return f"(- {arg1} {arg2})"
            elif operator == '*':
                if arg1 == '1': return arg2
                elif arg2 == '1': return arg1
                elif arg1 == '0' or arg2 == '0': return '0'
                else: return f"(* {arg1} {arg2})"
            elif operator == '/':
                if arg1 == '0': return '0'
                elif arg2 == '1': return arg1
                else: return f"(/ {arg1} {arg2})"
            elif operator == '^':
                if arg1 == '0': return '0'
                elif arg2 == '1': return arg1
                else: return f"(^ {arg1} {arg2})"
    else:
        function = opFunc
        arg = simplify(args[0])
        return f"({function} {arg})"


def diff(s):
    if is_constant(s):
        return '0'
    elif s == 'x':
        return '1'

    opFunc, args = separate(s)

    if len(args) == 2:
        operator = opFunc
        arg1Diff, arg2Diff = list(map(diff, args))
        arg1, arg2 = args

        expressions = {
            '+' : f"(+ {arg1Diff} {arg2Diff})",
            '-' : f"(- {arg1Diff} {arg2Diff})",
            '*' : f"(+ (* {arg1Diff} {arg2}) (* {arg1} {arg2Diff}))",
            '/' : f"(/ (+ (* {arg1Diff} {arg2}) (* -1 (* {arg1} {arg2Diff}))) (^ {arg2} 2))",
            '^' : f"(+ (* {arg2} (* {arg1Diff} (^ {arg1} (+ {arg2} -1)))) (* {arg2Diff} (* (ln {arg1}) (^ {arg1} {arg2}))))"
        }
        expression = expressions[operator]
        return simplify(expression)
    else:
        function = opFunc
        arg = simplify(args[0])
        expressions = {
            'cos' : f"(* {diff(arg)} (* -1 (sin {arg})))",
            'sin' : f"(* {diff(arg)} (cos {arg}))",
            'tan' : f"(* {diff(arg)} (^ (cos {arg}) -2))",
            'exp' : f"(* {diff(arg)} (exp {arg}))",
            'ln' : f"(/ {diff(arg)} {arg})"
        }
        expression = expressions[function]
        return simplify(expression)

examples = [
    ("(+ x 2)", "1"),
    ("(* 1 x)", "1"),
    ("(^ x 3)", "(* 3 (^ x 2))"),
    ("(cos x)", "(* -1 (sin x))"),
    ("(sin x)", "(cos x)"),
    ("(tan x)", "(^ (cos x) -2)"),
    ("(exp x)", "(exp x)"),
    ("(ln x)" , "(/ 1 x)"),
    ("(+ x x)", "2"),
    ("(/ 2 (+ 1 x))", "(/ -2 (^ (+ 1 x) 2))"),
    ("(tan (* 2 x))", "(* 2 (^ (cos (* 2 x)) -2))"),
    ("(cos x)", "(* -1 (sin x))"),
    ("(- x x)", "0"),
    ("(/ x 2)", "0.5"),
    ("(- (+ x x) x)", "1"),
    ("(cos (* 2 x))", "(* 2 (* -1 (sin (* 2 x))))"),
    ("(* x 93)", "93")
]
N = len(examples)
for i in range(N):
    z = examples[i][0]
    print(f"Analysing: {z}")
    x = diff(z)
    y = examples[i][1]
    if x != y:
        print("Wrong Result")
        print(f"actual: {x}")
        print(f"expected: {y}")
    else:
        print("....Right Result")
    print()
