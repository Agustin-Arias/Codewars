'''
Problem:
    https://www.codewars.com/kata/52a78825cdfc2cfc87000005/train/python

On tree representation of mathematical operations
    http://www.math.wpi.edu/IQP/BVCalcHist/calc5.html#_Toc407004380
'''

OPERANDS = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a*b,
    '/': lambda a, b: a/b,
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
        print(f"self.value: {self.value}")
        if self.left != None:
            print(f"left: {self.left.value}")
            print(f"right: {self.right.value}")
        if self.right == None and self.left == None:
            result = self.value
        elif self.right.isDigit() and self.left.isDigit():
            result = OPERANDS[self.value](int(self.left.value), int(self.right.value))
        else:
            self.left = Node(value = str(self.left.eval()))
            self.right = Node(value = str(self.right.eval()))
            result = self.eval()

        return result

    def isDigit(self):
        return self.value.isdigit()

class Expression:
    def __init__(self, expression):
        self.expression = expression

    def getDigit(self, i):
        nodeVal = ""
        while self.expression[i].isdigit():
            nodeVal += self.expression[i]
            i+=1
        node = Node(value = nodeVal)
        i-=1
        return node, i

    def getPar(self, i):
        nodeVal = ""
        parCounter = 1
        expression = self.expression
        i+=1

        while True:
            if expression[i] == '(':
                parCounter += 1
            elif expression[i] == ')':
                parCounter -= 1
            if parCounter == 0: break
            nodeVal += expression[i]
            i+=1

        exp = Expression(nodeVal)
        i -= 1
        return exp.parse(), i

    def parse(self):
        tree = Node()
        expression = self.expression

        i = 0
        while i < len(expression):
            if expression[i].isdigit():
                left, i = self.getDigit(i)
            elif expression[i] in "+-*/":
                tree.value = expression[i]
                tree.left = left
                tree.right = Node(value = expression[i+1:].strip())
                i = len(expression)
            elif expression[i] == '(':
                left, i = self.getPar(i)
            i+=1
        return tree



expression = Expression(" (1231+231) + 243")

node = expression.parse()


print(node.eval())

# print(f"n1: {node}")
# print(f"n1.v: {node.value}")
# print(f"n2.v: {node.left.value}")
# print(f"n2.l.v: {node.left.left.value}")
# print(f"n2.r.v: {node.left.right.value}")
# print(f"n3.v: {node.right.value}")
