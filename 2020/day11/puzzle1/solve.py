with open("./input") as input_file:
    rows = [list(line.strip()) for line in input_file.readlines()]

ROWS = len(rows)
COLUMNS = len(rows[0])


def is_seat(pos):
    return pos != "."


def is_free(pos):
    return pos == "L"


# def normalize_coordinate(row_index, column_index):
    # return (
    # min(max(row_index, 0), ROWS - 1),
    # min(max(column_index, 0), COLUMNS - 1),
    # )


def adjacent_indices(row_index, column_index):
    for a in range(-1, 2):
        for b in range(-1, 2):
            if row_index + a < 0:
                continue

            if row_index + a >= ROWS:
                continue

            if column_index + b < 0:
                continue

            if column_index + b >= COLUMNS:
                continue

            if a == 0 and b == 0:
                continue

            yield row_index + a, column_index + b

            # return set(
            # normalize_coordinate(row_index + a, column_index + b)
            # for b in [-1, 1]
            # for a in [-1, 1]
            # )


occupied_counts = [[0 for _ in rows[0]] for _ in rows]
i = 0
changed = True
change_count = 0

while changed:
    print("🍎" * 20, i, change_count)
    for row in rows:
        print("".join(row))
    i += 1
    changed = False
    change_count = 0
    changes = set()
    count_changes = list()
    for row_index in range(len(rows)):
        for column_index in range(len(rows[0])):
            pos = rows[row_index][column_index]
            if not is_seat(pos):
                continue

            if is_free(pos) and occupied_counts[row_index][column_index] == 0:
                changes.add((row_index, column_index, "#"))
                for y, x in adjacent_indices(row_index, column_index):
                    count_changes.append((x, y, 1))

            if not is_free(pos) and occupied_counts[row_index][column_index] >= 4:
                changes.add((row_index, column_index, "L"))
                for y, x in adjacent_indices(row_index, column_index):
                    count_changes.append((x, y, -1))

    for row_index, column_index, value in changes:
        rows[row_index][column_index] = value

    for x, y, value in count_changes:
        occupied_counts[y][x] += value
        changed = True
        change_count += 1

    print(changed, occupied_counts)

occupied = 0
for row in rows:
    for seat in row:
        if is_seat(seat) and not is_free(seat):
            occupied += 1

print('Result {}'.format(occupied))
