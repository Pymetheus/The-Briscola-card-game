import random

class CardGame(object):

    def __init__(self):
        self.card_dictionary = {}
        self.card_deck = []

    def print_card_dictionary(self):
        for item, key in zip(self.card_dictionary.keys(), self.card_dictionary.values()):
            print(item, key)

    def create_card_deck(self, card_dictionary):
        for item in card_dictionary.keys():
            self.card_deck.append(item)
        return self.card_deck

    def shuffle_cards(self, cards):
        print("")
        print("SHUFFLING CARDS")
        print("")

        shuffled_cards = cards.copy()
        random.shuffle(shuffled_cards)
        return shuffled_cards
