def merge_all_ranges(ranges):
    ranges.sort()
    merged = [ranges[0]]
    for individual in ranges[1:]:
        if individual[0] <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(merged[-1][1], individual[1]))
        else:
            merged.append(individual)
    return merged

def read_input():
    ranges = []
    with open("inputs/day2.txt", "r") as f:
        for individual in f.read().strip().split(','):
            ranges.append(tuple(map(int, individual.split('-'))))
    return merge_all_ranges(ranges)

def part1(ranges):
    invalid_ids = 0
    for start, stop in ranges:
        for i in range(start, stop + 1):
            s = str(i)
            if len(s) % 2: continue
            mid = len(s)//2
            invalid_ids += i * (s[0:mid] == s[mid:])
    return invalid_ids

def part2(ranges):
    invalid_ids = 0
    for start, stop in ranges:
        for i in range(start, stop + 1):
            s, invalid = str(i), False
            for j in range(1, len(s)):
                if len(s) % j: continue
                prev, it = s[:j], True
                for k in range(1, len(s)//j):
                    if prev != s[k*j:k*j+j]: it = False; break
                if it: invalid = True; break
            if invalid: invalid_ids += i
    return invalid_ids

if __name__ == "__main__":
    ranges = read_input()
    print(part1(ranges))
    print(part2(ranges))
