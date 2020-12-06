from functions import *
# import copy

board = init_bonus()
# print_list(board)


empty_jetons = init_jeton()
# print_list(empty_jetons)


# new_jetons_board = affiche_jetons(
#     empty_jetons, [[0, 0], [0, 3], [1, 1], [1, 5],  [1, 2], [4, 5], [4, 7]])  # what does empty jetons do in the function
new_jetons_board = affiche_jetons(
    empty_jetons, [])  # what does empty jetons do in the function


letter_value_dico = init_dico()
letters_list = init_pioche(letter_value_dico)
first_hand = piocher(2, letters_list)
completed_hand = completer_main(first_hand, letters_list)
exchanged_hand, letters_list, did_exchange = echanger(
    completed_hand[0:2], completed_hand, letters_list)


all_possible_words = generer_dico('documents/littre.txt')
word_with_u = [word for word in all_possible_words if word[0] == "u"]

# mots_jouables_arg_1 = ["COURIR", "PIED", "DEPIT", "DEPTI", "TAPIR", "MARCHER"]
# mots_jouables_arg_2 = ["P", "I", "D", "E", "T", "A", "R"]
# mots_jouables(mots_jouables_arg_1, mots_jouables_arg_2, extras=0)

# value = valeur_mot('ronaldd', letter_value_dico)

# meilleur_mott = meilleur_mot(
#     mots_jouables_arg_1, mots_jouables_arg_2, letter_value_dico)

# meilleurs_motts = meilleurs_mots(
#     mots_jouables_arg_1, mots_jouables_arg_2, letter_value_dico)

# coords_list = lire_coords(new_jetons_board)

# tester_placement(new_jetons_board, 1, 1, "vertical", "roni")

hand_letters = list("domihebdis")
mot = 'domi'
direction = 'vertical'
placer_mot(new_jetons_board, hand_letters, mot, 1, 1, direction)

print_list(new_jetons_board)

# value1 = valeur_mot(mot, letter_value_dico)
value2 = valeur_mot_better(
    direction, mot, letter_value_dico, board, 1, 1)
# print(value1, value2)

# print(letter_value_dico)
