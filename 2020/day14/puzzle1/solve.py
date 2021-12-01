with open("./input") as input_file:
    lines = input_file.readlines()

program = [
    (int(address.split('[')[1].split(']')[0]),
     list("{0:b}".format(int(value.strip())))
     ) if address != "mask" else (
         "mask", list(value.strip())
    )
    for address, value in [
        line.split(" = ")
        for line in
        lines]
]

print(program)
memory = dict()
mask = None

for address, value in program:
    if address == "mask":
        mask = value
        continue
    value_to_mask = ["0"] * (len(mask) - len(value)) + value
    masked_value = [m if m != "X" else v for v, m in zip(value_to_mask, mask)]
    memory[address] = masked_value

print(memory)
memory_with_decimals = {
    key: int("".join(value), 2)
    for key, value in memory.items()}

print(memory_with_decimals)

# assert memory_with_decimals[8] == 64
# assert memory_with_decimals[7] == 101

print(sum(memory_with_decimals.values()))
