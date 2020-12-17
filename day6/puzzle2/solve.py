with open('./input') as input_file:
    input_data = input_file.read()

groups = [[set(person) for person in line.split('\n') if person]
          for line in input_data.split("\n\n")]

# print(groups)


def yes_answers_of_group(group):
    if len(group) == 1:
        return group[0]

    return set(group[0]).intersection(yes_answers_of_group(group[1:]))


print(groups)
yes_answers_per_group = [yes_answers_of_group(
    group) for group in groups]
print(yes_answers_per_group)
solution = sum(len(group) for group in yes_answers_per_group)

print(solution)
