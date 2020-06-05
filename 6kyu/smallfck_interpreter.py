# Esolang Interpreters #2 - Custom Smallfuck Interpreter
# https://www.codewars.com/kata/58678d29dbca9a68d80000d7/solutions/python
def interpreter(code, tape):
    print(code, tape)
    translation, pointer, pointer_limit = list(map(int, tape)), 0, len(tape)
    index_of_code, index_limit = 0, len(code)
    loops = []
    while index_of_code < index_limit and pointer >= 0 and pointer < pointer_limit:
        command = code[index_of_code]
        print(command, index_of_code, loops, ''.join(str(bit) for bit in translation))
        if pointer >= pointer_limit:
            break
        if command == '>':
            pointer += 1
        elif command == '<':
            pointer -= 1
        elif command == '*':
            translation[pointer] += 1
            translation[pointer] %= 2
        elif command == '[':
            if translation[pointer] == 0:
                index_of_code += 1
                # print(code, index_of_code)
                in_inside_loop = False
                while index_of_code < index_limit:
                    # print(222, code[index_of_code], in_inside_loop)
                    if code[index_of_code] == '[':
                        in_inside_loop = True
                    elif code[index_of_code] == ']':
                        if in_inside_loop:
                            in_inside_loop = False
                        else:
                            break
                    index_of_code +=1
                # print(index_of_code)
            else:
                loops.append(index_of_code)
        elif command == ']':
            if translation[pointer] == 1:
                index_of_code = loops[-1]
            loops.pop()
        index_of_code += 1
    return ''.join(str(bit) for bit in translation)
code, tape ="[*>[>*>]>] 11001".split(' ')
print(interpreter(code, tape))
