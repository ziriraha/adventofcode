def read_input():
    fresh_ingredients = []
    ingredients = []
    with open("inputs/day5.txt", "r") as f:
        while fresh := f.readline().replace('\n', ''):
            fresh_ingredients.append(tuple(map(int, fresh.split('-'))))
        while ingredient := f.readline().replace('\n', ''):
            ingredients.append(int(ingredient))
    return fresh_ingredients, ingredients

def merge_all_ranges(ranges):
    ranges.sort()
    merged = [ranges[0]]
    for individual in ranges[1:]:
        if individual[0] <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(merged[-1][1], individual[1]))
        else:
            merged.append(individual)
    return merged

def part1(fresh_ingredients, ingredients):
    safe_ingredients = set()
    ingredients.sort()
    for ingredient_range in merge_all_ranges(fresh_ingredients):
        in_range = False
        for ingredient in ingredients:
            if ingredient_range[0] <= ingredient and ingredient <= ingredient_range[1]:
                safe_ingredients.add(ingredient)
                in_range = True
            elif in_range: break
    return len(safe_ingredients)

def part2(fresh_ingredients):
    return sum(individual[1] - individual[0] + 1 for individual in merge_all_ranges(fresh_ingredients))

if __name__ == "__main__":
    fresh_ingredients, ingredients = read_input()
    print(part1(fresh_ingredients, ingredients))
    print(part2(fresh_ingredients))
