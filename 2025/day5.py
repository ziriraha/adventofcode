def merge_all_ranges(ranges):
    ranges.sort()
    merged = [ranges[0]]
    for individual in ranges[1:]:
        if individual[0] <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(merged[-1][1], individual[1]))
        else:
            merged.append(individual)
    return merged

def read_input():
    fresh_ingredients = []
    ingredients = []
    with open("inputs/day5.txt", "r") as f:
        while fresh := f.readline().strip():
            fresh_ingredients.append(tuple(map(int, fresh.split('-'))))
        while ingredient := f.readline().strip():
            ingredients.append(int(ingredient))
    return merge_all_ranges(fresh_ingredients), ingredients.sort()

def part1(fresh_ingredients, ingredients):
    safe_ingredients = set()
    for start, stop in fresh_ingredients:
        in_range = False
        for ingredient in ingredients:
            if start <= ingredient and ingredient <= stop:
                safe_ingredients.add(ingredient)
                in_range = True
            elif in_range: break
    return len(safe_ingredients)

def part2(fresh_ingredients):
    return sum(stop - start + 1 for start, stop in fresh_ingredients)

if __name__ == "__main__":
    fresh_ingredients, ingredients = read_input()
    print(part1(fresh_ingredients, ingredients))
    print(part2(fresh_ingredients))
