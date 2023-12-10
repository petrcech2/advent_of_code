import re

def number_location(number,row,row_counter):
    #print(f"Number {number} - starts at {starts_at} and finishes at {finishes_at}")
    return {
        'number': number,
        'row': row_counter,
        'starts_at': starts_at,
        'finishes_at': finishes_at
    }


def main():
    numbers_locations, symbols_location = [], []
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
                if not(c.isalnum()) and c != '.':
                    symbols_location.append({
                        'row': row_counter,
                        'located': char_position
                    })
                    #print(f"row: {row_counter} and position: {char_position}")
                char_position+=1
            row_counter+=1
        for number in numbers_locations:
            flag = False
            for symbol in symbols_location:
                if abs(symbol['row'] - number['row']) <= 1 and number['starts_at']-1 <= symbol['located'] <= number['finishes_at']+1:
                    print(symbol)
                    flag = True
            print(f"{number} - {flag}")
            if flag:
                counter += int(number['number'])

    print(counter)



if __name__ == "__main__":
    main()