from collections import defaultdict
from functools import cmp_to_key

def read_input():
    with open("inputs/day5.txt") as f:
        data = f.read()
        order, manuals = data.split("\n\n")
        return parse_ordering(order.splitlines()), [m.split(",") for m in manuals.splitlines()]

def parse_ordering(rules):
    dRules = defaultdict(list)
    for rule in rules:
        b, a = rule.split("|")
        dRules[b].append(a)
    return dict(dRules)

def check_order(rules, pages): 
    return all(not page in rules.setdefault(pages[i], []) 
               for i in range(len(pages)) 
               for page in pages[:i])

def part1(rules, manuals): 
    return sum([int(manual[len(manual)//2]) 
                for manual in manuals if check_order(rules, manual)])

def compare_pages(page1, page2, rules): 
    return (1 if page1 in rules.setdefault(page2, []) 
            else -1 if page2 in rules.setdefault(page1, []) 
            else 0)

def part2(rules, manuals): 
    return sum([int(sorted(manual, 
                    key=cmp_to_key(lambda x, y: compare_pages(x, y, rules)))
            [len(manual)//2]) 
        for manual in 
            [manual for manual in 
                manuals if not check_order(rules, manual)]])

if __name__ == "__main__":
    rules, manuals = read_input()
    print(part1(rules, manuals))
    print(part2(rules, manuals))