import random


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


# create deck of cards
deck = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A",
        "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A",
        "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A",
        "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A",

        ]
# flags for if first hand and if player is standing
first_hand = True
standing = False
game_over = False

# create hand for players and dealer
player = []
dealer = []

# define total amount to bet
pocket = 100
wager = 0

while game_over is False:
    # shuffle cards
    random.shuffle(deck)

    # ask for bet
    print("\nYou currently have $" + str(pocket))
    bet = (input("Make your initial bet: "))
    if bet.isdigit():
        wager += int(bet)
    else:
        bet = int(input('Please type a number: '))
        wager += int(bet)

    # deal cards
    print('Dealing cards...')
    player.append(deck.pop())
    dealer.append(deck.pop())
    player.append(deck.pop())
    dealer.append(deck.pop())

    # calculate hands
    player_score = calc_hand(player)
    dealer_score = calc_hand(dealer)

    # show the table
    print("Player's hand: " + "[" + player[0] + "]" + "[" + player[1] + "]")

    print("\nDealers's hand: " + "[" + dealer[0] + "]" + "[?]")

    print("\nYour current hand total: " + str(player_score))
    # main game loop

    while not standing:
        player_score = calc_hand(player)
        dealer_score = calc_hand(dealer)

        if player_score == 21 and first_hand:
            winnings = wager * 2
            pocket += int(winnings)
            print('\nBlackJack! You Win!')
            print('You won $' + str(winnings) + "!")
            break

        print("\nYou are currently betting $" + str(wager))
        bet = (input("How much would you like to bet? "))
        if bet.isdigit():
            wager += int(bet)
        else:
            bet = int(input('Please type a number: '))
            wager += int(bet)

        print("\nYour current hand total: " + str(player_score))

        if player_score > 21:
            print(str(player_score) + ' You busted!')
            break
        if player_score == 21:
            standing = True

        move = str(input("\nWould you like to hit[1] or stand[2]? "))

        if move == '1':
            player.append(deck.pop())
            print(str(player))
            player_score = calc_hand(player)
            dealer_score = calc_hand(dealer)
            print("\nYour current hand total: " + str(player_score))

            if player_score > 21:
                print('\nYou Busted! You lose your wager.')
                pocket -= wager
                break

        elif move == '2':
            standing = True
        else:
            print("please type [1] or [2]")

    # standing, dealers turn
    while standing:
        player_score = calc_hand(player)
        dealer_score = calc_hand(dealer)

        if dealer_score > 21:
            winnings = wager * 2
            pocket += int(winnings)
            print("Player: " + str(player))
            print("Dealer: " + str(dealer))
            print("\nPlayer Score: " + str(player_score))
            print("\nDealer Score: " + str(dealer_score))
            print("\nThe Dealer Busts. You win!")
            print('You won ' + "$" + str(winnings) + "!")
            break

        if dealer_score == 21:
            if dealer_score != player_score:
                print("Player: " + str(player))
                print("Dealer: " + str(dealer))
                print("\nPlayer Score: " + str(player_score))
                print("\nDealer Score: " + str(dealer_score))
                print("\nThe Dealer has BlackJack.  You lose")
                print("You lost " + "$" + str(wager) + ".")
                pocket -= wager
                break

        if dealer_score > player_score:
            print("Player: " + str(player))
            print("Dealer: " + str(dealer))
            print("\nPlayer Score: " + str(player_score))
            print("\nDealer Score: " + str(dealer_score))
            print("\nDealer Wins!")
            print("You lost " + "$" + str(wager) + ".")
            pocket -= wager
            break

        if dealer_score == player_score:
            print("Player: " + str(player))
            print("Dealer: " + str(dealer))
            print("\nPlayer Score: " + str(player_score))
            print("\nDealer Score: " + str(dealer_score))
            print("\nThis game is a draw")
            print("You get back your wager!")
            break

        print('\nDrawing card for dealer...')
        dealer.append(deck.pop())
        print(str(dealer))

    again = input("\nWould you like to play again? Type 'y' or 'n': ")
    if again == 'y':
        game_over = False
        standing = False
        player = []
        dealer = []
        wager = 0
    else:
        game_over = True

    if pocket < 0:
        game_over = True

print("Thanks for playing!")
