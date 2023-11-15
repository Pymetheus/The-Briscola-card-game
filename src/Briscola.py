from CardGame import CardGame
from CardGameActions import CardGameActions

class Briscola(CardGame):

    def __init__(self):
        super().__init__()
        self.create_briscola_card_dictionary()
        self.create_card_deck(self.card_dictionary)

    def create_briscola_card_dictionary(self):
        self.card_colors = ["Swords", "Cups", "Coins", "Sticks"]
        self.card_values = ["2", "4", "5", "6", "7", "Jack", "Queen", "King", "Three", "Ace"]
        self.card_points = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.card_rating = [0, 0, 0, 0, 0, 2, 3, 4, 10, 11]

        for index in range(len(self.card_colors)):
            for card, point, rating in zip(self.card_values, self.card_points, self.card_rating):
                self.card_dictionary[self.card_colors[index] + " " + card] = [self.card_colors[index], point, rating]
        return self.card_dictionary


class BriscolaGameActions(CardGameActions):

    def __init__(self):
        super().__init__()
        self.card_dictionary = Briscola().card_dictionary
        self.computers_turn = False
        self.game_result = [0, 0]
        self.game_result_points = [0, 0]

    def computer_select_card(self, player_card = None):

        if self.computers_turn == False:
            played_color = self.card_dictionary[player_card][0]

            #Try to beat player first with color card
            for card in self.computer_cards:
                if self.card_dictionary[card][0] == played_color:
                    if self.card_dictionary[card][1] > self.card_dictionary[player_card][1]:
                        computer_card = card
                        #print(f"\tComputer selected card by color: {computer_card}")
                        self.computer_cards.remove(computer_card)
                        return computer_card

            #Try to beat player if card is equal to or higher then 10 if he has no trump card
            if self.card_dictionary[player_card][1] >= 6 and self.card_dictionary[player_card][0] != self.trump_card:
                for card in self.computer_cards:
                    if self.card_dictionary[card][0] == self.trump_card:
                        computer_card = card
                        #print(f"\tComputer selected card by trump: {computer_card}")
                        self.computer_cards.remove(computer_card)
                        return computer_card

            #Try not to play trump card when player is playing a low trump card
            if self.card_dictionary[player_card][1] <= 6 and self.card_dictionary[player_card][0] == self.trump_card:
                for card in self.computer_cards:
                    if self.card_dictionary[card][0] != self.trump_card and self.card_dictionary[card][1] <= 6:
                        computer_card = card
                        #print(f"\tComputer selected card lowest non trump card: {computer_card}")
                        self.computer_cards.remove(computer_card)
                        return computer_card

            #When not able to beat player by color or trump card
            computer_card = self.computer_cards[0]
            #print(f"\tComputer selected lowest card: {computer_card}")
            self.computer_cards.remove(computer_card)
            return computer_card

        else:
            #when computer starts try not to play trump card
            for card in self.computer_cards:
                if self.card_dictionary[card][0] != self.trump_card and self.card_dictionary[card][1] <= 6:
                    computer_card = card
                    #print(f"\tComputer selected card lowest non trump card: {computer_card}")
                    self.computer_cards.remove(computer_card)
                    return computer_card

            #When computer starts play lowest card
            computer_card = self.computer_cards[0]
            #print(f"\tComputer selected lowest card: {computer_card}")
            self.computer_cards.remove(computer_card)
            return computer_card

    def determine_winner(self, p_card, c_card):
        print("")
        print("DETERMINIG WINNER:")
        print("")

        if self.card_dictionary[p_card][0] == self.trump_card and self.card_dictionary[c_card][0] != self.trump_card:
            print("\tPLAYER WON with trump card")
            self.computers_turn = False
        elif self.card_dictionary[p_card][0] != self.trump_card and self.card_dictionary[c_card][0] == self.trump_card:
            print("\tCOMPUTER WON with trump card")
            self.computers_turn = True
        elif self.computers_turn == False and self.card_dictionary[c_card][0] != self.card_dictionary[p_card][0]:
            print("\tPLAYER WON with colour")
            self.computers_turn = False
        elif self.computers_turn == True and self.card_dictionary[c_card][0] != self.card_dictionary[p_card][0]:
            print("\tCOMPUTER WON with colour")
            self.computers_turn = True
        elif self.card_dictionary[p_card][0] == self.card_dictionary[c_card][0]:
            if self.card_dictionary[p_card][1] > self.card_dictionary[c_card][1]:
                print("\tPLAYER WON with higher card")
                self.computers_turn = False
            else:
                print("\tCOMPUTER WON with higher card")
                self.computers_turn = True
        else:
            print("### - ERROR - ###")

        if self.computers_turn == False:
            print("\tPLAYER getting the points")
            self.game_result[0] += 1
            self.game_result_points[0] += (self.card_dictionary[p_card][2] + self.card_dictionary[c_card][2])
        elif self.computers_turn == True:
            print("\tCOMPUTER getting the points")
            self.game_result[1] += 1
            self.game_result_points[1] += (self.card_dictionary[p_card][2] + self.card_dictionary[c_card][2])
        else:
            print("### - ERROR - ###")

        print("")
        print(f"\tPlayer Card: {p_card}\n\tComputer Card: {c_card}")
        print("")
        print(f"\tPlayer won rounds: {self.game_result[0]} - Computer won rounds: {self.game_result[1]}")
        print(f"\tPlayer points: {self.game_result_points[0]} - Computer points: {self.game_result_points[1]}")
        print("")
        print("\t----------------------------------------")


        return self.computers_turn

    def play_game(self):
        playing_cards = Briscola().shuffle_cards(Briscola().card_deck)
        self.select_trump_card(Briscola().card_colors)

        while (len(playing_cards) != 0) or (len(self.player_cards) > 0):
            if len(playing_cards) > 0:
                self.give_out_cards(playing_cards)

            print(f"\tRemaining cards to give out: {len(playing_cards)}")

            if self.computers_turn == False:
                print("")
                print("PLAYER IS STARTING")
                player_selected_card = self.player_select_card()

                print("")
                print("COMPUTER REACTING")
                self.computer_cards = self.sort_cards(self.computer_cards, self.card_dictionary)
                computer_selected_card = self.computer_select_card(player_selected_card)
                print("")
                print(f"\tCOMPUTER SELECTED CARD: {computer_selected_card}")

                self.computers_turn = self.determine_winner(player_selected_card, computer_selected_card)

            else:
                print("")
                print("COMPUTER IS STARTING")
                self.computer_cards = self.sort_cards(self.computer_cards, self.card_dictionary)
                computer_selected_card = self.computer_select_card()
                print("")
                print(f"\tCOMPUTER SELECTED CARD: {computer_selected_card}")

                print("")
                print("PLAYERS TURN")
                player_selected_card = self.player_select_card()

                self.computers_turn = self.determine_winner(player_selected_card, computer_selected_card)
