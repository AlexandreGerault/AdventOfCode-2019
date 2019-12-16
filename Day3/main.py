def list_from_file(filename_: str) -> list:
    file = open(filename_, 'r')
    return [
        list(map(lambda x: (x[0], int(x[1:])), file.readline().split(','))),
        list(map(lambda x: (x[0], int(x[1:])), file.readline().split(',')))
    ]


def distance(point_: tuple) -> int:
    return abs(point_[0]) + abs(point_[1])


def wire_to_grid(wire_: list) -> list:
    current_corner = (0, 0)
    grid = list()
    for movement in wire_:
        x, y = 0, 0

        if movement[0] == 'R':
            x = 1
        elif movement[0] == 'L':
            x = -1
        elif movement[0] == 'U':
            y = 1
        elif movement[0] == 'D':
            y = -1

        amount = movement[1]

        for i in range(amount):
            current_corner = (current_corner[0] + x, current_corner[1] + y)
            grid.append(current_corner)

    return grid


def cross_points(wire1_: list, wire2_: list) -> list:
    result = list(set(wire1_) & set(wire2_))
    return result


if __name__ == "__main__":
    wires = list_from_file('input.txt')

    wire_grid_1 = wire_to_grid(wires[0])
    wire_grid_2 = wire_to_grid(wires[1])

    my_cross_points = cross_points(wire_grid_1, wire_grid_2)
    closest_point = my_cross_points[0]

    for cross_point in my_cross_points:
        print('Cross point: {}\nClosest point: {}\n'.format(cross_point, closest_point))
        if distance(closest_point) > distance(cross_point): closest_point = cross_point

    print("Closest cross point distance: {}".format(distance(closest_point)))


