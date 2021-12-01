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
        print(pointer, program[pointer], accumulator)
        if pointer in coverage:
            return accumulator
        coverage.add(pointer)
        active_instruction = program[pointer]
        command, argument = active_instruction
        if command == "acc":
            accumulator += argument
        if command == "jmp":
            pointer += argument
            continue
        pointer += 1


print(execute(parsed_commands))
