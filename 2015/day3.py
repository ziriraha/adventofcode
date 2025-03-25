def read_input(filename):
    with open(filename, "r") as f:
        return f.read()
    
def travel(directions):
    x, y = 0, 0
    travelled = set(["0,0"])
    for dir in directions:
        match dir:
            case '^': y += 1
            case '>': x += 1
            case 'v': y -= 1
            case '<': x -= 1
        travelled.add(f"{x},{y}")
    return len(travelled)

def travel_with_robosanta(directions):
    x, y = 0, 0
    rx, ry = 0, 0
    sx, sy = 0, 0
    travelled = set(["0,0"])
    for index, dir in enumerate(directions):
        x, y = (rx, ry) if index % 2 else (sx, sy)

        match dir:
            case '^': y += 1
            case '>': x += 1
            case 'v': y -= 1
            case '<': x -= 1

        if index % 2: rx, ry = x, y
        else: sx, sy = x, y
        travelled.add(f"{x},{y}")
    return len(travelled)

if __name__ == "__main__":
    directions = read_input("inputs/day3.txt")
    print(travel(directions))
    print(travel_with_robosanta(directions))