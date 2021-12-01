with open('./input') as input_file:
    raw_input = [
        line.strip().replace(" ", "")
        for line in input_file.readlines()
    ]


def evaluate(expression):
    print("🍏", "".join(expression))
    expression = list(expression)
    operator = None
    inside_parentheses = []
    parenthesis_depth = 0
    first_item = expression.pop(0)
    if first_item == "(":
        parenthesis_depth = 1
    else:
        value = int(first_item)

    while expression:
        if parenthesis_depth:
            inside_parentheses.append(expression.pop(0))
            next_ = expression.pop(0)
            if next_ == "(":
                parenthesis_depth += 1
            if next_ == ")":
                parenthesis_depth -= 1
            inside_parentheses.append(next_)

            if parenthesis_depth == 0:
                if operator == '+':
                    print("value = ", value, "+",
                          evaluate(inside_parentheses[0:-1]))
                    value += evaluate(inside_parentheses[0:-1])
                if operator == '*':
                    print("value = ", value, "*",
                          evaluate(inside_parentheses[0:-1]))
                    value *= evaluate(inside_parentheses[0:-1])
                if operator == None:
                    value = evaluate(inside_parentheses[0:-1])
                inside_parentheses = []
        else:
            operator = expression.pop(0)
            right_hand_side = expression.pop(0)
            if right_hand_side == "(":
                parenthesis_depth += 1
            else:
                if operator == '+':
                    value += int(right_hand_side)
                if operator == '*':
                    value *= int(right_hand_side)

    print("🍎", value)
    return value


assert evaluate("5") == 5
assert evaluate("(5)") == 5
assert evaluate("(5)+1") == 6
assert evaluate("2") == 2
assert evaluate("2+2") == 4
assert evaluate("2*3") == 6
assert evaluate("2*(3+1)") == 8
assert evaluate("2*(3+(1*2))") == 10

assert evaluate("2*3+(4*5)") == 26
assert evaluate("5+(8*3+9+3*4*3)") == 437
assert evaluate("(2+4*9)") == 54
assert evaluate("(6+9*8+6)") == 126
assert evaluate("(2+4*9)*(6+9*8+6)") == 6804, evaluate("(2+4*9)*(6+9*8+6)")
assert evaluate("((2+4*9)*(6+9*8+6)+6)+2+4*2") == 13632

print(sum(evaluate(x) for x in raw_input))
