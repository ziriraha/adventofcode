def read_input():
    with open("inputs/day7.txt", "r") as f:
        return [list(map(int, line.replace(":", "").split(" "))) for line in f.read().splitlines()]

def part1(eq):
    if len(eq) == 1: return eq
    results = part1(eq[1:])
    return ([eq[0]*result for result in results] # Multiplication
            + [eq[0]+result for result in results]) # Adition

def part2(eq):
    if len(eq) == 1: return eq
    results = part2(eq[1:])
    return ([eq[0]*result for result in results] # Multiplication
            + [eq[0]+result for result in results] # Adition
            + [int(str(result)+str(eq[0])) for result in results]) # Concatenation

def evaluate(part, equations):
    return sum([eq[0] for eq in equations if eq[0] in part(eq[1:][::-1])])

if __name__ == "__main__":
    print(evaluate(part1, read_input()))
    print(evaluate(part2, read_input()))