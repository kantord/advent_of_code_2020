import itertools
with open("./input") as input_file:
    raw_numbers = input_file.readlines()


def is_the_sum_of_any_combination(number, prev_numbers):
    for a, b in itertools.combinations(prev_numbers, 2):
        if a + b == number:
            return True
    return False


parsed_numbers = list(map(int, raw_numbers))
PREAMBLE_LENGTH = 25
indexer = range(PREAMBLE_LENGTH, len(parsed_numbers) - PREAMBLE_LENGTH)
for index, number in zip(indexer,  parsed_numbers[PREAMBLE_LENGTH:]):
    first_index_to_consider = index - PREAMBLE_LENGTH
    last_index_to_consider = first_index_to_consider + PREAMBLE_LENGTH
    print("Considering number {}: {}. Consider between {} and {}".format(
        index, number, first_index_to_consider, last_index_to_consider))
    numbers_to_consider = parsed_numbers[first_index_to_consider:last_index_to_consider]
    if not is_the_sum_of_any_combination(number, numbers_to_consider):
        print("{} is not the sum of any 2 of {}".format(
            number, numbers_to_consider))
        break
