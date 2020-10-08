# https://www.codewars.com/kata/57f2b753e3b78621da0020e8/train/python

def replace(string, table):
    out = ""
    for char in string:
        if char in table.keys():
            out+=table[char]
        else:
            out+=char
    return out

def simplify(equalities, formulaOr):
    import re
    pattern = r"(\d+)(\w|\(|\ )"
    repl = r"\1*\2"

    table = {eq.split("=")[1].strip() : '(' + re.sub(pattern, repl, eq.split("=")[0].strip()) + ')' for eq in equalities}

    formula = formulaOr
    formula = re.sub(pattern, repl, formula)

    while any(formula.count(var) != 0 for var in table.keys()):
        formula = replace(formula, table)

    leftOverVar = ''
    i = 0
    while leftOverVar == '' and i < len(formula):
        char = formula[i]
        if not char in "()+-*1234567890":
            leftOverVar = char
        i+=1

    formula = formula.replace(leftOverVar, '1')
    formula = eval(formula)
    formula = str(formula) + leftOverVar
    return formula
