import re

def read_input():
    robots = []
    with open("inputs/day14.txt", "r") as f:
        data = f.read().splitlines()
        for entry in data:
            pv = entry.split(" ")
            pos = pv[0].replace("p=", "").split(",")
            vel = pv[1].replace("v=", "").split(",")
            robots.append(([int(pos[0]), int(pos[1])], # position
                           [int(vel[0]), int(vel[1])])) # velocity
    return robots

MAP_X = 101 # 101 #wide 
MAP_Y = 103 # 103 #tall

TIME = 100

def part1(robots, mapx, mapy, time):
    while time > 0:
        for robot in robots:
            pos = robot[0]
            vel = robot[1]
            pos[0] = (pos[0] + vel[0]) % mapx
            pos[1] = (pos[1] + vel[1]) % mapy
        time -= 1

    quads = [0, 0, 0, 0]

    for robot in robots:
        pos = robot[0]
        if pos[0] < mapx//2:
        # quadrant 1
            if pos[1] < mapy//2:
                quads[0] += 1
        # quadrant 2
            elif pos[1] > mapy//2:
                quads[1] += 1
        elif pos[0] > mapx//2:
        # quadrant 3
            if pos[1] < mapy//2:
                quads[2] += 1
        # quadrant 4
            elif pos[1] > mapy//2:
                quads[3] += 1
    return quads[0] * quads[1] * quads[2] * quads[3]

def part2(robots, mapx, mapy):
    unstopped = True
    base = [[" " for _ in range(mapy)] for _ in range(mapx)]
    time = 0
    while unstopped:
        for robot in robots:
            pos = robot[0]
            vel = robot[1]
            pos[0] = (pos[0] + vel[0]) % mapx
            pos[1] = (pos[1] + vel[1]) % mapy

        # find group of 3x3 robots together

        display = [row.copy() for row in base]
        for robot in robots:
            pos = robot[0]
            display[pos[0]][pos[1]] = "#"
        # find group of 3x3 robots together
        string = "".join(["".join(row) for row in display])
        sol = re.findall(r'#######', string)
        if len(sol) > 0:
            for row in display:
                print("".join(row))
            if input("continue?") == "s":
                unstopped = False
        time += 1
    return time


if __name__ == "__main__":
    print(part1(read_input(), MAP_X, MAP_Y, TIME))
    print(part2(read_input(), MAP_X, MAP_Y))