import re
from math import lcm
from itertools import cycle

def navigator(maps, directions):
    starting_locations = [location for location in maps.keys() if location.endswith("A")]
    first_z = []
    for location in starting_locations:
        counter=0
        for direction in cycle(directions):
            location = maps[location][direction]
            counter += 1
            if location.endswith('Z'):
                first_z.append(counter)
                break
    print(lcm(*first_z))

def main():
    with open('input.txt') as f:
        input = f.read().split('\n')
        maps = {}
        directions = [0 if instruction == "L" else 1 for instruction in input[0]]
        for row in input[2:]:
            maps[row[:3]] = re.findall(r'\w+', row.split('=')[1])
        navigator(maps, directions)

if __name__ == "__main__":
    main()