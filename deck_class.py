'''Deck module'''
from random import shuffle
import card_class as card


class Deck:
    '''deck class'''
    def __init__(self):
        self.all_cards = []
        for suit in card.suits:
            for rank in card.ranks:
                created_card = card.Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle_deck(self): # shuffle the cards
        shuffle(self.all_cards)

    def deal_one(self): # pop one card from the list
        return self.all_cards.pop()

# new_d = Deck()
# new_d.shuffle_deck()

# my_card=new_d.deal_one()

# print(my_card)
# print(len(new_d.all_cards))

# for card_obj in new_d.all_cards:
#     print(card_obj)
