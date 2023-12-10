import re


def navigator(maps, directions):
    flag = False
    counter = 0
    location = 'AAA'
    while flag == False:
        for direction in directions:
            print(f'Starting location is {location} and moving to the {direction}')
            if direction == 'L':
                location = maps[location][0]
            elif direction == 'R':
                location = maps[location][1]
            counter += 1
            if location == 'ZZZ':
                flag = True
            print(f'Moved to location: {location}')
    print(counter)

def main():
    with open('input.txt') as f:
        input = f.read().split('\n')
        maps = {}
        for i,row in enumerate(input):
            if i == 0:
                directions = [*row]
            if i > 1:
                maps[row[:3]] = re.findall(r'\w+', row.split('=')[1])
        navigator(maps, directions)

if __name__ == "__main__":
    main()