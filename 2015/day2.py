def read_input(filename):
    with open(filename, "r") as f:
        return [list(map(int, dim.split("x"))) for dim in f.read().splitlines()]
    
def calculate_wrappingpaper(dimentions):
    total_area = 0
    for dim in dimentions:
        l, w, h = dim
        smallest_area = min(l*h, l*w, h*w)
        paper_area = 2*l*w + 2*w*h + 2*h*l
        total_area += paper_area + smallest_area
    return total_area

def calculate_ribbon(dimentions):
    total_length = 0
    for dim in dimentions:
        l, w, h = dim
        around = min(2*l + 2*w, 2*l + 2*h, 2*w + 2*h)
        bow = l*w*h
        total_length += around + bow
    return total_length

if __name__ == "__main__":
    dimentions = read_input("inputs/day2.txt")
    print(calculate_wrappingpaper(dimentions))
    print(calculate_ribbon(dimentions))