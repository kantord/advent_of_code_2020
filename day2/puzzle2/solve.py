def is_valid(line):
    rule_source, password = line.split(': ')
    range_rule, character = rule_source.split(' ')
    pos1_str, pos2_str = range_rule.split('-')
    pos1 = int(pos1_str)
    pos2 = int(pos2_str)
    characters = [password[pos1 - 1], password[pos2 - 1]]
    return len(list(filter(lambda c: c == character, characters))) == 1


with open("./input") as input_file:
    input_values = input_file.readlines()


valid_passwords = list(filter(is_valid, input_values))
solution = len(valid_passwords)

print(solution)
