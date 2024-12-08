from collections import defaultdict
import re

def read_input():
    with open("inputs/day8.txt", "r") as f:
        return f.read().splitlines()

def get_antenas(signals):
    antenas = defaultdict(list)
    for i in range(len(signals)):
        for j in range(len(signals[i])):
            if signals[i][j] == ".": continue
            antenas[signals[i][j]].append((i, j))
    return dict(antenas)

def evaluate(signals, part):
    antenas = get_antenas(signals)
    antinodes = set([])

    for typeA in antenas.keys():
        others = antenas[typeA].copy()
        for i in antenas[typeA]:
            others.remove(i) # No need to repeat pairs (direction doesnt matter)
            for j in others:
                part(i, j, signals, antinodes)
    return len(antinodes)

def part1(i, j, signals, antinodes):
    # Calculate that pair's antinode coordinates and add them in the antinode map.
    # Calculate vector between pairs
    diff = (i[0] - j[0], i[1] - j[1])
    # Add diff vector to i and add -diff vector to j
    an1 = (i[0] + diff[0], i[1] + diff[1])
    an2 = (j[0] - diff[0], j[1] - diff[1])
    # Add the new points to the antinode map (try)
    if 0 <= an1[0] and an1[0] < len(signals) and 0 <= an1[1] and an1[1] < len(signals[an1[0]]):
        antinodes.add(an1)
    if 0 <= an2[0] and an2[0] < len(signals) and 0 <= an2[1] and an2[1] < len(signals[an2[0]]):
        antinodes.add(an2)

def part2(i, j, signals, antinodes):
    # Calculate that pair's antinode coordinates and add them in the antinode map.
    # Calculate vector between pairs
    diff = (i[0] - j[0], i[1] - j[1])
    # Add diff vector to i and add -diff vector to j
    l = 0
    an = (i[0], i[1])
    while 0 <= an[0] and an[0] < len(signals) and 0 <= an[1] and an[1] < len(signals[an[0]]):
        antinodes.add(an)
        an = (i[0] + l * diff[0], i[1] + l * diff[1])
        l+=1
    l = 0
    an = (j[0], j[1])
    while 0 <= an[0] and an[0] < len(signals) and 0 <= an[1] and an[1] < len(signals[an[0]]):
        antinodes.add(an)
        an = (j[0] - l * diff[0], j[1] - l * diff[1])
        l+=1

if __name__ == "__main__":
    print(evaluate(read_input(), part1))
    print(evaluate(read_input(), part2))