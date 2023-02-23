import random

card_colors = ["Kreuz", "Pik", "Herz", "Karo"]
card_values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Bube", "Dame", "König", "Ass"]
card_points = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
card_rating = [0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 4, 10, 11]

card_dictionary = {}
card_deck = []

player_cards = []
computer_cards = []
trump_card = "Herz"
game_result = [0, 0]
game_result_points = [0, 0]

computers_turn = False
testing_modus = True

for index in range(len(card_colors)):
    for card, point, rating in zip(card_values, card_points, card_rating):
        card_dictionary[card_colors[index] + " " + card] = [card_colors[index], point, rating]

for item in card_dictionary.keys():
    card_deck.append(item)

def shuffle_cards(cards):
    print("")
    print("SHUFFLING CARDS")
    print("")

    shuffled_cards = cards.copy()
    random.shuffle(shuffled_cards)
    return shuffled_cards

def give_out_cards(cards):
    print("")
    print("GIVING OUT CARDS")
    print("")
    #print(len(player_cards))
    #print(len(computer_cards))

    while (len(player_cards) != 3) and (len(computer_cards) != 3):
        give_player = cards.pop()
        player_cards.append(give_player)

        give_computer = cards.pop()
        computer_cards.append(give_computer)

    #print("")
    #print(f"Player has following cards: {player_cards}")
    #print(f"Computer has following cards: {computer_cards}")
    #print("")

def select_trump_card():
    print("")
    print("SELECTING TRUMP CARD")
    print("")
    while True:
        try:
            print(f"\tWhich color do you want to select: {card_colors}")
            selected_color = input("\t> ")

            if selected_color in card_colors:
                trump_card = selected_color
                print(f"\tThe trump card is {trump_card}")
                return trump_card
            else:
                print(f"\tThe color {selected_color} is not in your card colors: {card_colors}")
        except:
            print("EXCEPTION")
            break

def player_select_card(player_cards):
    print("")
    print("PLAYER SELECTING CARD")
    print("")

    if testing_modus == True:
        print("\tTesting the computer with random seletced player cards.")
        print("")
        player_card = random.choice(player_cards)
        player_cards.remove(player_card)

        return(player_card)
    else:
        #print("Manual Game Modus")

        while True:
            try:
                print(f"\tWhich card do you want to select: {player_cards}")
                selected_card = input("\t> ")

                if selected_card in player_cards:
                    player_card = selected_card
                    player_cards.remove(player_card)

                    #print("")
                    #print(f"The player selected the card: {player_card}")
                    #print(f"Remaining player cards: {player_cards}")
                    #print("")

                    return(player_card)

                else:
                    print(f"\tThe card {selected_card} is not in your cards: {player_cards}")
            except:
                print("EXCEPTION")
                break

def computer_select_card(computer_cards, player_card = None):

    if computers_turn == False:
        played_color = card_dictionary[player_card][0]
        #print(f"Played color: {played_color}")

        #Try to beat player first with color card
        for card in computer_cards:
            #print(card_dictionary[card][0])
            if card_dictionary[card][0] == played_color:
                if card_dictionary[card][1] > card_dictionary[player_card][1]:
                    computer_card = card
                    #print(f"\tComputer selected card by color: {computer_card}")
                    computer_cards.remove(computer_card)
                    return computer_card

        #Try to beat player if card is equal to or higher then 10 if he has no trump card
        if card_dictionary[player_card][1] >= 10 and card_dictionary[player_card][0] != trump_card:
            for card in computer_cards:
                #print(card_dictionary[card][0])
                if card_dictionary[card][0] == trump_card:
                    computer_card = card
                    #print(f"\tComputer selected card by trump: {computer_card}")
                    computer_cards.remove(computer_card)
                    return computer_card

        #Try not to play trump card when player is playing a low trump card
        if card_dictionary[player_card][1] <= 10 and card_dictionary[player_card][0] == trump_card:
            for card in computer_cards:
                #print(card_dictionary[card][0])
                if card_dictionary[card][0] != trump_card and card_dictionary[card][1] <= 10:
                    computer_card = card
                    #print(f"\tComputer selected card lowest non trump card: {computer_card}")
                    computer_cards.remove(computer_card)
                    return computer_card

        #When not able to beat player by color or trump card
        computer_card = computer_cards[0]
        #print(f"\tComputer selected lowest card: {computer_card}")
        computer_cards.remove(computer_card)
        return computer_card

    else:
        #when computer starts try not to play trump card
        for card in computer_cards:
            if card_dictionary[card][0] != trump_card and card_dictionary[card][1] <= 10:
                computer_card = card
                #print(f"\tComputer selected card lowest non trump card: {computer_card}")
                computer_cards.remove(computer_card)
                return computer_card

        #When computer starts play lowest card
        computer_card = computer_cards[0]
        #print(f"\tComputer selected lowest card: {computer_card}")
        computer_cards.remove(computer_card)
        return computer_card

