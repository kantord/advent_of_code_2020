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

# print(program)
memory = dict()
mask = None


def get_actual_addresses(unmasked_address, mask):
    try:
        unmasked_address = list(unmasked_address)
        mask = list(mask)
        v = unmasked_address.pop()
        m = mask.pop()
        print(len(unmasked_address))
        for x in get_actual_addresses(list(unmasked_address), list(mask)):
            if m == "0":
                yield [v] + x
            if m == "1":
                yield ["1"] + x
            if m == "X":
                yield ["0"] + x
                yield ["1"] + x
    except GeneratorExit:
        pass
    except:
        yield []


for address, value in program:
    if address == "mask":
        mask = value
        continue
    address_as_string = list("{0:b}".format(address))
    unmasked_address = ["0"] * \
        (len(mask) - len(address_as_string)) + address_as_string
    actual_addresses = [
        "".join(x) for x in get_actual_addresses(unmasked_address, mask)
    ]
    print(actual_addresses)
    for address in actual_addresses:
        memory[address] = value

# print(memory)
memory_with_decimals = {
    key: int("".join(value), 2)
    for key, value in memory.items()}

# print(memory_with_decimals)

# assert memory_with_decimals[8] == 64
# assert memory_with_decimals[7] == 101

print(sum(memory_with_decimals.values()))
