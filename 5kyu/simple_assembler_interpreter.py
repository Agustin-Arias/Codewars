def get_value(x, registers):
    if x in registers.keys():
        return registers[x]
    return int(x)

def simple_assembler(program):
    registers = {}
    pointer = 0
    while pointer < len(program):
        s = program[pointer].split(' ')
        if s[0] == 'mov':
            x, y = s[1:]
            registers[x] = get_value(y, registers)
            pointer += 1
        elif s[0] == 'inc':
            x = s[1]
            registers[x] += 1
            pointer += 1
        elif s[0] == 'dec':
            x = s[1]
            registers[x] -= 1
            pointer += 1
        elif s[0] == 'jnz':
            x, y = s[1:]
            if get_value(x, registers) != 0:
                pointer += get_value(y, registers)
            else:
                pointer += 1
    return registers
