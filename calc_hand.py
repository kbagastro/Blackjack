# function to calculate hand total
def calc_hand(hand):
    non_aces = [card for card in hand if card != 'A']
    aces = [card for card in hand if card == 'A']

    sum = 0

    for card in non_aces:
        if card in 'JQK':
            sum += 10
        else:
            sum += int(card)

    for card in aces:
        if sum <= 10:
            sum += 11
        else:
            sum += 1

    return sum
