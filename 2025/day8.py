import math

def read_input():
    junction_boxes, pairs = [], []
    with open("inputs/day8.txt", "r") as f:
        while row := f.readline().strip():
            junction_boxes.append(tuple(map(int, row.split(","))))
    for index, box1 in enumerate(junction_boxes):
        for box2 in junction_boxes[index+1:]:
            pairs.append((box1, box2))
    return set(junction_boxes), sorted(pairs,
        key=lambda p: math.sqrt((p[0][0] - p[1][0])**2 + (p[0][1] - p[1][1])**2 + (p[0][2] - p[1][2])**2))

def connect(circuits, i, pair):
    cs = {k for k, circuit in circuits.items() if any(box in circuit[1] for box in pair)}
    match len(cs):
        case 0:
            circuits[i] = ([pair], set(pair))
            i += 1
        case 1:
            index = cs.pop()
            circuits[index][0].append(pair)
            circuits[index][1].update(set(pair))
        case 2:
            new = ([pair], set(pair))
            for other in {other for j in cs for other in circuits.pop(j)[0]}:
                new[0].append(other)
                new[1].update(set(other))
            circuits[i] = new
            i += 1
    return i

def main(boxes, pairs, target=1000):
    circuits, i = dict(), 0
    pair = ((0,0,0), (0,0,0))
    num_pair, part1 = 0, 0
    while not(not boxes and len(circuits) == 1):
        pair = pairs.pop(0)
        i = connect(circuits, i, pair)
        boxes -= set(pair)
        if (num_pair := num_pair + 1) == target:
            part1 = math.prod(sorted([len(circuit[1]) for circuit in circuits.values()])[-3:])
    return part1, pair[0][0] * pair[1][0]

if __name__ == '__main__':
    part1, part2 = main(*read_input())
    print(part1)
    print(part2)
