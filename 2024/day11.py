from collections import defaultdict

def read_input():
    with open("inputs/day11.txt", "r") as f:
        return [int(num) for num in f.read().split(" ")]

results = defaultdict(int)
def blink(state, level):
    if type(state) == list: return sum([blink(i, level) for i in state])
    if level == 0: return 1
    if not (state, level) in results.keys():
        if state == 0: results[(state, level)] = blink(1, level-1)
        elif len(str(state)) % 2 == 0:
            string = str(state)
            left = int(string[:len(string)//2])
            right = int(string[len(string)//2:])

            results[(state, level)] = blink([left, right], level-1)
        else:
            results[(state, level)] = blink(state*2024, level-1)
    return results[(state, level)]

def part1(state):
    return blink(state, 25)

def part2(state):
    return blink(state, 75)

if __name__ == "__main__":
    print(part1(read_input()))
    print(part2(read_input()))