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


all_possible_words = generer_dico('documents/littre.txt')
word_with_u = [word for word in all_possible_words if word[0] == "u"]

# just to save names, cuz we have a loot
# mots_jouables_arg_1 = ["COURIR", "PIED", "DEPIT", "TAPIR", "MARCHER"]
# mots_jouables_arg_2 = ["P", "I", "D", "E"]
# mots_jouables(mots_jouables_arg_1, mots_jouables_arg_2, extras=0)

# # ------- TEST CASE -------- #
# # Amelioration: les mots peuvent etre places en exploitant les jetons deja poses sur le plateau. Completer ces fonctions
# # pour generer des listes de mots jouables avec les lettres de la main plus une lettre manquante, ou plus plusieurs
# # lettres manquantes(on pourra passer ce nombre en parametre).


# ['abc', 'cab', 'abcd', 'bacd', 'abcdef']
# ['a', 'b', 'c']
# with all the letters, it returns
# ['abc', 'cab']

# with 1 letter missing it returns or with ['d'] as the argument
# ['abc', 'cab'] + ['abcd', 'bacd']

# with 2 letters missing it returns or with ['d', 'e'] as the argument
# ['abc', 'cab'] + ['abcd', 'bacd'] + ['abcedf']
