from collections import defaultdict
from functools import cmp_to_key

def read_input():
    with open("day5.txt") as f:
        data = f.read()
        order, manuals = data.split("\n\n")
        return order.splitlines(), manuals.splitlines()

def parse_ordering(rules):
    dRules = defaultdict(list)
    for rule in rules:
        b, a = rule.split("|")
        dRules[b].append(a)
    return dict(dRules)

def check_order(rules, pages): return all(not page in rules.setdefault(pages[i], []) for i in range(len(pages)) for page in pages[:i])

def part1(rules, manuals): return sum([int(manual[len(manual)//2]) for manual in manuals if check_order(rules, manual)])

def compare_pages(page1, page2, rules):
    if page1 in rules.setdefault(page2, []):
        return 1
    if page2 in rules.setdefault(page1, []):
        return -1
    else:
        return 0


def part2(rules, manuals):
    unordered = [manual for manual in manuals if not check_order(rules, manual)]
    ordered = [sorted(manual, key=cmp_to_key(lambda x, y: compare_pages(x, y, rules))) for manual in unordered]
    return sum([int(manual[len(manual)//2]) for manual in ordered])

if __name__ == "__main__":
    order, manuals = read_input()
    rules = parse_ordering(order)
    manuals = [m.split(",") for m in manuals]
    print(part1(rules, manuals))
    print(part2(rules, manuals))