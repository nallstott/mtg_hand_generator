# Go back later and make this work with a csv file as a single input, run all the functions, and then return the hand
# When adding cards, details go [Number in deck, card type, CMC, notable details]
import random

deck = {}

def add_cards(card_name, details):
	deck[card_name.lower()] = details

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
	while len(hand) < 8:
		current_card = get_random_card()
		if current_card in hand:
			count = 0
			for x in hand:
				count += 1
			if count > current_card[1][0]:
				continue
			else:
				hand.append(current_card[0])
		else:
			hand.append(current_card[0])
	return """
	{}
	{}
	{}
	{}
	{}
	{}
	{}
	""".format(hand[0], hand[1], hand[2], hand[3], hand[4], hand[5], hand[6])





add_cards('Light Up The Stage', [3, 'sorcery', 'CCR', 'spectacle'])
add_cards('Lightning Bolt', [4, 'instant', 'R', ])
add_cards('Goblin Guide', [4, 'creature', 'R', 'haste'])
add_cards('Monestary Swiftspear', [4, 'creature', 'R', 'haste and prowess'])
add_cards('Eidolon of the Great Revel', [4, 'creature', 'RR', 'damage on cast 3cmc or less'])
add_cards('Lava Spike', [4, 'sorcery', 'R'])
add_cards('Boros Charm', [4, 'instant', 'RW', '4 damage, indestructable or doublestrike creatures'])
add_cards('Searing Blaze', [3, 'instant', 'RR', 'w/landfall, 3 damage to creature and player'])
add_cards('Lightning Helix', [2, 'instant', 'RW', '3 damage to target, gain 3 life'])
add_cards('Rift Bolt', [2, 'sorcery', 'CCR', 'suspend R'])
add_cards('Skewer the Critics', [4, 'sorcery', 'CCR', 'spectacle'])
add_cards('Skullcrack', [2, 'instant', 'CR', 'prevent lifegain'])
add_cards('Grim Lavamancer', [1, 'creature', 'R', 'exile 2 cards for 2 damage to target'])
add_cards('Wooded Foothills', [3, 'land', 'none', 'RG fetch'])
add_cards('Arid Mesa', [3, 'land', 'none', 'RW fetch'])
add_cards('Sunbaked Canyon', [4, 'land', 'none', 'RW horizon land'])
add_cards('Sacred Foundry', [2, 'land', 'none', 'RW shock land'])
add_cards('Bloodstained Mire', [3, 'land', 'none', 'RB fetch'])
add_cards('Mountain', [3, 'basic land', 'none', 'R basic'])
add_cards('Stomping Grounds', [1, 'land', 'none', 'RG shock land'])


# print(generate_hand())
print(generate_hand())


