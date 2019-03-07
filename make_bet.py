import variables

def make_bet():
	""" function to add betting.  checks for correct value for bet and if bet is too high """
	temp_pocket = variables.pocket - int(variables.wager)
	betting = True
	print("You currently have: $" + str(temp_pocket) + " to bet.")
	while betting:
		print("Your current bet is $" + str(variables.wager))
		bet = input("Enter the amount you would like to bet: ")

		if bet.isdigit():
			if int(bet) > int(temp_pocket):
				print("You cannot bet more than you have")
			else:
				variables.wager += int(bet)
				betting = False
		else:
			print('Please enter a valid number')


