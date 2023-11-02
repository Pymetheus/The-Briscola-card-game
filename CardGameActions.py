import random

class CardGameActions(object):

    def __init__(self):
        self.player_cards = []
        self.computer_cards = []
        self.dealt_cards = 3
        self.trump_card = ""
        self.test_modus = False

    def give_out_cards(self, cards):
        print("")
        print("GIVING OUT CARDS")
        print("")

        while (len(self.player_cards) != self.dealt_cards) and (len(self.computer_cards) != self.dealt_cards):
            give_player = cards.pop()
            self.player_cards.append(give_player)

            give_computer = cards.pop()
            self.computer_cards.append(give_computer)

        #print("")
        #print(f"Player has following cards: {player_cards}")
        #print(f"Computer has following cards: {computer_cards}")
        #print("")

    def select_trump_card(self, card_colors):
        print("")
        print("SELECTING TRUMP CARD")
        print("")

        if self.test_modus == True:
            print("\tRandom selected trump card.")
            print("")
            self.trump_card = random.choice(card_colors)
            print(f"\tThe trump card is {self.trump_card}")
            return self.trump_card
        else:
            while True:
                try:
                    print(f"\tWhich color do you want to select: {card_colors}")
                    selected_color = input("\t> ")

                    if selected_color in card_colors:
                        self.trump_card = selected_color
                        print(f"\tThe trump card is {self.trump_card}")
                        return self.trump_card
                    else:
                        print(f"\tThe color {selected_color} is not in your card colors: {card_colors}")
                except:
                    print("EXCEPTION")
                    break

    def player_select_card(self):
        print("")
        print("PLAYER SELECTING CARD")
        print("")

        if self.test_modus == True:
            print("\tTesting the computer with random seletced player cards.")
            print("")
            player_card = random.choice(self.player_cards)
            self.player_cards.remove(player_card)
            return player_card
        else:
            while True:
                try:
                    print(f"\tWhich card do you want to select: {self.player_cards}")
                    selected_card = input("\t> ")

                    if selected_card in self.player_cards:
                        player_card = selected_card
                        self.player_cards.remove(player_card)

                        print("")
                        print(f"\tThe player selected the card: {player_card}")
                        print(f"\tRemaining player cards: {self.player_cards}")
                        print("")

                        return player_card

                    else:
                        print(f"\tThe card {selected_card} is not in your cards: {player_cards}")
                except:
                    print("EXCEPTION")
                    break

    def computer_random_select_card(self):
        print("\tTesting the player with random seletced computer cards.")
        print("")
        computer_card = random.choice(self.computer_cards)
        self.computer_cards.remove(computer_card)
        return(computer_card)

    def sort_cards(self, cards, card_dictionary):
        sorted_cards = []
        sorted_dictionary = sorted(card_dictionary.items(), key=lambda x:x[1][1])

        for item in sorted_dictionary:
            if item[0] in cards:
                sorted_cards.append(item[0])
        return sorted_cards
