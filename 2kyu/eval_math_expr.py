import re
from operator import itemgetter

OPERANDS = {
    '+': lambda a, b: float(a) + float(b),
    '-': lambda a, b: 0 - float(b) if (a == '') else float(a) - float(b),
    '*': lambda a, b: float(a) * float(b),
    '/': lambda a, b: float(a) / float(b),
}

PATTERNS = {
    "any_number": r"(-?\d+)",
    "positive_number": r"(\d+)",
    "operand": r"(\+|\-|\*|\/)",
    "plus_or_minus": r"(\+|\-)",
}

class Node:
    def __init__(self, value = None, left = None, right = None):
        '''
            --value can be a numeric string or a character
                ('+', '-', '*', '/')
            --left and right are instances of Node
        '''
        self.left = left
        self.value = value
        self.right = right

    def __str__(self, level = 0):
        output = "\t"*level + self.value + "\n"
        for child in [self.left, self.right]:
            if child != None:
                output += child.__str__(level + 1)

        return output

# class Tree:
#     def __init__(self, head = None):
#         self.head = head

#     def __str__(self):
#         return self.head.__str__()

class Expression:

    def __init__(self, string = ""):
        self.string = self.trasform_negatives(self.remove_double_operands(string.replace(' ', '')))


    def get_binary_expression(self):
        any_number, operand = PATTERNS['any_number'], PATTERNS['operand']
        pattern = rf"^{any_number}{operand}{any_number}$"
        return re.search(pattern, self.string)

    def remove_double_operands(self, string): 
        plus_or_minus = PATTERNS['plus_or_minus']
        pattern = rf"{plus_or_minus}{plus_or_minus}"
        get_sign = lambda m: '+' if float(f"{m.group(1)}1") * float(f"{m.group(2)}1") > 0 else '-'
        return re.sub(pattern, get_sign, string)

    def is_wrapped_in_parenthesis(self):
        index = 0
        parenthesis_count = 0
        parenthesis_add = {
            '(': 1,
            ')':-1
        }

        index = 0
        if self.string[index] in '()':
            char = self.string[index]
            parenthesis_count += parenthesis_add[char]
            index+=1
            while parenthesis_count != 0 and index < len(self.string):
                char = self.string[index]
                if char in '()':
                    parenthesis_count+=parenthesis_add[char]
                index += 1

        return index == len(self.string) and parenthesis_count == 0

    def remove_parenthesis(self):
        self.string = self.string[1:-1]

    def left_has_no_parenthesis(self):
        return self.string[0] != '('

    def separate_left(self):
        any_number, operand = PATTERNS['any_number'], PATTERNS['operand']
        pattern = rf"^{any_number}{operand}(.*)$"
        return re.search(pattern, self.string).groups()

    def is_number(self):
        any_number = PATTERNS['any_number']
        pattern = f"^{any_number}$"
        if re.match(pattern, self.string):
            return True
        return False

    def remove_double_negative(self, string):
        # simplify sections of the form {}
        positive_number = PATTERNS['positive_number']
        unit = rf"\(?\-{positive_number}\)?"
        pattern = rf"{unit}\*{unit}"
        repl = r"\1*\2"
        return re.sub(pattern, repl, string)


    def trasform_negatives(self, string):
        # remove negatives preceeding parenthesis
        pattern = r"\-\("
        repl = r"+(-1)*("
        output = re.sub(pattern, repl, string)
        output = self.remove_double_negative(output)

        # remove negatives preceeding numbers
        pattern = r"\-([2-9]|\d{2,})"
        repl = r"+(\1)*(-1)"
        output = re.sub(pattern, repl, output)

        output = self.remove_double_negative(output)
        
        return output

    def to_tree(self):

        if self.is_wrapped_in_parenthesis():
            self.remove_parenthesis()
            self.to_tree()

        if self.is_number():
            return Node(value = self.string)

        regex_search = self.get_binary_expression()
        if regex_search:
            left, operand, right = regex_search.groups()
            head_node = Node(operand, Node(value = left), Node(value = right))
            return head_node

        if self.left_has_no_parenthesis():
            left, operand, right = self.separate_left()
            head_node = Node(operand, left = Node(left), right = Expression(right).to_tree())

        else:
            left = ''

            index = 1
            parenthesis_count = 1

            parenthesis_add = {
                '(': 1,
                ')':-1
            }

            while index < len(self.string):
                char = self.string[index]
                if char in '()':
                    parenthesis_count+=parenthesis_add[char]
                if parenthesis_count == 0:
                    break
                left += char
                index += 1

            index += 1
            operand = self.string[index]
            right = self.string[index+1:]

            head_node = Node(operand, left = Expression(left).to_tree(), right = Expression(right).to_tree())


        return head_node


'''
-(-\d+) => +\d
+- => 
pattern = \-\(\-\d+\)
'''
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

'''
    Number: '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | 9

    Operand: '+' | '-' | '/' | '*'

    Parenthesis: '(' | ')'

    ValidCharacter: Number | Operand | Parenthesis

    Expression: ValidCharacter*
'''
i = 4
string, solution = tests[i]

expression = Expression(string)

print(f"expression: {expression.string}")

print("expression to tree: ")

tree = expression.to_tree()
print(tree)
