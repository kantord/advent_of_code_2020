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
# valid_permutation = tuple(sorted(outlets))
# valid_permutation_with_outlet_and_device = (
# 0, ) + valid_permutation + (valid_permutation[-1] + 3, )

# differences = [
# abs(valid_permutation_with_outlet_and_device[i -
# 1] - valid_permutation_with_outlet_and_device[i])
# for i in range(1, len(valid_permutation_with_outlet_and_device))
# ]
# one_jolt_diffs = list(filter(lambda x: x == 1, differences))
# three_jolt_diffs = list(filter(lambda x: x == 3, differences))

# print(len(one_jolt_diffs) * len(three_jolt_diffs))


# def get_valid_permutations(has_so_far, still_to_go):
# print(len(still_to_go))
# prev_item = has_so_far[-1]
# if not still_to_go:
# yield has_so_far
# for next_item in still_to_go[0:3]:
# if prev_item >= next_item:
# continue

# if prev_item + 3 < next_item:
# continue

# new_still_to_go = sorted(
# filter(lambda x: x >= next_item, set(still_to_go) - {next_item, }))

# for solution in get_valid_permutations(has_so_far + (next_item, ), new_still_to_go):
# yield solution


# valid_permutations = list(get_valid_permutations((0, ), sorted(outlets)))
# print(valid_permutations)
# print(len(valid_permutations))

device = max(outlets) + 3


# def count_ways_to_arrange(current_outlet):
# if current_outlet > biggest_adapter:
# return 0

# if current_outlet == biggest_adapter:
# return 1

# return count_ways_to_arrange(current_outlet + 1) + \
# count_ways_to_arrange(current_outlet + 2) + \
# count_ways_to_arrange(current_outlet + 3)


# print(count_ways_to_arrange(0))

adapters = [0, ] + sorted(outlets) + [device]
ways_to_reach = [0 for _ in adapters]
ways_to_reach[0] = 1
print(adapters)

for i in range(len(adapters)):
    print(ways_to_reach)
    for j in range(i + 1, len(adapters)):
        if (adapters[j] - adapters[i] > 3):
            break
        ways_to_reach[j] += ways_to_reach[i]

print(ways_to_reach[-1])
