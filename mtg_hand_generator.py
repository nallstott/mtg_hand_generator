deck = {}

def add_cards(card_name, number_in_deck):
	deck[card_name.lower()] = number_in_deck

def remove_cards(card_name, number_to_remove):
	card_name = card_name.lower()
	if card_name in deck.keys():
		if deck[card_name] == 0:
			del deck[card_name]
		else:
			deck[card_name] -= number_to_remove
	else:
		print('Sorry, {} isn\'t in the deck right now. Add it using add_cards.'.format(card_name))

def clear_deck():
	deck.clear()


add_cards('Poluted Delta', 4)
remove_cards('Poluted Delta', 1)
print(deck.items())
clear_deck()
print(deck.items())