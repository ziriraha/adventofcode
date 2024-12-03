import re

def read_input():
    with open("day3.txt", "r") as f:
        data = f.read()
        return data
    
def eval_instruction(instr):
    operands = instr.replace("mul(", "").replace(")", "").split(",")
    return int(operands[0]) * int(operands[1])

def part1(data):
    return sum(map(eval_instruction, re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)", data)))

def part2(data):
    results = 0
    instructions = re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)|don't\(\)|do\(\)", data)
    do = True
    for instr in instructions:
        match instr:
            case "don't()":
                do = False
            case "do()":
                do = True
            case _:
                results += eval_instruction(instr)*do
    return results


if __name__ == "__main__":
    print(part1(read_input()))
    print(part2(read_input()))