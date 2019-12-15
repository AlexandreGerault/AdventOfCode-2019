def list_from_file(filename_: str) -> list:
    file = open(filename_, 'r')
    return list(map(lambda x: int(x), file.readline().split(',')))


def code_at(pos_: int, inputs_: list) -> list:
    if inputs_[pos_] == 99:
        return [99]
    else:
        return [inputs_[pos_ + i] for i in range(0, 4)]


def run_intcode(noun: int, verb: int) -> int:
    inputs = list_from_file('input.txt')
    inputs[1], inputs[2], index = noun, verb, 0

    while index < len(inputs):
        code = code_at(index, inputs)
        opcode = code[0]

        if opcode == 1:
            inputs[code[3]] = inputs[code[1]] + inputs[code[2]]
        elif opcode == 2:
            inputs[code[3]] = inputs[code[1]] * inputs[code[2]]
        elif opcode == 99:
            break

        index += 4

    return inputs[0]


def find_inputs_for(expected: int) -> tuple:
    for noun in range(0, 99):
        for verb in range(0, 99):
            if run_intcode(noun, verb) == expected:
                return noun, verb


if __name__ == '__main__':
    result = find_inputs_for(19690720)
    print(result[0]*100 + result[1])
