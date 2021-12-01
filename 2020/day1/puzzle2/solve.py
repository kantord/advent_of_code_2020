import itertools

with open("./input") as input_file:
    input_values = map(lambda line: int(line), input_file.readlines())

all_combinations = itertools.combinations(input_values, 3)
correct_combinations = filter(lambda pair: sum(pair) == 2020, all_combinations)
a, b, c = list(correct_combinations)[0]
solution = a * b * c

print(solution)
