import re

def read_input():
    with open("inputs/day4.txt", "r") as f:
        return f.read().splitlines()
    
def rotate_45_degrees(matrix):
    n = len(matrix)
    m = len(matrix[0])
    result = [[] for _ in range(n + m - 1 )]

    for i in range(n):
        for j in range(m):
            result[i + j].append(matrix[i][j]) 
    return ["".join(row) for row in result]

def part1(grid):
    unit = "\n".join(grid)
    rotated = "\n".join([''.join(row) for row in zip(*grid[::-1])])
    diag = "\n".join(rotate_45_degrees(grid))
    inv_diag = "\n".join(rotate_45_degrees(rotated.splitlines()))
    return sum([
        # Horizontal
        len(re.findall(r"XMAS", unit)),
        len(re.findall(r"SAMX", unit)),
        # Vertical
        len(re.findall(r"XMAS", rotated)),
        len(re.findall(r"SAMX", rotated)),
        # Diagonal
        len(re.findall(r"XMAS", diag)),
        len(re.findall(r"SAMX", diag)),
        # Inverse Diagonal
        len(re.findall(r"XMAS", inv_diag)),
        len(re.findall(r"SAMX", inv_diag))
    ])

def part2(grid):
    #Find all occurances of two MAS word shaped in an X
    ctr = 0
    for i in range(1, len(grid)-1):
        for j in range(1, len(grid[i])-1):
            if grid[i][j] != 'A': continue
            # Diagona
            if (f:='MS'.find(grid[i-1][j-1])) == -1: continue
            if 'MS'[f-1] != grid[i+1][j+1]: continue
            # Inverse Diagonal
            if (f:='MS'.find(grid[i-1][j+1])) == -1: continue
            if 'MS'[f-1] != grid[i+1][j-1]: continue
            ctr += 1
    return ctr

if __name__ == "__main__":
    print(part1(read_input()))
    print(part2(read_input()))