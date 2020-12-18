import inspect
import functools

with open('./input') as input_file:
    raw_input = [
        line.strip().replace(" ", "")
        for line in input_file.readlines()
    ]


def magicprint(*t):
    print(" "*4*len(inspect.stack()), *t)


# def evaluate(expression):
    # magicprint("🍏", "".join(expression))
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
    # magicprint("value = ", value, "+",
    # evaluate(inside_parentheses[0:-1]))
    # value += evaluate(inside_parentheses[0:-1])
    # if operator == '*':
    # magicprint("value = ", value, "*",
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

    # magicprint("🍎", value)
    # return value


def parse_number(x):
    magicprint("💣 parse_number", x)
    return int(x[0]), x[1:]


assert parse_number("3") == (3, "")
assert parse_number("5") == (5, "")


def alt_(a, b):
    def p(x):
        try:
            return a(x)
        except:
            return b(x)

    return p


def alt(*ps):
    return functools.reduce(alt_, ps[1:], ps[0])


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


# def parse_parentheses_or_number(x):
    # magicprint('🦵 parse_parentheses_or_number', x)
    # try:
    # return parse_parentheses(x)
    # except:
    # magicprint("trying to return a number instead of parse_parentheses")
    # return parse_number(x)


parse_parentheses_or_number = alt(parse_parentheses, parse_number)


def parse_addition(x):
    magicprint("💩 parse_addition", x)
    lhs, remainder = parse_parentheses_or_number(x)
    op = remainder[0]
    magicprint("🍫", lhs, remainder, op)
    if op != "*":
        raise ValueError()
    rhs, rem = parse_multiplication_expression(remainder[1:])

    return lhs * rhs, rem


def parse_multiplication(x):
    magicprint('🍎parse_multiplication', x)
    lhs, remainder = parse_addition_expression(x)
    op = remainder[0]
    if op != "+":
        raise ValueError()
    rhs, rem = parse_multiplication_expression(remainder[1:])

    return lhs + rhs, rem


# def parse_addition_expression(x):
    # magicprint('🍍 parse_addition_expression', x)
    # try:
    # return parse_addition(x)
    # except:
    # magicprint(
    # "trying to return parse_parentheses_or_number instead of addition")
    # return parse_parentheses_or_number(x)

parse_addition_expression = alt(parse_addition, parse_parentheses_or_number)


# def parse_multiplication_expression(x):
# try:
# return parse_multiplication(x)
# except:
# return parse_addition_expression(x)

parse_multiplication_expression = alt(
    parse_multiplication, parse_addition_expression)


def test(x, y):
    assert parse_multiplication_expression(x)[0] == y, "expected: {}, value: {}, remainder: {}".format(
        *map(repr, [y, *parse_multiplication_expression(x)])
    )


test("(5)", 5)
test("((5))", 5)
test("((5))5", 5)

test("4+1", 5)
test("3+1+1", 5)
test("3+1+1+2", 7)
test("(4)+1", 5)
test("4+(1)", 5)
test("(4)+(1)", 5)


test("4*1", 4)
test("1+(2*3)+(4*(5+6))", (51))
test("2*3+(4*5)", (46))
test("8*3*5*4", 480)
test("8*6+9", 480 // 4)
magicprint("🍌" * 30)
test("6+9*8", 480 // 4)
test("8*6+9*4", 480)
test("8*3+9+3*4", 480)

test("5+(8*3+9+3*4)", 485)
# assert parse_multiplication_expression("5+(8*3+9+3*4*3)")
# 0] == (1445)
# assert parse_multiplication_expression(
# "5*9*(7*3*3+9*3+(8+6*4))")[0] == (669060)
# assert parse_multiplication_expression(
# "((2+4*9)*(6+9*8+6)+6)+2+4*2")[0] == (23340)
