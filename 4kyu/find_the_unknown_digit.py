# Find the unknown digit
# https://www.codewars.com/kata/546d15cebed2e10334000ed9
import re
def solve_runes(string):
    print(string)
    numbers = re.compile(r'\d')  # we get every instance of a digit
    set1 = set(int(number) for number in numbers.findall(string))
    set2 = set(list(range(10)))
    possible_digits = set2.difference(set1)  # we dont check these digits

    check1 = re.compile(r'[^0123456789\?]\?{2,}')  # we check for (operator)??
    check2 = re.compile(r'[\+\-\*=]\?\d+')  # we check for ?(digits)
    print(check1.search(string))
    print(check2.search(string))
    if check1.search(string) != None or check2.search(string) != None:
        if 0 in possible_digits:
            possible_digits.remove(0)  # if this happens we remove 0
            print(2, '0 removed')

    foo = string.split('=')
    print(possible_digits)
    if 0 in possible_digits:
        for bar in foo:
            print(bar)
            if bar[0] == '-':
                if bar[1] == '?':
                    print('0 removed')
                    possible_digits.remove(0)
            elif bar[0] == '?':
                if len(bar) > 1:
                    if bar[1].isdecimal() or bar[1] == '?':
                        print('0 removed')
                        possible_digits.remove(0)
    possible_digits = sorted(list(possible_digits))
    replace = re.compile(r'\?')  # we replace ? for every digit in possible_digits
    for digit in possible_digits:
        print('Checking ' + str(digit) + '..')
        print()
        output_string = replace.sub(str(digit), string)
        expressions = output_string.split('=')

        lefthandside = expressions[0].strip()  # we remove any blank spaces
        righthandside = expressions[1].strip()  # we remove any blank spaces
        if eval(lefthandside) == eval(righthandside):
            print('Done:')
            print(lefthandside + '=' + righthandside)
            return digit  # if we find a match, we return the digit
    print('No digit was found.')
    return -1  # else we return -1

string = '1278--28726=3???4'
print(solve_runes(string))
