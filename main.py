import random
from calc_hand import calc_hand
from make_bet import make_bet
import variables

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
# pocket = 100
# wager = 0
# temp_pocket = pocket - int(wager)

while game_over is False:
	# shuffle cards
	random.shuffle(deck)

	# check if player is broke
	if variables.pocket == 0:
		print("You are out of money! Sorry!")
		break

	# ask for bet
	make_bet()

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
			winnings = variables.wager * 2
			variables.pocket += int(winnings)
			print('\nBlackJack! You Win!')
			print('You won $' + str(winnings) + "!")
			break

		make_bet()

		print("\nYour current hand total: " + str(player_score))

		if player_score > 21:
			print(str(player_score) + ' You busted!')
			variables.pocket -= variables.wager
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
			first_hand = False
			if player_score > 21:
				print('\nYou Busted! You lose your wager.')
				variables.pocket -= variables.wager
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
			winnings = variables.wager * 2
			variables.pocket += int(winnings)
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
				print("You lost " + "$" + str(variables.wager) + ".")
				variables.pocket -= variables.wager
				break

		if dealer_score > player_score:
			print("Player: " + str(player))
			print("Dealer: " + str(dealer))
			print("\nPlayer Score: " + str(player_score))
			print("\nDealer Score: " + str(dealer_score))
			print("\nDealer Wins!")
			print("You lost " + "$" + str(variables.wager) + ".")
			variables.pocket -= variables.wager
			break

		if dealer_score == player_score:
			variables.pocket += variables.wager
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
		variables.wager = 0
	else:
		game_over = True

print("Thanks for playing!")
