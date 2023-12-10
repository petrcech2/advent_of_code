def prepare_cards(amount):
    print(amount)

def main():
    with open('input.txt') as f:
        input = f.read().split('\n')
        print(len(input))
        price_counter = 0
        for row in input:
            win_ratio = 0
            print(row)
            winning_nums = row.replace('  ',' ').split(':')[1].strip().split(' | ')[0].split(' ')
            bet_nums = row.replace('  ',' ').split(':')[1].split(' | ')[1].strip().split(' ')
            print(winning_nums)
            print(bet_nums)
            for w_num in winning_nums:
                for b_num in bet_nums:
                    if w_num == b_num and win_ratio == 0:
                        win_ratio+=1
                    elif w_num == b_num and win_ratio != 0:
                        win_ratio*=2
            price_counter+=win_ratio
        print(f"win_ratio je celkem {price_counter}")


if __name__ == "__main__":
    main()