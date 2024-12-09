def read_input():
    with open("inputs/day9.txt", "r") as f:
        data = f.read()
    return data

def calculate_checksum(memory):
    return sum([i * int(memory[i]) for i in range(len(memory)) if memory[i] != '.'])

def part1(storage):
    idS = 0
    memory = []
    for i in range(len(storage)):
        memory += ["." if i%2 else str(idS) for _ in range(int(storage[i]))]
        idS += 1 if i%2 else 0

    head = 0
    tail = len(memory)-1
    while head != tail:
        if memory[head] != ".": head += 1; continue
        if memory[tail] == ".": tail -= 1; continue
        memory[head] = memory[tail]
        memory[tail] = "."
    return calculate_checksum(memory)

def part2(storage):
    # A file will be an object with: (id, size)
    # A free space will be (None, size)
    idS = 0
    memory = []
    for i in range(len(storage)):
        if i%2:
            memory.append([None, int(storage[i])])
        else:
            memory.append([idS, int(storage[i])])
            idS += 1

    # When i add a file to a free space we place the file before
    #  the free space (insert(index, object)) and substract the file
    #  size from the free space size.
    head = 0
    tail = len(memory) - 1
    while tail > 0:
        if memory[tail][0] == None: tail -= 1; continue
        if memory[head][0] != None: head += 1; continue
        if head > tail: tail -= 1; head = 0; continue
        if memory[head][1] < memory[tail][1]: head += 1; continue
        memory[head][1] -= memory[tail][1]
        memory.insert(head, memory[tail].copy())
        memory[tail+1][0] = None
        head = 0
    
    check_memory = []
    for i in memory:
        check_memory += ["." if i[0] == None else str(i[0]) for _ in range(i[1])]
    return calculate_checksum(check_memory)

if __name__ == "__main__":
    print(part1(read_input()))
    print(part2(read_input()))