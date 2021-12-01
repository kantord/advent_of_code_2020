def is_valid(line):
    rule_source, password = line.split(': ')
    range_rule, character = rule_source.split(' ')
    min_count_str, max_count_str = range_rule.split('-')
    min_count = int(min_count_str)
    max_count = int(max_count_str)
    actual_count = len(list(c for c in password if c == character))

    return min_count <= actual_count <= max_count


with open("./input") as input_file:
    input_values = input_file.readlines()


valid_passwords = list(filter(is_valid, input_values))
solution = len(valid_passwords)

print(solution)
