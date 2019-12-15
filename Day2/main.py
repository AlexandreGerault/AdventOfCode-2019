def list_from_file(filename_) -> list:
    file = open(filename_, 'r')
    return list(map(lambda x: int(x), file.readline().split(',')))


def code_at(pos_, inputs_):
    if inputs_[pos_] == 99:
        return [99]
    else:
        return [inputs_[pos_ + i] for i in range(0, 4)]


if __name__ == '__main__':
    inputs = list_from_file('input.txt')
    inputs[1], inputs[2], index = 12, 2, 0

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

    print(inputs[0])
