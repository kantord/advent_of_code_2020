with open('./input') as input_file:
    raw_rules = input_file.readlines()


def parse_limit(raw_limit):
    rule = raw_limit.split(' bags')[0].split(' bag')[0]

    return {
        "count": int(rule.split(' ')[0]),
        "limit_for": " ".join(rule.split(' ')[1:]),
    }


def parse_rule(rule):
    rule_for, raw_rule = rule.split(' bags contain ')
    raw_limits = raw_rule.split('.')[0].split(", ")

    return {
        "rule_for": rule_for,
        "limits": [parse_limit(limit) for limit in raw_limits]
        if raw_limits[0] != "no other bags" else []
    }


# def get_valid_parents(bag_type, rules):
    # checked = set()
    # to_check = set(rule["rule_for"] for rule in rules)
    # parents = {rule["rule_for"]: [] for rule in rules}
    # results = set()
    # while to_check:
    # print(parents)
    # checking = to_check.pop()
    # checked.add(checking)
    # checking_rule = [
    # rule for rule in rules if rule["rule_for"] == checking][0]

    # for child_rule in checking_rule["limits"]:
    # limit_for = child_rule["limit_for"]

    # to_check.add(limit_for)
    # parents[limit_for] = [] + parents[checking] + [checking]
    # if limit_for == bag_type:
    # results.add(parents[limit_for][0])

    # return results

def can_contain(bag_type, rule, rules):
    for limit in rule["limits"]:
        if limit["limit_for"] == bag_type:
            return True
        if can_contain(bag_type, [rule for rule in rules if rule["rule_for"] == limit["limit_for"]][0], rules):
            return True
    return False


def get_valid_parents(bag_type, rules):
    solutions = set()

    for rule in rules:
        if can_contain(bag_type, rule, rules):
            solutions.add(rule["rule_for"])

    return solutions


rules = [parse_rule(rule) for rule in raw_rules]
solution = get_valid_parents("shiny gold", rules)

print(solution)
print(len(solution))
