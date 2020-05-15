# Simple Finite State Machine Compiler
# https://www.codewars.com/kata/59923f1301726f5430000059/train/python
class FSM(object):

    def __init__(self, instructions):
        instructions = instructions.split("\n")
        sections = [instruction.split(";") for instruction in instructions]
        self.next_if = {section[0]: section[1].strip().split(", ") for section in sections}
        self.output = {section[0]: int(section[2]) for section in sections}

    def run_fsm(self, start, sequence):
        # return tuple: (final_state, final_state_output, path)
        print(f"start: {start}")
        print("sequence: ", *sequence, end= "\n"*2)

        path = [start]
        nextins = start
        for num in sequence:
            print(f"input {num}: {nextins}->", end = "")
            nextins = self.next_if[nextins][num]
            path.append(nextins)
            print(f"{nextins}")

        print()
        print(f"final state: {nextins}")
        print(f"output: {self.output[nextins]}\n")

        return nextins, self.output[nextins], path

instructions = '''S1; S1, S2; 9
S2; S1, S3; 10
S3; S4, S3; 8
S4; S4, S1; 0'''
fsm = FSM(instructions)
# print(fsm.next_if)
# print(fsm.output)

start = 'S1'
sequence = [0, 1, 1, 0, 1]

print(fsm.run_fsm(start, sequence))


