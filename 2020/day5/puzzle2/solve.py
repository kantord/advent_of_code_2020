def parse_seat_row(seat_string):
    return int(seat_string[0:7].replace("F", "0").replace("B", "1"), 2)


def parse_seat_column(seat_string):
    return int(seat_string[7:10].replace("L", "0").replace("R", "1"), 2)


def parse_seat(seat_string):
    return parse_seat_row(seat_string), parse_seat_column(seat_string)


def get_seat_id(seat):
    row, column = seat

    return row * 8 + column


with open('./input') as input_file:
    input_file_lines = input_file.readlines()

seat_ids = [get_seat_id(parse_seat(line)) for line in input_file_lines]

my_seat_id = [my_id for my_id in range(
    min(seat_ids), max(seat_ids)) if my_id not in seat_ids][0]

print(my_seat_id)
