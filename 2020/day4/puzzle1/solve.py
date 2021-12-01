import re

REQUIRED_FIELDS = [
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
    # "cid",
]


def validate_year(min_year, max_year):
    def validate(value):
        if not re.match("[0-9]{4}", value):
            return False

        parsed_year = int(value)

        return min_year <= parsed_year <= max_year

    return validate


def validate_height(value):
    match = re.match('([0-9]+)(cm|in)', value)
    if not match:
        return False

    raw_number, unit = match.groups()
    parsed_number = int(raw_number)
    print(parsed_number, unit)
    if unit == "cm":
        return 150 <= parsed_number <= 193

    if unit == "in":
        return 59 <= parsed_number <= 76

    return False


def validate_choice(choices):
    def validator(value):
        return value in choices

    return validator


VALIDATORS = {
    "byr": validate_year(1920, 2002),
    "iyr": validate_year(2010, 2020),
    "eyr": validate_year(2020, 2030),
    "hgt": validate_height,
    "hcl": re.compile("#[0-9a-f]{6}").match,
    "ecl": validate_choice(["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]),
    "pid": re.compile("[0-9]{9}").match,
}


def get_raw_passports():
    with open('./input') as input_file:
        input_data = input_file.read()

    return input_data.split('\n\n')


def parse_passport(passport):
    raw_fields = passport.replace("\n", " ").split(' ')
    parsed_passport = dict()

    for raw_field in raw_fields:
        if not raw_field:
            continue
        field_name, field_value = raw_field.split(':')
        parsed_passport[field_name] = field_value

    return parsed_passport


def is_valid_passport(passport):
    for field_name in REQUIRED_FIELDS:
        if field_name not in passport:
            return False

    for field_name, validator in VALIDATORS.items():
        if field_name not in passport:
            return False

        if not validator(passport[field_name]):
            return False

    return True


raw_passports = get_raw_passports()
parsed_passports = [parse_passport(passport) for passport in raw_passports]
valid_passports = [
    passport for passport in parsed_passports if is_valid_passport(passport)]

invalid_passports = [
    passport for passport in parsed_passports if not is_valid_passport(passport)]


print(len(valid_passports))
