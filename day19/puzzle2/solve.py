import inspect
import functools
import re

with open('./input') as input_file:
    raw_input = input_file.read()


raw_rules, messages = raw_input.split('\n'*2)


def map_(f, p):
    def parser(x):
        return f(*p()(x))

    parser.__name__ = p.__name__

    return parser


def magicprint(*t):
    return
    print(">"*len(inspect.stack()), *t)


def parse_regexp(exp):
    def p(x):
        magicprint("Trying regepx {} to match {}".format(repr(exp), repr(x)))
        match = re.match(exp, x)
        if not match:
            raise ValueError(
                "{} does not match regular expression".format(repr(x)))
        start, end = match.span()
        return x[start:end], x[end:]

    return p


parse_number = map_(lambda p, r: (int(p), r),
                    lambda: parse_regexp("[0-9]+"))

assert parse_number("3") == (3, "")
assert parse_number("5") == (5, "")
assert parse_number("153") == (153, "")
assert parse_number("0") == (0, "")
assert parse_number("153x") == (153, "x")


# def alt_(a, b):

# myname = "alt({})".format(", ".join(x.__name__ for x in [a, b]))

# def alternative_parser(x):
# magicprint("🍄Trying {} or {} to match {}".format(
# a.__name__, b.__name__, repr(x)))
# try:
# return a(x)
# except ValueError:
# return b(x)

# alternative_parser.__name__ = myname
# return alternative_parser


# def alt(*ps):
# ps = [p() for p in ps]
# f = functools.reduce(alt_, ps[1:], ps[0])

# f.__name__ = " | ".join(p.__name__ for p in ps)

# return f


def alt(*ps):
    def pp(x):
        for p in ps:
            try:
                return p()(x)
            except ValueError:
                continue
        raise ValueError("None of the alternatives matched")

    return pp


def seq(f, *ps):
    def p(x):
        remainder = x
        parsed = []

        magicprint("Trying sequence {}".format(
            ps
        ))
        for p in ps:
            magicprint("Trying  {}".format(
                p
            ))
            # try:
            values = p()(remainder)
            # except ValueError:
            # raise ValueError("Sequence not matched with {}".format(x))
            # try:
            new_parsed, remainder = values
            parsed.append(new_parsed)
            # except ValueError:
            # raise RuntimeError("This should not happend", repr(values))

        if parsed:
            return f(parsed, remainder)
        else:
            raise ValueError("No match with this sequence 🐷:🚙")

    p.__name__ = " ".join(p().__name__ for p in ps)

    return p


def parse_string(s):
    myname = repr(s)

    def string_parser(x):
        magicprint("Trying string {} on {}".format(repr(s), repr(x)))
        if x.startswith(s):
            return s, x[len(s):]
        else:
            raise ValueError(
                "String {} is not matching {}".format(repr(x), repr(s)))

    string_parser.__name__ = myname
    return string_parser


rules = {}


def rule_parser(rule_id):
    def p(x):
        return rules[rule_id][0](x)

    print("😀", rule_id)
    p.__name__ == str(rule_id)

    return p


simple_rule_parser = map_(
    lambda p, r: (rule_parser(p), r),
    lambda: parse_number
)


rul_seq_parser = seq(
    lambda p, r: (seq(lambda p, r: (p, r), lambda: p[0], lambda: p[2]), r),
    lambda: simple_rule_parser,
    lambda: parse_string(" "),
    lambda: alt(
        lambda: rul_seq_parser,
        lambda: simple_rule_parser
    ),
)


def parse_seq(p, r):
    print("💸"*20, p, r)
    return alt(lambda: p[0], lambda: p[2]), r


rul_alt_parse = seq(
    parse_seq,
    lambda: rul_seq_parser,
    lambda: parse_string(" | "),
    lambda: alt(
        lambda: rul_alt_parse,
        lambda: rul_seq_parser,
    )
)

assert rul_seq_parser("45 35")
# assert rul_seq_parser("45 35 2")[1] == ""

assert rul_alt_parse("2 3 | 3 2")[1] == ""


# string_rule_parser = alt(
# lambda: map_(
# lambda p, r: (parse_string("b"), r),
# lambda: parse_string('"b"')
# ),
# lambda: map_(
# lambda p, r: (parse_string("a"), r),
# lambda: parse_string('"a"')
# ),
# )

string_rule_parser = map_(
    lambda p, r: (parse_regexp('^' + p[1]), r),
    lambda: parse_regexp('^"[ab]"'))

assert string_rule_parser('"a"')[1] == ""
assert string_rule_parser('"b"')[1] == ""
assert string_rule_parser('"a"')[0]("abx")[1] == "bx"
# assert string_rule_parser('"a"')[0]("ybx")[1] == "ybx"


raw_rule_parser = alt(
    lambda: rul_alt_parse,
    lambda: rul_seq_parser,
    lambda: simple_rule_parser,
    lambda: string_rule_parser,
)


for raw_rule in raw_rules.split('\n'):
    raw_rule = raw_rule.strip()
    id_, rule_desc = raw_rule.split(': ')
    print(rule_desc)
    rules[int(id_)] = raw_rule_parser(rule_desc)

# print(rules)

for i, rule in rules.items():
    print("ℹ️", i, " => ", rule[0].__name__)


# print(sum(1 for x in messages[0:-1] if rules[0][0](x.strip())[1] == ""))

# assert rules[0][0]("aa")[1] == ""

total_matching = 0
for x in messages.split('\n')[0:-1]:
    x = x.strip()
    try:
        _, r = rules[0][0](x)
        if not r:
            print(repr(x), "✅")
            total_matching += 1
        else:
            print(repr(x), "❌", repr(r))
    except ValueError as e:
        print(e)
        print(repr(x), "❌ (VE)")

print("Total matching", total_matching)

# my_rules = {}

# for rule in raw_rules.split('\n'):
    # ruleid, rule = rule.strip().split(': ')
    # my_rules[ruleid] = rule

# msgs = set(messages.split("\n")[0:-2])

# print(msgs)

# max_length = max(len(x) for x in msgs)


# def get_matching_strings(rule):
    # print("🍅", repr(rule))
    # if rule == '"a"':
        # yield "a"
    # elif rule == '"b"':
        # yield "b"
    # else:
        # if "|" in rule:
            # for variant in rule.split(' | '):
                # for x in get_matching_strings(variant):
                    # yield x
        # elif " " in rule:
            # xx = rule.split(' ')
            # for yy in get_matching_strings(" ".join(xx[1:])):
                # if len(yy) >= max_length:
                    # break
                # for xxx in get_matching_strings(xx[0]):
                    # if len(yy) + len(xxx) >= max_length:
                        # continue
                    # yield xxx + yy
        # else:
            # for u in get_matching_strings(my_rules[rule]):
                # yield u


# all_matching_strings = set(get_matching_strings(my_rules["0"]))

# print(all_matching_strings)


# matching_msg = msgs.intersection(all_matching_strings)

# print(matching_msg)


# print("Total matching", len(matching_msg))
