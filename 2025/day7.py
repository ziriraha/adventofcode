from collections import defaultdict

def read_input():
    useful_splitters = 0
    with open("inputs/day7.txt", "r") as f:
        particles = defaultdict(int)
        while row := f.readline().strip():
            if row == len(row)*'.': continue
            for pos, el in enumerate(row):
                if el == 'S': particles[pos] = 1
                elif el != '.' and particles[pos]:
                    useful_splitters += 1
                    quantity = particles.pop(pos)
                    particles[pos+1] += quantity
                    particles[pos-1] += quantity
    return useful_splitters, sum(particles.values())

if __name__ == "__main__":
    part1, part2 = read_input()
    print(part1)
    print(part2)
