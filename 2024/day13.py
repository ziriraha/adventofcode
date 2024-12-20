from pulp import LpProblem, LpVariable, LpMinimize, PULP_CBC_CMD

def read_input():
    # A tuple with 3 elements:
    #  Tuple with values for Button A
    #  Tuple with values for Button B
    #  Tuple with Prize positions

    data = []
    prizes = []
    with open("inputs/day13.txt", "r") as f:
        data = f.read().split("\n\n")
    for d in data:
        details = d.replace(", Y", "").split("\n")
        butA = details[0].split("+")
        A = (int(butA[-2]), int(butA[-1]))
        butB = details[1].split("+")
        B = (int(butB[-2]), int(butB[-1]))
        prize = details[2].split("=")
        P = (int(prize[-2]), int(prize[-1]))
        prizes.append((A, B, P))
    return prizes

def part1(prizes):
    tokens = 0

    for p in prizes:
        a = p[0]
        b = p[1]
        xy = p[2]

        problem = LpProblem("Integer_Linear_Programming", LpMinimize)

        A = LpVariable("A", lowBound=0, upBound=100, cat="Integer")
        B = LpVariable("B", lowBound=0, upBound=100, cat="Integer")

        problem += 3 * A + 1 * B, "Objective"

        problem += a[0] * A + b[0] * B == xy[0]
        problem += a[1] * A + b[1] * B == xy[1]

        # Solve the problem with CBC solver
        solver = PULP_CBC_CMD(msg=False)
        problem.solve(solver)

        if problem.status == 1:
            tokens += problem.objective.value()

    return int(tokens)

def part2(prizes):
    tokens = 0
    ADD = 10000000000000
    for p in prizes:
        a = p[0]
        b = p[1]
        xy = p[2]

        problem = LpProblem("Integer_Linear_Programming", LpMinimize)

        A = LpVariable("A", lowBound=100, cat="Integer")
        B = LpVariable("B", lowBound=100, cat="Integer")

        problem += 3 * A + 1 * B, "Objective"

        problem += a[0] * A + b[0] * B == (xy[0] + ADD)
        problem += a[1] * A + b[1] * B == (xy[1] + ADD)

        # Solve the problem with CBC solver
        solver = PULP_CBC_CMD(msg=False)
        problem.solve(solver)

        if problem.status == 1:
            tokens += problem.objective.value()

    return int(tokens)

if __name__ == "__main__":
    # Minimization problem with Simplex
    # Minimize p = 3*A + 1*B
    # Restrictions:
    #  AX + BX = XX
    #  AY + BY = YY
    print(part1(read_input()))
    print(part2(read_input()))

