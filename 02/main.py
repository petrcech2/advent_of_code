rules = {
    'red': 12,
    'green': 13,
    'blue': 14
}

def cubes_check(row):
    FLAG = True
    game_part = row.split(';')
    for part in game_part:
        take = part.split(',')
        for cube in take:
            num,color=cube[1:].split(' ')
            if color in rules.keys() and int(num) > rules[color]:
                FLAG = False
    return FLAG


def main():
    number = 0
    with open('input.txt') as f:
        input = f.read().split('\n')
        for row in input:
            game_number = row.split(':')[0].replace('Game ','')
            if cubes_check(row.split(':')[1]):
                number+= int(game_number)
    print(number)


if __name__ == "__main__":
    main()