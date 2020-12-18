import inspect
import functools
import operator

with open('./input') as input_file:
    raw_input = [
        line.strip().replace(" ", "")
        for line in input_file.readlines()
    ]


def magicprint(*t):
    return
    print(">"*len(inspect.stack()), *t)


def parse_number(x):
    magicprint("number", x)
    return int(x[0]), x[1:]


assert parse_number("3") == (3, "")
assert parse_number("5") == (5, "")


def alt_(a, b):

    myname = "alt({})".format(", ".join(x.__name__ for x in [a, b]))

    def alternative_parser(x):
        magicprint(myname, x)
        try:
            return a(x)
        except ValueError:
            magicprint("alt: {} DISCARDED".format(b.__name__))
            return b(x)

    alternative_parser.__name__ = myname
    return alternative_parser


def alt(*ps):
    ps = [p() for p in ps]
    return functools.reduce(alt_, ps[1:], ps[0])


def seq(f, *ps):
    def p(x):
        remainder = x
        parsed = []

        for p in ps:
            values = p()(remainder)
            try:
                new_parsed, remainder = values
                parsed.append(new_parsed)
            except ValueError:
                raise RuntimeError("This should not happend", repr(values))

        return f(parsed, remainder)

    return p


def parse_string(s):
    myname = "string_parser({})".format(repr(s))

    def string_parser(x):
        magicprint(myname, x)
        if x.startswith(s):
            return s, x[len(s):]
        else:
            raise ValueError("")

    string_parser.__name__ = myname
    return string_parser


parse_parentheses = seq(lambda p, r: (p[1], r),
                        lambda: parse_string("("),
                        lambda: parse_multiplication_expression,
                        lambda: parse_string(")")
                        )


parse_parentheses_or_number = alt(
    lambda: parse_parentheses, lambda: parse_number)


parse_addition = seq(
    lambda p, r: (sum(p[i] for i in range(0, len(p), 2)), r),
    lambda: parse_parentheses_or_number,
    lambda: parse_string("+"),
    lambda: alt(
        lambda: parse_addition,
        lambda: parse_parentheses_or_number,
    ),
)

parse_multiplication = seq(
    lambda p, r: (functools.reduce(
        operator.mul, (p[i] for i in range(0, len(p), 2))), r),
    lambda: parse_addition_expression,
    lambda: parse_string("*"),
    lambda: alt(
        lambda: parse_multiplication,
        lambda: parse_addition_expression
    ),
)


# def parse_multiplication(x):
# magicprint('🍎parse_multiplication', x)
# lhs, remainder = parse_addition_expression(x)
# try:
# op = remainder[0]
# except IndexError:
# raise ValueError()
# if op != "+":
# raise ValueError()
# rhs, rem = parse_multiplication_expression(remainder[1:])

# return lhs + rhs, rem


parse_addition_expression = alt(
    lambda: parse_addition, lambda: parse_parentheses_or_number)
parse_multiplication_expression = alt(
    lambda: parse_multiplication, lambda: parse_addition_expression)


def test(x, y):
    result = parse_multiplication_expression(x)
    magicprint("🍌" * 30, result)
    assert result[0] == y, "expected: {}, value: {}, remainder: {}".format(
        *map(repr, [y, *result]))


print("🔥" * 30)
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
test("6+9*8", 480 // 4)
test("8*6+9*4", 480)
test("8*3+9+3*4", 480)

test("5+(8*3+9+3*4)", 485)
test("5+(8*3+9+3*4*3)", 1445)
test("5*9*(7*3*3+9*3+(8+6*4))", 669060)
test("((2+4*9)*(6+9*8+6)+6)+2+4*2", 23340)

print(sum(parse_multiplication_expression(x)[0] for x in raw_input))
