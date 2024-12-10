def read_input():
    with open("inputs/day10.txt", "r") as f:
        return [[int(num) for num in line] for line in f.read().splitlines()]


# Find a trail head (0)
# travel its path depth first
# return the number of ends it has
#  (set of endings per head)

def get_neighbours(i, j, mapa):
    sim = mapa[i][j]
    neighbours = []
    on_map = lambda a, b: 0 <= a and a < len(mapa) and 0 <= b and b < len(mapa[i])
    if on_map(i-1, j) and mapa[i-1][j] - 1 == sim:
        neighbours.append((i-1, j, mapa[i-1][j]))
    if on_map(i+1, j) and mapa[i+1][j] - 1 == sim:
        neighbours.append((i+1, j, mapa[i+1][j]))
    if on_map(i, j-1) and mapa[i][j-1] - 1 == sim:
        neighbours.append((i, j-1, mapa[i][j-1]))
    if on_map(i, j+1) and mapa[i][j+1] - 1 == sim:
        neighbours.append((i, j+1, mapa[i][j+1]))
    return neighbours

def part1(mapa):
    scores = []
    for i in range(len(mapa)):
        for j in range(len(mapa[i])):
            if mapa[i][j] != 0: continue
            visited = []
            score = 0
            to_visit = get_neighbours(i, j, mapa)
            while len(to_visit) > 0:
                p = to_visit.pop()
                if p in visited: continue
                if p[2] == 9: 
                    score += 1
                else:
                    to_visit += get_neighbours(p[0], p[1], mapa)
                visited.append(p)
            scores.append(score)
    return sum(scores)

def part2(mapa):
    # Same as part1 but wihtout visited array
    scores = []
    for i in range(len(mapa)):
        for j in range(len(mapa[i])):
            if mapa[i][j] != 0: continue
            score = 0
            to_visit = get_neighbours(i, j, mapa)
            while len(to_visit) > 0:
                p = to_visit.pop()
                if p[2] == 9: 
                    score += 1
                else:
                    to_visit += get_neighbours(p[0], p[1], mapa)
            scores.append(score)
    return sum(scores)

if __name__ == "__main__":
    print(part1(read_input()))
    print(part2(read_input()))