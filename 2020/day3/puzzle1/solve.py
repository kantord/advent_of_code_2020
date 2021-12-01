with open("./input") as input_file:
    input_lines = input_file.readlines()


def is_tree_at_coordinate(column, row):
    line = input_lines[row]
    point = line[column % (len(line) - 1)]

    return point == "#"


assert is_tree_at_coordinate(0, 0) == False

path = [(y * 3, y) for y in range(1, len(input_lines))]
path_with_trees = [c for c in path if is_tree_at_coordinate(*c)]

for y in range(11):
    print("".join([("X" if (x, y) in path_with_trees else "#") if is_tree_at_coordinate(x, y)
                   else ("O" if (x, y) in path else ".") for x in range(30)]))

print(len(path_with_trees))
