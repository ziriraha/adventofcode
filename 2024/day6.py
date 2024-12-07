import re

def read_input():
    with open("inputs/day6.txt", "r") as f:
        return [list(line) for line in f.read().splitlines()]
    
def convert(pmap):
    return "\n".join(["".join(line) for line in pmap])

dirs = '<v>^'
leg = '.#X'

# Find initial position
def find_init(pmap):
    d = -1
    for i in range(len(pmap)):
        if not any([di in pmap[i] for di in dirs]): continue
        for j in range(len(pmap[i])):
            if (d := dirs.find(pmap[i][j])) != -1: return d, i, j
    return -1, -1, -1

def prepare_map(pmap):
    for i in range(len(pmap)):
        pmap[i].insert(0, " ")
        pmap[i].append(" ")
    line = list(" "*(len(pmap[0])+2))
    pmap.insert(0, line)
    pmap.append(line)
    return pmap

def get_final_map(pmap):
    pmap = prepare_map(pmap)
    d, x, y = find_init(pmap)
    mx, my = len(pmap), len(pmap[0])
    idi, ix, iy = d, x, y

    path = []
    
    while 0 <= x and x < mx and 0 <= y and y < my:
        try:
            match dirs[d]:
                case '<':
                    if pmap[x][y-1] != leg[1]:
                        pmap[x][y] = leg[2]
                        x, y = x, y-1
                    else:
                        d = dirs.find(dirs[d-1])
                case 'v':
                    if pmap[x+1][y] != leg[1]:
                        pmap[x][y] = leg[2]
                        x, y = x+1, y
                    else:
                        d = dirs.find(dirs[d-1])
                case '>':
                    if pmap[x][y+1] != leg[1]:
                        pmap[x][y] = leg[2]
                        x, y = x, y+1
                    else:
                        d = dirs.find(dirs[d-1])
                case '^':
                    if pmap[x-1][y] != leg[1]:
                        pmap[x][y] = leg[2]
                        x, y = x-1, y
                    else:
                        d = dirs.find(dirs[d-1])
        except:
            break
        if (d, x, y) in path:
            return "Looped"
        path.append((d, x, y))
    return convert(pmap[1:-1])

def get_visited_positions(final):
    #calculate positions of all Xs
    positions = []
    final = final.splitlines()
    for i in range(len(final)):
        if not leg[2] in final[i]: continue
        for j in range(len(final[i])):
            if final[i][j] == leg[2]:
                positions.append((i,j-1))
    return positions

def part1(pmap):
    return len(get_visited_positions(get_final_map(pmap)))

def copy(pmap):
    return [i.copy() for i in pmap]

def part2(pmap):
    pposis = get_visited_positions(get_final_map(copy(pmap)))
    _, x, y = find_init(pmap)
    possiblities = 0
    for i in range(len(pposis)):
        pos = pposis[i]
        print("\r", ">  "+str(i) + "/" + str(len(pposis)), end="                 ")
        if pos[0] == x and pos[1] == y: continue
        cmap = copy(pmap)
        cmap[pos[0]][pos[1]] = leg[1]
        if get_final_map(cmap) == "Looped":
            possiblities += 1
    return possiblities


if __name__ == "__main__":
    print(part1(read_input()))
    print(part2(read_input()))