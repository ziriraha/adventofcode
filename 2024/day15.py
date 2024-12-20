def read_input():
    with open("inputs/day15.txt", "r") as f:
        data = f.read().split("\n\n")
        mapa = [list(row) for row in data[0].splitlines()]
        movements = list(data[1])
    return (mapa, movements)

def part1(inputs):
    mapa, movements = inputs
    print(mapa)
    print()
    print(movements)



if __name__ == "__main__":
    print(part1(read_input()))