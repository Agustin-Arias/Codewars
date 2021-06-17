'''
Problem:
    https://www.codewars.com/kata/52a78825cdfc2cfc87000005/train/python

On tree representation of mathematical operations
    http://www.math.wpi.edu/IQP/BVCalcHist/calc5.html#_Toc407004380
'''

OPERANDS = {
    '+': lambda a, b: float(a) + float(b),
    '-': lambda a, b: 0 - float(b) if (a == '') else float(a) - float(b),
    '*': lambda a, b: float(a) * float(b),
    '/': lambda a, b: float(a) / float(b),
}

class Node:
    def __init__(self, value = None, left = None, right = None):
        '''
            --value can be a numeric string or a character
                ('+', '-', '*', '/')
            --left and right are instances of Node
        '''
        self.left = left
        self.right = right
        self.value = value

    def eval(self):


        if self.is_a_number():
            return self.value

        elif self.right.is_a_number() and self.left.is_a_number():
            operation = OPERANDS[self.value]
            left_number, right_number = self.left.value, self.right.value
            return operation(left_number, right_number)

        else:
            self.left = Node(value = str(self.left.eval()))
            self.right = Node(value = str(self.right.eval()))
            return self.eval()


    def is_a_number(self):
        # the node is a number iff it is
        # a terminal node
        return self.right == None and self.left == None

class Expression:
    def __init__(self, expression):
        # expression is an arithmetic
        # operation with parentheses,
        # numbers and operators such as
        # +, -, * and /
        self.expression = expression

    def getDigit(self, i):
        nodeVal = ""
        while self.expression[i].isdigit():
            nodeVal += self.expression[i]
            i+=1
        node = Node(value = nodeVal)
        i-=1
        return node, i

def getDigit(expression, i):
    # gets the digit starting from i
    number = ""
    indx = i
    while indx < len(expression) and expression[indx] in "0123456789.":
        number += expression[indx]
        indx+=1
    return number, indx

def getPar(expression, i):
    # gets the digit starting from i
    insidePar = ""
    indx = i+1
    parCounter = 1
    while indx < len(expression):
        char = expression[indx]

        if char == '(': parCounter+=1
        elif char == ')': parCounter-=1

        if parCounter == 0: break

        insidePar += expression[indx]

        indx+=1
    return insidePar, indx+1

def convert_minus_to_plus(expression):
    out = ""
    i = 0
    while i < len(expression):
        char = expression[i]
        if char == '-':
            # print(f"out: {out}")
            j = i+1
            number = ""
            while True:
                # print(f"expression[j:]: {expression[j:]}")
                if expression[j].isdigit():
                    number, j = getDigit(expression, j)
                    number = f"(-1)*({number})"
                    break
                elif expression[j] == '(':
                    number, j = getPar(expression, j)
                    number = f"(-1)*({number})"
                    break
                elif expression[j] == '-':
                    number, j = getDigit(expression, j+1)
                    break
                else:
                    j+=1
            if number != "":
                out += f"+ ({number})"
            else:
                out += f"+ (-1)*"
            number = ""
            i = j
        else:
            out += char
            i+=1
    return out

def parse(expression, prin = False):
    if expression == "":
        return None
    elif expression == "-1":
        return Node("-1")
    tree = Node()
    i = 0
    left = right = value =''
    removePar = False
    while i < len(expression):
        char = expression[i]

        if char.isdigit():

            left, i = getDigit(expression, i)
        elif char == '(':

            left, i = getPar(expression, i)
            if i == len(expression):
                removePar = True
        elif char == '+':

            value = char
            right = expression[i+1:]
            if left == '':
                left = expression[:i]
            i = len(expression)
        elif char == '*':

            value = char
            right = expression[i+1:]
            if left == '':
                left = expression[:i]
            i = len(expression)
        else:
            i+=1

            print(f"Now: left={left}")
            print(f"Now: value={value}")
            print(f"Now: right={right}")
            print(f"Now: expression[i:]={expression[i:]}")





    if removePar:
        tree = parse(left, True)
    elif left == '' and right != '':

        tree.value = right.strip()
    elif left != '' and right == '':

        tree.value = left.strip()
    else:

        tree.value = value

            tree.left = parse(left, True)
            tree.right = parse(right, True)
        else:
            tree.left = parse(left)
            tree.right = parse(right)
    return tree

tests = [
    ["1 + 1", 2],
    ["8/16", 0.5],
    ["3 -(-1)", 4],
    ["2 + -2", 0],
    ["10- 2- -5", 13],
    ["(((10)))", 10],
    ["3 * 5", 15],
    ["-7 * -(6 / 3)", 14]
]

i = 2
expression = tests[i][0]
print(f"expression: {expression}")
parsed_expression = convert_minus_to_plus(expression)
print(f"parsed_expression: {parsed_expression}")


tree = parse(expression, True)
print("\n"*5)
print(tree.value)
#print(tree.left.value)
#print(tree.right.value)
#print(tree.right.left.value)
#print(tree.right.right.value)
#print(tree.right.left.left.value)
#print(tree.right.left.right.value)
print(tree.eval())

# index = 0
# for expression, result in tests:
#     print("Testing   " + expression)
#     print(f"index: {index}")
#     tree = parse(expression)
#     if tree.eval() == result:
#         print("....All ok")
#     else:
#         print("...Error")
#         print(f"\tExpected: {result}")
#         print(f"\tGot: {tree.eval()}")
#     index += 1
# print(tree.eval()- eval(expression))

