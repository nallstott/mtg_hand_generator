import random
import csv

with open('deck.csv', 'r') as deck_csv:
	reader = csv.reader(deck_csv)
	with open('deck_writer.csv', 'w') as deck_file_csv:
		writer = csv.writer(deck_file_csv)
		deck = {rows[0]: rows[1:] for rows in reader}

for card in deck.items():
	card[1][0] = int(card[1][0])


# def add_cards(card_name, details):
# 	deck[card_name.lower()] = details

# def remove_cards(card_name, number_to_remove):
# 	card_name = card_name.lower()
# 	if card_name in deck.keys():
# 		if deck[card_name][1][0] == 0:
# 			del deck[card_name]
# 		else:
# 			deck[card_name][1][0] -= number_to_remove
# 	else:
# 		print('Sorry, {} isn\'t in the deck right now. Add it using add_cards.'.format(card_name))

# def clear_deck():
# 	deck.clear()

def deck_count():
	count = 0
	for x in deck.values():
		count += x[0]
	if count == 60:
		return 'Your deck has 60 cards in it!'
	elif count < 60:
		return 'Um, your deck only has {} cards in it.'.format(count)
	else:
		return 'Your deck has {} cards in it. That\'s too many, you dumbass.'.format(count)

def get_random_card():
	return random.choice(list(deck.items()))

def generate_hand():
	hand = []
	while len(hand) < 11:
		current_card = get_random_card()
		if current_card in hand:
			count = 0
			for x in hand:
				count += 1
			if count > current_card[1][0]:
				continue
			else:
				hand.append(current_card)
		else:
			hand.append(current_card)
	return """
	{}

	Your opening hand is:
	{}: a {} type card that's cmc {},
	{}: a {} type card that's cmc {},
	{}: a {} type card that's cmc {},
	{}: a {} type card that's cmc {},
	{}: a {} type card that's cmc {},
	{}: a {} type card that's cmc {},
	{}: a {} type card that's cmc {},

	Your next three draws will be:
	{}: a {} type card that's cmc {},
	{}: a {} type card that's cmc {},
	{}: a {} type card that's cmc {},
	""".format(deck_count(), hand[0][0], hand[0][1][1], hand[0][1][2], hand[1][0], hand[1][1][1], hand[1][1][2], hand[2][0], hand[2][1][1], hand[2][1][2], hand[3][0], hand[3][1][1], hand[3][1][2], hand[4][0], hand[4][1][1], hand[4][1][2], hand[5][0], hand[5][1][1], hand[5][1][2], hand[6][0], hand[6][1][1], hand[6][1][2], hand[7][0], hand[7][1][1], hand[7][1][2], hand[8][0], hand[8][1][1], hand[8][1][2], hand[9][0], hand[9][1][1], hand[9][1][2])

print(generate_hand())

