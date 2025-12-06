def read_input():
    rolls = {}
    with open("inputs/day4.txt", "r") as f:
        i = 0
        while row := f.readline().strip():
            for j in range(len(row)):
                rolls[i, j] = row[j]
            i += 1
    return rolls, i, j + 1

def is_accessible(rolls, rows, cols, i, j):
    surroundings = 0
    for di in (-1, 0, 1):
        for dj in (-1, 0, 1):
            if di == 0 and dj == 0: continue
            ni, nj = i + di, j + dj
            surroundings += 0 <= nj < cols and 0 <= ni < rows and rolls[ni, nj] == '@'
    return surroundings < 4

def part1(rolls, rows, cols):
    return sum(rolls[i, j] == '@' and is_accessible(rolls, rows, cols, i, j) for i, j in rolls)

def part2(rolls, rows, cols):
    removed = 0
    to_remove = {'4': '2'}
    while len(to_remove):
        to_remove = {
            (i, j): 'x'
            for i, j in rolls
            if rolls[i, j] == '@' and is_accessible(rolls, rows, cols, i, j)
        }
        rolls.update(to_remove)
        removed += len(to_remove)
    return removed

if __name__ == "__main__":
    rolls, i, j = read_input()
    print(part1(rolls, i, j))
    print(part2(rolls, i, j))
