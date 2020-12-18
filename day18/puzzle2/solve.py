with open('./input') as input_file:
    raw_input = [
        line.strip().replace(" ", "")
        for line in input_file.readlines()
    ]


# def evaluate(expression):
    # print("🍏", "".join(expression))
    # expression = list(expression)
    # operator = None
    # inside_parentheses = []
    # parenthesis_depth = 0
    # first_item = expression.pop(0)
    # if first_item == "(":
    # parenthesis_depth = 1
    # else:
    # value = int(first_item)

    # while expression:
    # if parenthesis_depth:
    # inside_parentheses.append(expression.pop(0))
    # next_ = expression.pop(0)
    # if next_ == "(":
    # parenthesis_depth += 1
    # if next_ == ")":
    # parenthesis_depth -= 1
    # inside_parentheses.append(next_)

    # if parenthesis_depth == 0:
    # if operator == '+':
    # print("value = ", value, "+",
    # evaluate(inside_parentheses[0:-1]))
    # value += evaluate(inside_parentheses[0:-1])
    # if operator == '*':
    # print("value = ", value, "*",
    # evaluate(inside_parentheses[0:-1]))
    # value *= evaluate(inside_parentheses[0:-1])
    # if operator == None:
    # value = evaluate(inside_parentheses[0:-1])
    # inside_parentheses = []
    # else:
    # operator = expression.pop(0)
    # right_hand_side = expression.pop(0)
    # if right_hand_side == "(":
    # parenthesis_depth += 1
    # else:
    # if operator == '+':
    # value += int(right_hand_side)
    # if operator == '*':
    # value *= int(right_hand_side)

    # print("🍎", value)
    # return value


def parse_number(x):
    print("💣 parse_number", x)
    return int(x[0]), x[1:]


assert parse_number("3") == (3, "")
assert parse_number("5") == (5, "")


def parse_parentheses(x):
    if not x[0] == "(":
        raise ValueError("")
    depth = 1
    parsed = ""
    unparsed = list(x[1:])
    while depth:
        next_ = unparsed.pop(0)
        if next_ == ")":
            depth -= 1
        if depth:
            parsed += next_
            if next_ == "(":
                depth += 1

    return parse_multiplication_expression(parsed)[0], "".join(unparsed)


def parse_parentheses_or_number(x):
    print('🦵 parse_parentheses_or_number', x)
    try:
        return parse_parentheses(x)
    except:
        print("trying to return a number instead of parse_parentheses")
        return parse_number(x)


def parse_addition(x):
    print("💩 parse_addition", x)
    lhs, remainder = parse_parentheses_or_number(x)
    op = remainder[0]
    print("🍫", lhs, remainder, op)
    if op != "*":
        raise ValueError()
    rhs, rem = parse_multiplication_expression(remainder[1:])

    return lhs * rhs, rem


def parse_multiplication(x):
    print('🍎parse_multiplication', x)
    lhs, remainder = parse_addition_expression(x)
    op = remainder[0]
    if op != "+":
        raise ValueError()
    try:
        rhs, rem = parse_number(remainder[1:])

        return lhs + rhs, rem
    except:
        rhs, rem = parse_multiplication_expression(remainder[1:])

        return lhs + rhs, rem


def parse_addition_expression(x):
    print('🍍 parse_addition_expression', x)
    try:
        return parse_addition(x)
    except:
        print("trying to return parse_parentheses_or_number instead of addition")
        return parse_parentheses_or_number(x)


def parse_multiplication_expression(x):
    try:
        return parse_multiplication(x)
    except:
        return parse_addition_expression(x)


assert parse_multiplication_expression("(5)") == (5, "")
assert parse_multiplication_expression("((5))") == (5, "")
assert parse_multiplication_expression("((5))5") == (
    5, "5"), parse_parentheses("((5))5")

assert parse_multiplication_expression("4+1") == (5, "")
assert parse_multiplication_expression("3+1+1") == (5, "")
assert parse_multiplication_expression("3+1+1+2") == (7, "")
assert parse_multiplication_expression("(4)+1") == (5, "")
assert parse_multiplication_expression("4+(1)") == (5, "")
assert parse_multiplication_expression("(4)+(1)") == (5, "")


assert parse_multiplication_expression("4*1")[0] == 4
assert parse_multiplication_expression("1+(2*3)+(4*(5+6))")[0] == (51)
assert parse_multiplication_expression("2*3+(4*5)")[0] == (46)
assert parse_multiplication_expression("8*3*5*4")[0] == 480
assert parse_multiplication_expression("8*6+9")[0] == 480 // 4
print("🍌" * 30)
assert parse_multiplication_expression("6+9*8")[0] != 6 + 9 * 8
assert parse_multiplication_expression("6+9*8")[0] == 480 // 4
assert parse_multiplication_expression("8*6+9*4")[0] == 480
assert parse_multiplication_expression("8*3+9+3*4")[0] == 480

assert parse_multiplication_expression("5+(8*3+9+3*4)")[0] == 485
# assert parse_multiplication_expression("5+(8*3+9+3*4*3)")
# 0] == (1445)
# assert parse_multiplication_expression(
# "5*9*(7*3*3+9*3+(8+6*4))")[0] == (669060)
# assert parse_multiplication_expression(
# "((2+4*9)*(6+9*8+6)+6)+2+4*2")[0] == (23340)
