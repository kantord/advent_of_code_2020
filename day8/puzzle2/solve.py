with open('./input') as input_file:
    raw_commands = input_file.readlines()


def parse_command(raw_command):
    command, raw_argument = raw_command.split(' ')
    return (command, int(raw_argument))


parsed_commands = list(map(parse_command, raw_commands))


def execute(program):
    pointer = 0
    accumulator = 0
    coverage = set()
    while True:
        if pointer >= len(program):
            print("Exiting at line", pointer)
            return accumulator
        print(pointer, program[pointer], accumulator)
        if pointer in coverage:
            print("🍎Got into a loop!")
            return

        coverage.add(pointer)
        active_instruction = program[pointer]
        command, argument = active_instruction
        if command == "acc":
            accumulator += argument
        if command == "jmp":
            pointer += argument
            continue
        pointer += 1


def variants(program):
    for i in range(len(program)):
        print("Variant ", i)
        command = program[i]
        instruction, argument = command
        if instruction in ["jmp", "nop"]:
            yield program[0:i] + [("jmp", argument)] + program[i+1:]
            yield program[0:i] + [("nop", argument)] + program[i+1:]


def get_correct_variant(program):
    for variant in variants(program):
        assert len(variant) == len(program), (len(variant), len(program))
        result = execute(variant)
        if result:
            return result


print(get_correct_variant(parsed_commands))
