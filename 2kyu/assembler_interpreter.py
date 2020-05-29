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
        global line_number
        lbl = args[0]
        line_number = labels[lbl]
    def cmp(args):
        '''
            cmp  = 0 if equal
            cmp = 1 if x > y
            cmp = -1 if x < y
        '''
        global compare
        x, y = args[0].strip(', '), args[1]
        x, y = get_value(x, registers), get_value(y, registers)
        compare = (x > y) - (x < y)
    def jne(args):
        global line_number
        if compare != 0:
            lbl = args[0]
            line_number = labels[lbl]
    def je(args):
        global line_number
        if compare == 0:
            lbl = args[0]
            line_number = labels[lbl]
    def jge(args):
        global line_number
        if compare >= 0:
            lbl = args[0]
            line_number = labels[lbl]
    def jg(args):
        global line_number
        if compare == 1:
            lbl = args[0]
            line_number = labels[lbl]
    def jle(args):
        global line_number
        if compare <= 0:
            lbl = args[0]
            line_number = labels[lbl]
    def jl(args):
        global line_number
        if compare == -1:
            lbl = args[0]
            line_number = labels[lbl]
    def call(args):
        global line_number, line_number_reference, in_a_function
        lbl = args[0]
        if not in_a_function: line_number_reference, in_a_function = line_number, True
        line_number = labels[lbl]
    def ret(args):
        global line_number, line_number_reference, in_a_function
        line_number = line_number_reference
        in_a_function = False
    def msg(args):
        global output
        output = make_msg(message)
    def end(args):
        global line_number, program_ended_successfully
        program_ended_successfully = True
        line_number = total_lines
    def comment(args): pass
def set_up_environment(program):
    global processed_program, total_lines, registers, labels, commands, line_number, in_a_function
    line_number = 0
    in_a_function = False
    processed_program = remove_empty_spaces(remove_empty_strings(program.split('\n')))
    total_lines = len(processed_program)
    registers = {}
    labels = set_labels(processed_program)
    find_message(program)
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
def find_message(program):
    global message
    for line in program.split('\n'):
        if 'msg' in line:
            index = line.index('msg')
            message = line[3:].strip(' ')
def process_program(program):
    global processed_program
    processed_program = remove_empty_spaces(remove_empty_strings(program.split('\n')))
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
def make_msg(string):
    import re
    pattern = r"(', '|.|'.*?')"
    remove_comment = string[:string.index(';')].strip(' ') if ';' in string else string.strip(' ')
    message = re.findall(f"{pattern},", remove_comment) + re.findall(f", {pattern}$", remove_comment)
    print(message)
    output = ''
    for word in message:
        if word == ';':
            break
        elif word[0] == "'":  # if the word is a literal message, we join it with the ouput
            output += word.strip("'")
        else:
            output += str(get_value(word, registers))

    return output
def remove_empty_strings(string_list): return list(filter(lambda x: x.strip('') != '', string_list))
def remove_empty_spaces(processed_program): return [line.strip(' ') for line in processed_program]
def interpret_code(processed_program):
    global line_number, program_ended_successfully
    program_ended_successfully = False
    while line_number < total_lines:
        line = remove_empty_strings(processed_program[line_number].split(' '))
        command, args = line[0], line[1:]
        # print(line)
        do_command  = commands[command]
        do_command(args)
        # print(registers)
        line_number += 1
    if program_ended_successfully:
        return output
    return -1
def assembler_interpreter(program):
    set_up_commands()
    set_up_environment(program)
    process_program(program)
    print(message)
    set_labels(processed_program)
    return interpret_code(processed_program)



program = '''
mov c, 11   ; instruction mov c, 11
mov n, 6   ; instruction mov n, 6
call func
msg 'Random result: ', i
end

func:
    cmp c, n
    jl exit
    mov i, c
    mul i, n
    ret
; Do nothing
exit:
    msg 'Do nothing'
'''
print(assembler_interpreter(program))
