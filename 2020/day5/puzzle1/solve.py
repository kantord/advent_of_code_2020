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

parsed_seats = [parse_seat(line) for line in input_file_lines]

highest_seat_id = max(get_seat_id(seat) for seat in parsed_seats)

print(highest_seat_id)
