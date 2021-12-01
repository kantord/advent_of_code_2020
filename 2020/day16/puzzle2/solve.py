import operator
import functools

with open('./input') as input_file:
    raw_data = input_file.read().split("\n\n")

nearby_tickets = list(map(lambda x: list(map(int, x.split(
    ","))), raw_data[2].strip().split("\n")[1:]))

my_ticket = list(map(lambda x: list(map(int, x.split(
    ","))), raw_data[1].strip().split("\n")[1:]))[0]

print(my_ticket)

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


error = False
valid_tickets = []

for nearby_ticket in nearby_tickets:
    error = False
    for number in nearby_ticket:
        valid_rules = get_valid_rules_for_number(number)
        if not valid_rules:
            error = True

    if not error:
        valid_tickets.append(nearby_ticket)

valid_fields_for_id = {
    i: set(map(lambda x: x[0], rules))
    for i, _ in enumerate(valid_tickets[0])
}

# print(valid_tickets)

for nearby_ticket in valid_tickets:
    for i, value in enumerate(nearby_ticket):
        valid_rules = set(map(
            lambda x: x[0],
            get_valid_rules_for_number(value)))
        valid_fields_for_id[i] = valid_fields_for_id[i].intersection(
            valid_rules)

# print(valid_fields_for_id)


while not all(len(x) == 1 for _, x in valid_fields_for_id.items()):
    for fields in valid_fields_for_id.values():
        if len(fields) != 1:
            continue

        field_to_keep = list(fields)[0]

        for i, fields in valid_fields_for_id.items():
            if len(fields) == 1:
                continue

            if field_to_keep in valid_fields_for_id[i]:
                valid_fields_for_id[i].remove(field_to_keep)


matching_field_indicies = {
    list(set_)[0]: i
    for i, set_ in valid_fields_for_id.items()
    if list(set_)[0].startswith("departure")
}


print(functools.reduce(operator.mul,
                       map(
                           lambda i: my_ticket[i],
                           matching_field_indicies.values()), 1))
