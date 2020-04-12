import re


def take_second(x): return x[1]

def take_first(x): return x[0]

def return_string(lis):  # given a list of the form [(expression, number)], returns: number expression + (or -) number' expression' + ...
    first = lis[0]
    result = ''
    if first[1] == 1:
        result = first[0]
    elif first[1] == -1:
        result = '-' + first[0]
    else:
        result += str(first[1]) + first[0]
    for expression,number in lis[1:]:
        if number == 1:
            result = result + '+' + expression
        elif number == -1:
            result = result + '-' + expression
        elif number > 0:
            result = result + '+' + str(number) + expression
        else:
            result = result + str(number) + expression
    return result 


def simplify(string):
    regex_plus = re.compile(r'\+(\d*)(\w+)')  # this is the regular expression of '+(digit [or not])(letters)'
    regex_minus = re.compile(r'\-(\d*)(\w+)')  # this is the regular expression of '-(digit [or not])(letters)'

    dic_plus = {}
    if string[0] != '-':
        regex = re.compile(r'(\d*)(\w+)')
        double = regex.search(string).groups()
        ordered_expression = ''.join(sorted(double[1]))
        dic_plus.setdefault(ordered_expression,1)
        if double[0] != '':
            dic_plus[ordered_expression] = int(double[0])
            
    foo = [(expression[0], ''.join(sorted(expression[1]))) for expression in regex_plus.findall(string)]
    bar = [(expression[0], ''.join(sorted(expression[1]))) for expression in regex_minus.findall(string)]

    foo.sort(key = take_second)
    bar.sort(key = take_second)
    print('foo', foo)
    print('bar', bar)
  
    for tupl in foo:
        key = tupl[1]
        if tupl[0] != '':
            dic_plus.setdefault(key,0)
            dic_plus[key] += int(tupl[0])
        else:
            dic_plus.setdefault(key,1)
    print('dic_plus', dic_plus)
    dic_minus = {}
    for tupl in bar:
        key = tupl[1]
        if tupl[0] != '':
            dic_minus.setdefault(key,0)
            dic_minus[key] -= int(tupl[0])
        else:  # this means expression is of the form '-expresion'
            dic_minus.setdefault(key,0)
            dic_minus[key] -= 1
    print('dic_minus', dic_minus)
   
    for key, value in dic_minus.items():
        dic_plus.setdefault(key,0)
        dic_plus[key] += value
    print('dic_pluss', dic_plus)
    final_dic = {}
    for key, value in dic_plus.items():
        if value != 0:
            final_dic[key] = value
            
    final = sorted(list(final_dic.items()),key = take_first)
    final.sort(key = lambda x: len(take_first(x)))
    return return_string(final)

string = '3a+b+4ac+bc-ab+3a-cb-a-a'
print(string)
print(simplify(string))
