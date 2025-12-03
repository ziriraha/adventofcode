def find_best(cells, depth):
    if depth == 1: return max(cells)
    biggest_cell = max(cells[:-depth+1])
    next_biggest_cell = find_best(cells[cells.index(biggest_cell)+1:], depth-1)
    return biggest_cell * 10 ** (depth-1) + next_biggest_cell

def part1():
    jolts = 0
    with open("inputs/day3.txt", "r") as f:
        while battery := f.readline().replace('\n', ''):
            cells = list(map(int, battery))
            jolts += find_best(cells, 2)
    return jolts

def part2():
    jolts = 0
    with open("inputs/day3.txt", "r") as f:
        while battery := f.readline().replace('\n', ''):
            cells = list(map(int, battery))
            jolts += find_best(cells, 12)
    return jolts

if __name__ == "__main__":
    print(part1())
    print(part2())
