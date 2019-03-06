# function to print cards with brackets around value
def show_cards(hand):
	b = []
	for i in hand:
		i = "[" + i + "]"
		b.append(i)
	print(b)
