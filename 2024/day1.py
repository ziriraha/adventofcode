def read_and_sort():
    with open("day1.txt", "r") as f:
        left = []
        right = []
        data = f.read().splitlines()
        for row in data:
            numbers = row.replace("   ", ",").split(",")
            left.append(int(numbers[0]))
            right.append(int(numbers[1]))
        sorted_left = sorted(left)
        sorted_right = sorted(right)
        return sorted_left, sorted_right

def part1():
    left, right = read_and_sort()
    distance = 0
    for i in range(len(left)):
        distance += abs(left[i] - right[i])
    print(distance)


def find_similar(left, right_list):
    found = False
    quant = 0
    for i in right_list:
        if left == i:
            quant += 1
            found = True
        elif found:
            break
    return quant

def part2():
    left, right = read_and_sort()
    similarity = 0
    for i in left:
        similarity += i * find_similar(i, right)
    print(similarity)

if __name__ == "__main__":
    part1()
    part2()