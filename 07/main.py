def deck_of_cards(cards):
    occurences = []
    for card in cards:
        occurences.append(cards.count(card))

    if 5 in occurences:
        return 6
    elif 4 in occurences:
        return 5
    elif occurences.count(3) == 3 and occurences.count(2) == 2:
        return 4
    elif 3 in occurences:
        return 3
    elif occurences.count(2) == 4:
        return 2
    elif 2 in occurences:
        return 1
    elif 1 in occurences:
        return 0
    
def cards_straight(cards):
    card_meaning = {
        'A': 14,
        'K': 13,
        'Q': 12,
        'J': 11,
        'T': 10,
        '9': 9,
        '8': 8,
        '7': 7,
        '6': 6,
        '5': 5,
        '4': 4,
        '3': 3,
        '2': 2
    }
    straight = []
    for card in cards:
        if card in card_meaning.keys():
            straight.append(card_meaning[card])
    return straight


def main():
    with open('input.txt') as f:
        input = f.read().split('\n')
        card_power,bid = [],[]
        for i, item in enumerate(input,1):
            cards = item.split(' ')[0]
            bid = int(item.split(' ')[1])
            card_power.append([i,bid,deck_of_cards(cards)] + (cards_straight(cards)))
        sorted_lists = sorted(card_power, key=lambda x: x[2:8])
        price = 0
        for i, item in enumerate(sorted_lists,1):
            price += item[1]*i
        print(price)


if __name__ == "__main__":
    main()