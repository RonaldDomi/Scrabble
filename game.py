from functions import *


def tour_joueur(player, board):
    """
        desciption by Farah: shows us the board, gives the player choices to play\n
        if player acts, updates the board, and all that jizz\n
    """
    print("old sac : ", sac)

    hand = players_dico[player]['hand']
    print("hand: ", hand)
    choice = int(input(
        "what do you want to do, (skip, draw, place), enter a number(1-3): "))
    if choice == 1:
        # skip
        return
    elif choice == 2:
        # draw
        shitty_word = input(
            "what jetons would you like to exchange? ")  # "abcd"

        selected_jetons = list(shitty_word)
        # we use _ for variables we never use
        updated_hand = echanger(selected_jetons, hand, sac)[0]
        print("changed ", len(selected_jetons), ' letters')
    elif choice == 3:
        # place word

        # get ready the words
        list_of_all_possible_words = generer_dico('documents/littre.txt')
        available_words = mots_jouables(list_of_all_possible_words, hand, 0)
        best_words = meilleurs_mots(available_words, hand, letters_dico)
        print('best option: ', best_words)

        chosen_word = input("What word would you like to place? ")

        # read the coordinates
        coordinates_of_word = lire_coords(board)

        row = coordinates_of_word[0]
        column = coordinates_of_word[1]
        direction = coordinates_of_word[2]

        # place the word
        letters_that_need_to_be_put = tester_placement(
            board, row, column, direction, chosen_word)
        placer_mot(board, hand, chosen_word, row, column, direction)

        # update the player score
        played_word_value = valeur_mot_better(
            direction, chosen_word, letters_dico, bonus_board, row, column)

        players_dico[player]["score"] += played_word_value
        updated_hand = completer_main(hand, sac)
    players_dico[player]["hand"] = updated_hand
    print(player, "'s hand: ", updated_hand)
    print("new sac : ", sac)
    print("player ", player, " has ", players_dico[player]["score"], " points")


def remove_hand_points(hand, letters_points_dic):
    points_to_be_removed = 0
    for hand_letter in hand:
        points_to_be_removed += letters_points_dic[hand_letter.lower()]['val']

    return points_to_be_removed


#--------------------------- variable initialisation ------------------#
letters_dico = letters_dico()
sac = init_sac(letters_dico)

players_dico = {}
# player1 = input("first player ")
player1 = "Farah"
# player2 = input("second player ")
player2 = "Ronald"
hand1 = piocher(10, sac)
hand2 = piocher(10, sac)
score1 = 0
score2 = 0

players_dico[player1] = {}
players_dico[player1]['hand'] = hand1
players_dico[player1]['score'] = score1
players_dico[player1]['turn'] = 1
players_dico[player2] = {}
players_dico[player2]['hand'] = hand2
players_dico[player2]['score'] = score2
players_dico[player2]['turn'] = 2

turn = 1
bonus_board = init_bonus_board()
#--------------------------- variable initialisation ------------------#


#--------------------------- game loop ------------------#
board_list = init_jeton()
is_playing = True
close_next_turn = False
while is_playing:
    print('\n\n\n\n')
    if turn % 2 == 0:
        print(player2, "'s turn: ")
        tour_joueur(player2, board_list)
        if close_next_turn:
            is_playing = False
    else:
        print(player1, "'s turn: ")
        tour_joueur(player1, board_list)
        if close_next_turn:
            is_playing = False
    print_list(board_list)

    if(len(sac) == 0):
        close_next_turn = True

    turn += 1

#--------------------------- game loop ------------------#


#--------------------------- end game ------------------#
print('\n\n\n')
print('the game has ended')
print(player1, "'s points before removing hand points are: ",
      players_dico[player1]["score"])
print(player2, "'s points before removing hand points are: ",
      players_dico[player2]["score"])
players_dico[player1]["score"] -= remove_hand_points(
    players_dico[player1]['hand'], letters_dico)
players_dico[player2]["score"] -= remove_hand_points(
    players_dico[player2]['hand'], letters_dico)
print(player1, "'s points after removing hand points are: ",
      players_dico[player1]["score"])
print(player2, "'s points after removing hand points are: ",
      players_dico[player2]["score"])

#--------------------------- end game ------------------#
