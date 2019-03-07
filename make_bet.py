def make_bet():

	global wager
	global pocket
	global temp_pocket

	betting = True
	print("You currently have: $" + str(temp_pocket) + " to bet.")
	while betting:
		print("Your current bet is $" + str(wager))
		bet = input("Enter the amount you would like to bet: ")

		if bet.isdigit():
			wager += int(bet)
			if int(wager) > int(temp_pocket):
				print("You cannot bet more than you have")
				wager -= int(bet)
			else:
				betting = False
		else:
			print('Please enter a valid number')



pocket = 100
wager = 0
temp_pocket = pocket - int(wager)
