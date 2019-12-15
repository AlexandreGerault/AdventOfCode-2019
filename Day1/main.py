from functools import reduce


def required_module_fuel(mass_: int) -> int:
    return int(mass_ / 3) - 2


def list_from_file(filename) -> list:
    file = open(filename, 'r')
    return list(map(lambda x: int(x.rstrip()), file.readlines()))


if __name__ == '__main__':
    modules_mass = list_from_file('input.txt')
    result = reduce(lambda acc, item: acc + required_module_fuel(item), modules_mass, 0)

    print(result)
