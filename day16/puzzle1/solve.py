with open('./input') as input_file:
    raw_data = input_file.read().split("\n\n")

nearby_tickets = list(map(lambda x: list(map(int, x.split(
    ","))), raw_data[2].strip().split("\n")[1:]))

rules = list(map(
    lambda x: (x[0], tuple(
        map(
            lambda x: tuple(map(int, x.split("-"))),
            x[1].split(" or ")))),
    list(map(
        lambda x: x.split(": "), raw_data[0].split('\n')))))


def get_valid_rules_for_number(number):
    valid_rules = []
    for rule in rules:
        _, ranges = rule
        for range_ in ranges:
            min_, max_ = range_
            if min_ <= number <= max_:
                valid_rules.append(rule)
                break
    return valid_rules


error_rate = 0

for nearby_ticket in nearby_tickets:
    for number in nearby_ticket:
        valid_rules = get_valid_rules_for_number(number)
        if not valid_rules:
            error_rate += number

print(error_rate)
