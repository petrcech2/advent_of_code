import re

def main():
    numbers_locations, symbols_locations = [], []
    row_counter = 1
    counter = 0
    with open('input.txt') as f:
        input = f.read().split('\n')
        for row in input:
            starting_location = 0
            numbers = re.findall(r'\d+', row)
            for number in numbers:
                starts_at = row.find(number,starting_location)
                finishes_at = starts_at + len(number) - 1
                starting_location = finishes_at
                numbers_locations.append({
                    'number': number,
                    'row': row_counter,
                    'starts_at': starts_at,
                    'finishes_at': finishes_at
                })
            char_position = 0
            for c in row:
                if  c == '*':
                    symbols_locations.append({
                        'row': row_counter,
                        'located': char_position
                    })
                    #print(f"row: {row_counter} and position: {char_position}")
                char_position+=1
            row_counter+=1
        for symbol in symbols_locations:
            print(symbol)
            multiplier = []
            for number in numbers_locations:
                if abs(symbol['row'] - number['row']) <= 1 and number['starts_at']-1 <= symbol['located'] <= number['finishes_at']+1:
                    multiplier.append(number['number'])
            print(multiplier)
            if len(multiplier) > 1:
                counter+= int(multiplier[0])*int(multiplier[1])
    print(counter)


if __name__ == "__main__":
    main()