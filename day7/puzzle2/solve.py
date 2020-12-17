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

def get_count(bag_type, rule, rules):
    result = 0
    for limit in rule["limits"]:
        result += limit["count"]
        result += limit["count"] * get_count(limit["limit_for"], [
            rule for rule in rules if rule["rule_for"] == limit["limit_for"]][0], rules)
    return result


def count_bags(bag_type, rules):
    for rule in rules:
        if rule["rule_for"] == bag_type:
            print("!!")
            return get_count(bag_type, rule, rules)


rules = [parse_rule(rule) for rule in raw_rules]
solution = count_bags("shiny gold", rules)

print(solution)
