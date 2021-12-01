import functools

with open("./input") as input_file:
    input_lines = input_file.readlines()


def debug(path_with_trees, path):
    for y in range(11):
        print("".join([("X" if (x, y) in path_with_trees else "#") if is_tree_at_coordinate(x, y)
                       else ("O" if (x, y) in path else ".") for x in range(30)]))

    print(path)
    print(len(path_with_trees))


def is_tree_at_coordinate(column, row):
    line = input_lines[row]
    point = line[column % (len(line) - 1)]

    return point == "#"


assert is_tree_at_coordinate(0, 0) == False


slopes = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2),
]


def calculate_slope(down, right):
    path = [(y * right // down, y)
            for y in range(down, len(input_lines), down)]
    path_with_trees = [c for c in path if is_tree_at_coordinate(*c)]

    debug(path_with_trees, path)

    return len(path_with_trees)


all_trees = [calculate_slope(down, right) for right, down in slopes]

print(all_trees)

print(functools.reduce(lambda a, b: a * b, all_trees))
