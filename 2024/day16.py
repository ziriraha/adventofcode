from operator import itemgetter

def read_input():
    with open("inputs/day16.txt", "r") as f:
        return [list(row) for row in f.read().splitlines()]

def get_start(mapa):
    for i in range(len(mapa)):
        for j in range(len(mapa[i])):
            if mapa[i][j] != "S": continue
            return i, j
    return None

def get_end(mapa):
    for i in range(len(mapa)):
        for j in range(len(mapa[i])):
            if mapa[i][j] != "E": continue
            return i, j
    return None

def distance(i1, j1, i2, j2):
    return abs(i1 - i2) + abs(j1 - j2)

def get_neighbours(i, j, mapa):
    sim = ".E"
    neighbours = []
    on_map = lambda a, b: 0 <= a and a < len(mapa) and 0 <= b and b < len(mapa[i])
    if on_map(i-1, j) and mapa[i-1][j] in sim:
        neighbours.append((i-1, j))
    if on_map(i+1, j) and mapa[i+1][j] in sim:
        neighbours.append((i+1, j))
    if on_map(i, j-1) and mapa[i][j-1] in sim:
        neighbours.append((i, j-1))
    if on_map(i, j+1) and mapa[i][j+1] in sim:
        neighbours.append((i, j+1))
    return neighbours

# A* algorithm
def part1(mapa):
    si, sj = get_start(mapa)
    ei, ej = get_end(mapa)
    to_visit = [(si, sj, distance(si, sj, ei, ej), 0)]
    while len(to_visit) > 0:
        print(to_visit)
        p = to_visit.pop(0)
        #if p[3] > 20: break
        if p[2] == 0: return p[3] + 1
        for nei in get_neighbours(p[0], p[1], mapa):
            to_visit.append((nei[0], nei[1], distance(nei[0], nei[1], ei, ej), p[3] + 1))
        to_visit.sort(key=itemgetter(2))

if __name__ == "__main__":
    print(part1(read_input()))