def north(p, wp, v):
    x, y = wp
    return p, (x + v, y)


def east(p, wp, v):
    x, y = wp
    return p, (x, y + v)


def south(p, wp, v):
    x, y = wp
    return p, (x - v, y)


def west(p, wp, v):
    x, y = wp
    return p, (x, y - v)


def forward(p, wp, v):
    x, y = p
    a, b = wp
    return (x + a * v, y + b * v), wp


def right(p, wp, v):
    c = v // 90
    new_wp = wp
    for _ in range(c):
        x, y = new_wp
        new_wp = (-y, x)
    return p, new_wp


def left(p, wp, v):
    return right(p, wp, 360 - v)


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
# d = east
wp = 1, 10

for instruction, value in parsed_commands:
    print(p, wp)
    p, wp = instruction(p, wp, value)

print("END", p)
print(abs(p[0]) + abs(p[1]))

# F10 (10, 100), (1, 10)
# N3 (10, 100), (4, 10)
# F7 (38, 1700, (4, 10)
# R90 (38, 1700, (-10, 4)
# R90 rotates the waypoint around the ship clockwise 90 degrees, moving it to 4 units east and 10 units south of the ship. The ship remains at east 170, north 38.
# F11 moves the ship to the waypoint 11 times (a total of 44 units east and 110 units south), leaving the ship at east 214, south 72. The waypoint stays 4 units east and 10 units south of the ship.
