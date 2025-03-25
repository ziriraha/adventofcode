from hashlib import md5

INPUT = "ckczppom"

def mine_adventcoin(inp, zeroes):
    hash = ""
    x = 0
    matching = "0"*zeroes
    while hash[:zeroes] != matching:
        hash = md5((inp + str(x)).encode()).hexdigest()
        x += 1
    return x - 1

if __name__ == "__main__":
    print(mine_adventcoin(INPUT, 5))
    print(mine_adventcoin(INPUT, 6))