def east(p, d, v):
    x, y = p
    return (x + v, y), d


def south(p, d, v):
    x, y = p
    return (x, y + v), d


def west(p, d, v):
    x, y = p
    return (x - v, y), d


def north(p, d, v):
    x, y = p
    return (x, y - v), d


def forward(p, d, v):
    return d(p, d, v)


def left(p, d, v):
    index = DIRECTIONS.index(d)
    c = v // 90
    return p, DIRECTIONS[(index - c) % len(DIRECTIONS)]


def right(p, d, v):
    index = DIRECTIONS.index(d)
    c = v // 90
    return p, DIRECTIONS[(index + c) % len(DIRECTIONS)]


DIRECTIONS = (west, north, east, south)


def parse_instruction(raw_instruction):
    if raw_instruction == "N":
        return north
    if raw_instruction == "S":
        return south
    if raw_instruction == "E":
        return east
    if raw_instruction == "W":
        return west
    if raw_instruction == "L":
        return left
    if raw_instruction == "R":
        return right
    if raw_instruction == "F":
        return forward

    0/0


def parse_command(raw_command):
    raw_instruction = raw_command[0]
    value = int(raw_command[1:].strip())

    return parse_instruction(raw_instruction), value


with open('./input') as input_file:
    raw_commands = input_file.readlines()

parsed_commands = list(map(parse_command, raw_commands))

p = 0, 0
d = east

for instruction, value in parsed_commands:
    print(p, d)
    p, d = instruction(p, d, value)

print("END", p)
print(abs(p[0]) + abs(p[1]))
