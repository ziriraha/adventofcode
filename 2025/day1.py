def part1():
    position = 50
    pointing_at_zero = 0
    with open("inputs/day1.txt", "r") as f:
        while len(instruction := f.readline()):
            rotation = int(instruction[1:])
            if instruction[0] == 'L': rotation *= -1
            position = (position + rotation) % 100
            pointing_at_zero += 1 * position == 0
    return pointing_at_zero

def part2():
    position = 50
    pointing_at_zero = 0
    with open("inputs/day1.txt", "r") as f:
        while len(instruction := f.readline()):
            rotation = int(instruction[1:])
            if instruction[0] == 'L': rotation *= -1
            moved = position + rotation
            pointing_at_zero += abs(moved) // 100 + (position != 0 and moved <= 0)
            position = moved % 100
    return pointing_at_zero

if __name__ == "__main__":
    print(part1())
    print(part2())
