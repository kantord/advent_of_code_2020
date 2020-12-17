import itertools
with open('./input') as input_file:
    raw_outlets = input_file.readlines()

outlets = set(map(int, raw_outlets))

# all_permutations = itertools.permutations(outlets, len(outlets))


# def is_valid_permutation(sequence):
# sequence_with_outlet = (0, ) + sequence
# for i in range(1, len(sequence_with_outlet)):
# value = sequence_with_outlet[i]
# previous_value = sequence_with_outlet[i - 1]
# if previous_value < value - 3:
# return False


# def get_valid_permutation(permutations):
# for permutation in permutations:
# if is_valid_permutation(permutation):
# return permutation


# valid_permutation = get_valid_permutation(all_permutations)
valid_permutation = tuple(sorted(outlets))
valid_permutation_with_outlet_and_device = (
    0, ) + valid_permutation + (valid_permutation[-1] + 3, )

differences = [
    abs(valid_permutation_with_outlet_and_device[i -
                                                 1] - valid_permutation_with_outlet_and_device[i])
    for i in range(1, len(valid_permutation_with_outlet_and_device))
]
one_jolt_diffs = list(filter(lambda x: x == 1, differences))
three_jolt_diffs = list(filter(lambda x: x == 3, differences))

print(len(one_jolt_diffs) * len(three_jolt_diffs))
