def read_input(filename):
    with open(filename, "r") as f:
        return f.read()
    
def calculate_floor(instructions):
    floor = 0
    for op in instructions:
        match op:
            case "(": floor += 1
            case ")": floor -= 1
    return floor

def calculate_position(instructions):
    floor = 0
    for position, op in enumerate(instructions):
        match op:
            case "(": floor += 1
            case ")": floor -= 1
        if floor < 0: return position + 1
    return -1

if __name__ == "__main__":
    instructions = read_input("inputs/day1.txt")
    print(calculate_floor(instructions))
    print(calculate_position(instructions))