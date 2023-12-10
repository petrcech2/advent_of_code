def prepare_cards(amount):
    buffer = []
    for i in range(1,amount+1):
        buffer.append([i, 1])
    return buffer

def main():
    with open('input.txt') as f:
        input = f.read().split('\n')
        cards_buffer = prepare_cards(len(input))
        row_number = 1
        for row in input:
            win_ratio = 0
            winning_nums = row.replace('  ',' ').split(':')[1].strip().split(' | ')[0].split(' ')
            bet_nums = row.replace('  ',' ').split(':')[1].split(' | ')[1].strip().split(' ')
            for w_num in winning_nums:
                for b_num in bet_nums:
                    if w_num == b_num:
                        win_ratio += 1
            for point in range(0,win_ratio):
                cards_buffer[point+row_number][1] += cards_buffer[row_number-1][1]
            row_number+=1

        sum = 0
        for list in cards_buffer:
            sum += list[1]
        print(sum)

if __name__ == "__main__":
    main()