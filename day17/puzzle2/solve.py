import collections
import functools

with open('./input') as input_file:
    raw_input = input_file.readlines()

print(raw_input)


state = collections.defaultdict(lambda: ".")
counts = collections.defaultdict(lambda: 0)


def get_neighbors(x, y, z, n):
    for a in range(-1, 2):
        for b in range(-1, 2):
            for c in range(-1, 2):
                for d in range(-1, 2):
                    if not all(n == 0 for n in [a, b, c, d]):
                        yield x + a, y + b, z + c, n + d


# assert len(list(get_neighbors(0, 0, 0))) == 26


def set_cell_active(coordinates):
    if state[coordinates] == ".":
        state[coordinates] = "#"
        for neighbor in get_neighbors(*coordinates):
            counts[neighbor] += 1


def set_cell_inactive(coordinates):
    if state[coordinates] == "#":
        state[coordinates] = "."
        for neighbor in get_neighbors(*coordinates):
            counts[neighbor] -= 1


for y, row in enumerate(raw_input):
    for x, character in enumerate(row):
        if character == "#":
            set_cell_active((x, y, 0, 0))


for i in range(6):
    print(i, sum(1 for v in state.values() if v == "#"))
    all_coordinates_to_check = set(state.keys()).union(functools.reduce(
        lambda acc, curr: acc.union(set(get_neighbors(*curr))), state.keys(), set()))
    to_set_active = set()
    to_set_inactive = set()

    for coordinate in all_coordinates_to_check:
        value = state[coordinate]
        if value == "#" and counts[coordinate] not in (2, 3):
            to_set_inactive.add(coordinate)
        if value == "." and counts[coordinate] == 3:
            to_set_active.add(coordinate)

    for x in to_set_active:
        set_cell_active(x)

    for x in to_set_inactive:
        set_cell_inactive(x)


print(sum(1 for v in state.values() if v == "#"))
