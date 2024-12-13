from collections import defaultdict

def read_input():
    with open("inputs/day12.txt", "r") as f:
        return [list(line) for line in f.read().splitlines()]
    
def get_neighbours(i, j, mapa):
    sim = mapa[i][j]
    neighbours = []
    on_map = lambda a, b: 0 <= a and a < len(mapa) and 0 <= b and b < len(mapa[i])
    if on_map(i-1, j) and mapa[i-1][j] == sim:
        neighbours.append((i-1, j))
    if on_map(i+1, j) and mapa[i+1][j] == sim:
        neighbours.append((i+1, j))
    if on_map(i, j-1) and mapa[i][j-1] == sim:
        neighbours.append((i, j-1))
    if on_map(i, j+1) and mapa[i][j+1] == sim:
        neighbours.append((i, j+1))
    return neighbours

def part1(mapa):
    regions = defaultdict(list)
    region_id = -1
    visited = []
    for i in range(len(mapa)):
        for j in range(len(mapa[i])):
            if (i, j) in visited: continue
            region_id += 1
            to_visit = [(i, j)]
            while len(to_visit) > 0:
                p = to_visit.pop()
                if p in visited: continue
                neighbours = get_neighbours(p[0], p[1], mapa)
                to_visit += neighbours
                perimeter = 4 - len(neighbours)
                regions[region_id].append(perimeter)
                visited.append(p)
    return sum([len(regions[reg]) * sum([point for point in regions[reg]]) for reg in regions.keys()])

# ! 1st Try: Calculating the number of corners the region has.
def calculate_sides(region):
    get_corners = lambda t: [((t[0]-1, t[1]-1), t), # Upper Left
                            ((t[0]-1, t[1]), (t[0], t[1]+1)), # Upper Right
                            ((t[0], t[1]-1), (t[0]+1, t[1])), # Lower Left
                            (t, (t[0]+1, t[1]+1))] # Lower Right
    is_adjecent = lambda t1, t2: ((t1[0] == t2[0] and t1[1] == t2[1] + 1) # Above
                                or (t1[0] == t2[0] and t1[1] == t2[1] - 1) # Below
                                or (t1[0] == t2[0] + 1 and t1[1] == t2[1]) # Left
                                or (t1[0] == t2[0] - 1 and t1[1] == t2[1])) # Right

    # Number of sides is equal to number of corners (if two tiles share a corner, do not count the corner)
    corners = defaultdict(list)
    for tile in region:
        for c in get_corners(tile):
            if c in corners.keys():
                pop_it = False
                for t in corners[c]:
                    if is_adjecent(t, tile):
                        pop_it = True
                if pop_it: corners.pop(c)
                else: corners[c].append(tile)
            else: corners[c].append(tile)
    return sum([len(corners[c]) for c in corners.keys()])

# ! 2nd Try (https://www.reddit.com/r/adventofcode/comments/1hcxmpp/2024_day_12_part_2_visualisation_of_my_first/)

def part2(mapa):
    regions = defaultdict(list)
    region_id = -1
    visited = []
    for i in range(len(mapa)):
        for j in range(len(mapa[i])):
            if (i, j) in visited: continue
            region_id += 1
            to_visit = [(i, j)]
            while len(to_visit) > 0:
                p = to_visit.pop()
                if p in visited: continue
                neighbours = get_neighbours(p[0], p[1], mapa)
                to_visit += neighbours
                regions[region_id].append((p[0], p[1]))
                visited.append(p)
    return sum([len(regions[reg]) * calculate_sides(regions[reg]) for reg in regions.keys()])

if __name__ == "__main__":
    print(part1(read_input()))
    print(part2(read_input()))