def map_modification(input):
    new_map = []
    for row in input:
        new_map.append(row)
        if row.count('.') == len(row):
            new_map.append(row)

    to_add_columns = []
    for i in range(len(input[0])):
        if all(row[i] == '.' for row in new_map):
            to_add_columns.append(i)
    to_add_columns.sort(reverse=True)

    for i in to_add_columns:
        new_map = [row[:i] + '.' + row[i:] for row in new_map]
    return new_map

def space_counter(map):
    hashtag_positions = []
    for row_index, row in enumerate(map):
        for col_index, char in enumerate(row):
            if char == '#':
                hashtag_positions.append([row_index, col_index])

    distance = 0
    for i,main_hashtag in enumerate(hashtag_positions):
        for hashtag_to_compare in hashtag_positions[i+1:]:
            distance += hashtag_to_compare[0]-main_hashtag[0]
            distance += abs(hashtag_to_compare[1]-main_hashtag[1])
    print(distance)


def main():
    with open('input.txt') as f:
        input = f.read().split('\n')
        map = map_modification(input)
        space_counter(map)

if __name__ == "__main__":
    main()