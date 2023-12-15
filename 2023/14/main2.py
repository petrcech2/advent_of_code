#can be done if i have enough time, just make a new mapping after stone_moving and turn locations by 90°

import re

def stone_moving(input):
    cnt = 0
    for row in input:
        hashtags_locations = [match.start() for match in re.finditer(r'#', row)]
        hashtags_locations.append(len(row)+1)
        rocks_locations = [match.start() for match in re.finditer(r'O', row)]
        rock_occurence = 1
        for i, hash in enumerate(hashtags_locations):
            for j, rock in enumerate(rocks_locations):
                if rock < hash and hash == hashtags_locations[0]:
                    cnt += len(row)-j
                    rocks_locations[j] = len(row)+1
                elif rock < hash:
                    cnt += len(row)-hashtags_locations[i-1]-rock_occurence
                    rock_occurence +=1
                    rocks_locations[j] = len(row)+1
            rock_occurence = 1
    print(cnt)


def columns_to_rows(input_str):
    new_list = []
    for i in range(len(input_str[0])):
        str = ''
        for row in input_str:
            str += row[i]
        new_list.append(str)
    return stone_moving(new_list)

def main():
    with open('input.txt') as f:
        input = f.read().split('\n')
        columns_to_rows(input)
if __name__ == "__main__":
    main()