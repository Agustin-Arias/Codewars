# import re

# def make_output(msg_parameters, registers):
#     print(msg_parameters)
#     output = ''
#     count = 0
#     for parameter in msg_parameters:
#         if count == 0:
#             if parameter == "'":
#                 count += 1
#             elif parameter == parameter.strip("'"):
#                 # parameter was a register
#                 print(parameter)
#                 output += str(registers[parameter])
#             else:
#                 # parameter was a string:
#                 output += parameter.strip("'")
#         elif count == 1 and parameter == "'":
#             output += ','
#             count = 0
#     return output


# def assembler_interpreter(program):
#     prog = list(filter(lambda x : x!= '', program.splitlines()))
#     labels = set_labels(prog)  # label: line_pointer
#     registers = {}
#     line_pointer = 0 # vertically

#     while line_pointer < len(prog):
#         skip = False
#         line = remove_empty_strings(prog[line_pointer].split(' '))
#         print(' '.join(line), line_pointer)
#         # print(f'registers: {registers}')
#         word = line[0]

#         if word == ';':
#             line_pointer += 1
#             skip = True

#         elif word == 'cmp':
#             x, y = line[1].strip(','), line[2]
#             greater, equal = get_value(x, registers) > get_value(y, registers), get_value(x, registers) == get_value(y, registers)

#         elif word == 'jne':
#             lbl = line[1]
#             if not equal:
#                 line_pointer = labels[lbl]
#                 skip = True

#         elif word == 'je':
#             lbl = line[1]
#             if equal:
#                 line_pointer = labels[lbl]
#                 skip = True

#         elif word == 'jge':
#             lbl = line[1]
#             if greater or equal:
#                 line_pointer = labels[lbl]
#                 skip = True

#         elif word == 'jg':
#             lbl = line[1]
#             if greater:
#                 line_pointer = labels[lbl]
#                 skip = True

#         elif word == 'jle':
#             lbl = line[1]
#             if not greater or equal:
#                 line_pointer = labels[lbl]
#                 skip = True

#         elif word == 'jl':
#             lbl = line[1]
#             if not greater:
#                 line_pointer = labels[lbl]
#                 skip = True

#         elif word == 'call':
#             line_pointer_call = line_pointer  # we set the references
#             lbl = line[1]
#             line_pointer = labels[lbl]  # we jump to the label
#             # print(f"line_pointer: {line_pointer}")
#             skip = True

#         elif word == 'msg':
#             string_line = prog[line_pointer]
#             msg_parameters = re.search(r"msg (.*) ;?", string_line).groups()[0].split(',')
#             msg_parameters = remove_empty_strings([x.strip(" ") for x in msg_parameters])
#             output = make_output(msg_parameters, registers)
#             line_pointer += 1
#             skip = True

#         elif word == 'end':
#             return output

#         import time, sys
#         time.sleep(1)
#         sys.stdout.flush()

#         if not skip:

#     return -1

def set_up_commands():
    global mov, inc, dec, add, sub, mul, div, jmp, cmp, jne, je, jge, jg, jle, jl, call, ret, msg, end, comment
    def mov(args):
        x, y = args[0].strip(', '), args[1]
        registers[x] = get_value(y, registers)
    def inc(args):
        x = args[0]
        registers[x] += 1
    def dec(args):
        x = args[0]
        registers[x] -= 1
    def add(args):
        x, y = args[0].strip(', '), args[1]
        registers[x] += get_value(y, registers)
    def sub(args):
        x, y = args[0].strip(', '), args[1]
        registers[x] -= get_value(y, registers)
    def mul(args):
        x, y = args[0].strip(', '), args[1]
        registers[x] *= get_value(y, registers)
    def div(args):
        x, y = args[0].strip(', '), args[1]
        registers[x] //= get_value(y, registers)
    def jmp(args):
        global line_number, line_number_reference
        lbl = args[0]
        line_number_reference = line_number
        line_number = labels[lbl]
    def cmp(args):
        '''
            cmp  = 0 if equal
            cmp = 1 if x > y
            cmp = -1 if x < y
        '''
        global compare
        x, y = args[0].strip(', '), args[1]
        compare = (x > y) - (x < y)
    def jne(args): pass
    def je(args): pass
    def jge(args): pass
    def jg(args): pass
    def jle(args): pass
    def jl(args): pass
    def call(args): pass
    def ret(args):
        global line_number
        line_number = line_number_reference
    def msg(args): pass
    def end(args):
        global line_number
        line_number = total_lines
    def comment(args): pass
def set_up_environment(program):
    global processed_program, total_lines, registers, labels, commands, line_number
    line_number = 0
    processed_program = remove_empty_spaces(remove_empty_lines(program))
    total_lines = len(processed_program)
    registers = {}
    labels = set_labels(processed_program)
    commands = {
        'mov' : mov,
        'inc' : inc,
        'dec' : dec,
        'add' : add,
        'sub' : sub,
        'mul' : mul,
        'div' : div,
        'jmp' : jmp,
        'cmp' : cmp,
        'jne' : jne,
        'je' : je,
        'jge' : jge,
        'jg' : jg,
        'jle' : jle,
        'jl' : jl,
        'call' : call,
        'ret' : ret,
        'msg' : msg,
        'end' : end,
        ';' : comment
    }
def set_labels(processed_program):
    labels = {}
    for index, line in enumerate(processed_program):
        if line[-1] == ':':
            labels[line[:-1]] = index
    return labels
def get_value(x, registers):
    if x in registers.keys():
        return registers[x]
    return int(x)
def remove_empty_lines(program): return list(filter(lambda x: x.strip('') != '', program.split('\n')))
def remove_empty_spaces(processed_program): return [line.strip(' ') for line in processed_program]
def assembler_interpreter(program):
    global line_number
    while line_number < total_lines:
        line = processed_program[line_number].split(' ')
        command, args = line[0], line[1:]
        do_command  = commands[command]
        do_command(args)
        line_number += 1

program = '''
mov a, 2
inc a
add a, 4
jmp function
cmp a, b
end

function:
    mov b, 5
    sub a, b
    ret
'''
set_up_commands()
set_up_environment(program)
processed_program = remove_empty_spaces(remove_empty_lines(program))
set_labels(processed_program)
assembler_interpreter(program)


print(registers)
