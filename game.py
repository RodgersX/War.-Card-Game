# create two instances of player 1 and player 2
# create a deck and shuffle it before splitting it among the players
# check if someone lost. check for 0 cards
import card_class as card
import deck_class as deck
import player_class as player

player1 = player.Player('One')
player2 = player.Player('Two')

new_deck = deck.Deck()
new_deck.shuffle_deck()

for x in range(26):  # assign two cards at a go.
    player1.add_cards(new_deck.deal_one())
    player2.add_cards(new_deck.deal_one())

# print(player1.all_cards[6])
gameon = True
round_num = 0
while gameon:
    round_num += 1  # counter for the rounds played
    print('Round {}'.format(round_num))

    # check if player out of cards
    if len(player1.all_cards) == 0:
        print('Player 1 out of cards! Player 2 wins')
        gameon = False
        break

    if len(player2.all_cards) == 0:
        print('Player 2 out of cards! Player 1 wins')
        gameon = False
        break

    # start new round
    player_one_cards = []  # cards in play for player 1
    player_one_cards.append(player1.remove_one())  # dish out a card to play

    player_two_cards = []  # cards in play for player 2
    player_two_cards.append(player2.remove_one())

    # check player cards against each other
    while True:
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player1.add_cards(player_one_cards)
            player1.add_cards(player_two_cards)
            break

        elif player_two_cards[-1].value > player_one_cards[-1].value:
            player2.add_cards(player_two_cards)
            player2.add_cards(player_one_cards)
            break

        else:
            print('WAR!')

            if len(player1.all_cards) < 5:
                print('Player 1 not able to fight back')
                print('Player 2 wins')
                gameon = False
                break

            elif len(player1.all_cards) < 5:
                print('Player 2 not able to fight back')
                print('Player 1 wins')
                gameon = False
                break

            else:
                for num in range(5):
                    player_one_cards.append(player1.remove_one())
                    player_two_cards.append(player2.remove_one())
