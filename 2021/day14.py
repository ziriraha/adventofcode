from collections import defaultdict

STEPS = 40

def read_input(file):
    with open(file, "r") as f:
        inp = f.read().splitlines()
    template = inp.pop(0)
    inp.pop(0)
    rules = {}
    for rule in inp:
        r = rule.split(" -> ")
        rules[r[0]] = r[1]
    return template, rules

def step(state, rules):
    nstate = defaultdict(int)
    for pair in state:
        if pair in rules.keys():
            nstate[pair[0] + rules[pair]] += state[pair]
            nstate[rules[pair] + pair[1]] += state[pair]
        else:
            nstate[pair] = state[pair]
    return nstate

def calculate(template, f, l):
    freq = defaultdict(int)
    for pair in template.keys():
        freq[pair[0]] += template[pair]
        freq[pair[1]] += template[pair]

    freq[f] += 1; freq[l] += 1
    frequencies = [n // 2 for n in freq.values()]
    return max(frequencies) - min(frequencies)

def convert(template):
    state = defaultdict(int)
    for i in range(len(template)-1):
        state[template[i:i+2]] += 1
    return state

if __name__ == "__main__":
    template, rules = read_input("inputs/day14.txt")
    first, last = template[0], template[-1]

    state = convert(template)
    for _ in range(STEPS):
        state = step(state, rules)
    
    print(calculate(state, first, last))