def sort_cards(cards):
    #print("")
    #print("SORTING CARDS")
    #print("")

    #print(f"Cards before sorting: {cards}")

    sorted_cards = []
    sorted_dictionary = sorted(card_dictionary.items(), key=lambda x:x[1][1])

    for item in sorted_dictionary:
        if item[0] in cards:
            sorted_cards.append(item[0])

    #print(f"Cards after sorting: {sorted_cards}")

    return sorted_cards

def determine_winner(p_card, c_card, c_turn):
    print("")
    print("DETERMINIG WINNER:")
    print("")

    if card_dictionary[p_card][0] == trump_card and card_dictionary[c_card][0] != trump_card:
        print("\tPLAYER WON with trump card")
        game_result[0] += 1
        game_result_points[0] += (card_dictionary[p_card][2] + card_dictionary[c_card][2])
        c_turn = False
    elif card_dictionary[p_card][0] != trump_card and card_dictionary[c_card][0] == trump_card:
        print("\tCOMPUTER WON with trump card")
        game_result[1] += 1
        game_result_points[1] += (card_dictionary[p_card][2] + card_dictionary[c_card][2])
        c_turn = True
    elif c_turn == False and card_dictionary[c_card][0] != card_dictionary[p_card][0]:
        print("\tPLAYER WON with colour")
        game_result[0] += 1
        game_result_points[0] += (card_dictionary[p_card][2] + card_dictionary[c_card][2])
        c_turn = False
    elif c_turn == True and card_dictionary[c_card][0] != card_dictionary[p_card][0]:
        print("\tCOMPUTER WON with colour")
        game_result[1] += 1
        game_result_points[1] += (card_dictionary[p_card][2] + card_dictionary[c_card][2])
        c_turn = True
    elif card_dictionary[p_card][0] == card_dictionary[c_card][0]:
        if card_dictionary[p_card][1] > card_dictionary[c_card][1]:
            print("\tPLAYER WON with higher card")
            game_result[0] += 1
            game_result_points[0] += (card_dictionary[p_card][2] + card_dictionary[c_card][2])
            c_turn = False
        else:
            print("\tCOMPUTER WON with higher card")
            game_result[1] += 1
            game_result_points[1] += (card_dictionary[p_card][2] + card_dictionary[c_card][2])
            c_turn = True
    else:
        print("### - ERROR - ###")

    print("")
    print(f"\tPlayer Card: {p_card}\n\tComputer Card: {c_card}")
    print("")
    print(f"\tPlayer won rounds: {game_result[0]} - Computer won rounds: {game_result[1]}")
    print(f"\tPlayer points: {game_result_points[0]} - Computer points: {game_result_points[1]}")
    print("")
    print("\t----------------------------------------")


    return c_turn


### MAIN GAME ###


playing_cards = shuffle_cards(card_deck)
#playing_cards = playing_cards[:8]

#print("")
#print("Those are the cards after shuffling:")
#print(playing_cards)

trump_card = select_trump_card()

while (len(playing_cards) != 0) or (len(player_cards) > 0):

    if len(playing_cards) > 0:
        give_out_cards(playing_cards)

    print(f"\tRemaining cards to give out: {len(playing_cards)}")
    print("")

    if computers_turn == False:
        print("")
        print("PLAYERS TURN")
        print("")

        player_selected_card = player_select_card(player_cards)

        print("")
        print(f"\tPLAYER SELECTED CARD: {player_selected_card}")
        print(f"\tRemaining player cards: {player_cards}")
        print("")

        print("")
        print("COMPUTER REACTING")
        computer_cards = sort_cards(computer_cards)

        computer_selected_card = computer_select_card(computer_cards, player_selected_card)

        print("")
        print(f"\tCOMPUTER SELECTED CARD: {computer_selected_card}")
        #print(f"Remaining computer cards: {computer_cards}")
        print("")

        computers_turn = determine_winner(player_selected_card, computer_selected_card, computers_turn)

    else:
        print("")
        print("COMPUTERS TURN")
        print("")

        print("")
        #print("The computer is sorting his cards")
        computer_cards = sort_cards(computer_cards)

        computer_selected_card = computer_select_card(computer_cards)

        print("")
        print(f"\tCOMPUTER SELECTED CARD: {computer_selected_card}")
        #print(f"Remaining computer cards: {computer_cards}")
        print("")

        print("")
        print("PLAYERS TURN")
        print("")

        player_selected_card = player_select_card(player_cards)

        print("")
        print(f"PLAYER SELECTED CARD: {player_selected_card}")
        print(f"Remaining player cards: {player_cards}")
        print("")

        computers_turn = determine_winner(player_selected_card, computer_selected_card, computers_turn)
