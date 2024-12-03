def read_input():
    reports = []
    with open("day2.txt", "r") as f:
        a = f.read().splitlines()
        for rep in a:
            levels = [int(x) for x in rep.split(" ")]
            reports.append(levels)
    return reports

def is_report_safe(levels):
    fDir = False
    isDec = False
    for i in range(len(levels) - 1):
        dif = abs(levels[i] - levels[i+1])
        if not (1 <= dif and dif <= 3):
            return False
        if not fDir:
            if levels[i] == levels[i+1]:
                continue
            isDec = levels[i] > levels[i+1]
            fDir = True
        elif fDir:
            if isDec and levels[i] > levels[i+1]:
                continue
            if not isDec and levels[i] < levels[i+1]:
                continue
            return False
    return True

# Shorter but slower version
# def is_report_safe(levels):
#     diffs = [levels[i] - levels[i+1] for i in range(len(levels) - 1)]
#     return set(diffs) <= {1,2,3} or set(diffs) <= {-1,-2,-3}

def part1():
    count = 0
    for report in read_input():
        if is_report_safe(report):
            count += 1
    print(count)

def part2():
    count = 0
    for report in read_input():
        if is_report_safe(report):
            count += 1
        else:
            for i in range(len(report)):
                what_if = report[:i] + report[i+1:]
                if is_report_safe(what_if):
                    count += 1
                    break
    print(count)


if __name__ == "__main__":
    part1()
    part2()