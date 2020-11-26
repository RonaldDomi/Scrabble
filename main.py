from functions import *
# import copy

board = init_bonus()
# print_list(board)


empty_jetons = init_jeton()
# print_list(empty_jetons)


new_jetons_board = affiche_jetons(
    empty_jetons, [[0, 0], [0, 3], [1, 1], [1, 5],  [1, 2]])
# print_list(new_jetons_board)


letters_dico = init_dico()
letters_list = init_pioche(letters_dico)
first_hand = piocher(2, letters_list)
completed_hand = completer_main(first_hand, letters_list)
exchanged_hand, letters_list, did_exchange = echanger(
    completed_hand[0:2], completed_hand, letters_list)
