import collections
with open('./input') as input_file:
    raw_input = input_file.readline().strip()

numbers = list(map(int, raw_input.split(',')))
turns = len(numbers)

last_spoken = collections.defaultdict(list)

for i, n in enumerate(numbers):
    last_spoken[n].append(i + 1)

N = 2020

while len(numbers) < N:
    print(str(round(len(numbers) / N * 100)) + "%")
    last_number = numbers[-1]
    # print("🍎", last_number)
    turns += 1
    if len(last_spoken[last_number]) < 2:
        last_spoken[0].append(turns)
        numbers.append(0)
    else:
        number = last_spoken[last_number][-1] - last_spoken[last_number][-2]
        last_spoken[number].append(turns)
        numbers.append(number)

# print(numbers)
print(numbers[-1])
# assert numbers[3] == 0
# assert numbers[4] == 3
