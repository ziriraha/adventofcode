def part1():
    invalid_ids = 0
    with open("inputs/day2.txt", "r") as f:
        x = ','
        while x:
            current_range = ""
            while (x := f.read(1)) and x != ',': current_range += x
            start, stop = map(int, current_range.split('-'))
            for i in range(start, stop + 1):
                s = str(i)
                if len(s) % 2: continue
                mid = len(s)//2
                invalid_ids += i * (s[0:mid] == s[mid:])
    return invalid_ids

def part2():
    invalid_ids = 0
    with open("inputs/day2.txt", "r") as f:
        x = ','
        while x:
            current_range = ""
            while (x := f.read(1)) and x != ',': current_range += x
            start, stop = map(int, current_range.split('-'))
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
    print(part1())
    print(part2())
