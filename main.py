from functions import *


board = init_bonus()
print_list(board)


empty_jetons = init_jeton()
print_list(empty_jetons)


new_jetons_board = affiche_jetons(
    empty_jetons, [[0, 0], [0, 3], [1, 1], [1, 5],  [1, 2]])
print_list(new_jetons_board)
