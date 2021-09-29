'''Player module'''
import deck_class as deck

class Player:
    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            # list of multiple cards
            self.all_cards.extend(new_cards)
        else:
            # single card
            self.all_cards.append(new_cards)

    def __str__(self):
        return 'Player {} has {} cards'.format(self.name, len(self.all_cards))
        # literal string did not work


# new_player = Player('Mawi')
# card=deck.Deck()
# mycard = card.deal_one()

# new_player.add_cards([mycard,mycard,mycard,mycard,mycard])
# print(new_player.all_cards[0])

# new_player.remove_one()
# print(new_player)

# extends merges items in one list with items in another List
