from collections import defaultdict
from math import prod

def calculate(inputs, operations):
    return sum(operations[key](values) for key, values in inputs.items())

def part1():
    inputs = defaultdict(list)
    operations = {}
    with open("inputs/day6.txt", "r") as f:
        while line := f.readline().strip():
            i = 0
            for number in line.split(' '):
                if number in ['+', '*']:
                    operations[i] = sum if number == '+' else prod
                elif number:
                    inputs[i].append(int(number))
                i += bool(number)
    return calculate(inputs, operations)

def part2():
    inputs = defaultdict(list)
    operations = {}
    with open("inputs/day6.txt", "r") as f:
        i = 0
        for line in [list(line) for line in zip(*f.readlines())]:
            if number := ''.join(line).strip():
                if number[-1] in ['+', '*']:
                    operations[i] = sum if number[-1] == '+' else prod
                    number = number[:-1].strip()
                inputs[i].append(int(number))
            else: i += 1
    return calculate(inputs, operations)

if __name__ == "__main__":
    print(part1())
    print(part2())
