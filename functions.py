import copy


cases_MT = [[0, 0], [0, 7], [0, 14], [7, 0],
            [7, 14], [14, 0], [14, 7], [14, 14]]
cases_MD = [[1, 1], [1, 13], [2, 2], [2, 12], [3, 3], [3, 11], [4, 4], [4, 10], [
    7, 7], [10, 4], [10, 10], [11, 3], [11, 11], [12, 2], [12, 12], [13, 1], [13, 13]]
cases_LT = [[1, 5], [1, 9], [5, 1], [5, 5], [5, 9], [5, 13],
            [9, 1], [9, 5], [9, 9], [9, 13], [13, 5], [13, 9]]
cases_LD = [[0, 3], [0, 11], [2, 6], [2, 8], [3, 0], [3, 7], [3, 14], [6, 2], [6, 6], [6, 8], [6, 12], [7, 3], [
    7, 11], [8, 2], [8, 6], [8, 8], [8, 12], [11, 0], [11, 7], [11, 14], [12, 6], [12, 8], [14, 3], [14, 11]]


def init_bonus():
    board = []
    for i in range(15):  # columns
        board.append([])
    for j in range(15):  # columns
        for i in range(15):  # rows
            board[j].append([j, i])
    # fills the board
    for rowIndex in range(15):  # [ []  [] ]
        for cellIndex in range(15):
            if board[rowIndex][cellIndex] in cases_MT:
                board[rowIndex][cellIndex] = "MT"
            elif board[rowIndex][cellIndex] in cases_MD:
                board[rowIndex][cellIndex] = "MD"
            elif board[rowIndex][cellIndex] in cases_LT:
                board[rowIndex][cellIndex] = "LT"
            elif board[rowIndex][cellIndex] in cases_LD:
                board[rowIndex][cellIndex] = "LD"
            else:
                board[rowIndex][cellIndex] = "  "
    return board


def init_jeton():
    empty_board = []
    for i in range(15):  # columns
        empty_board.append([])
    for j in range(15):  # columns
        for i in range(15):  # rows
            empty_board[j].append("   ")
    return empty_board


def affiche_jetons(empty_jetons, list_jetons):

    new_jetons_board = copy.deepcopy(empty_jetons)
    for row_index in range(15):
        for cell_index in range(15):
            if [row_index, cell_index] in list_jetons:

                if [row_index, cell_index] in cases_MT:
                    new_jetons_board[row_index][cell_index] = "jMT"
                elif [row_index, cell_index] in cases_MD:
                    new_jetons_board[row_index][cell_index] = "jMD"
                elif [row_index, cell_index] in cases_LT:
                    new_jetons_board[row_index][cell_index] = "jLT"
                elif [row_index, cell_index] in cases_LD:
                    new_jetons_board[row_index][cell_index] = "jLD"
                else:
                    new_jetons_board[row_index][cell_index] = "j  "
            else:
                cell = ""

    return new_jetons_board


def print_list(board_list):
    for row in board_list:
        print(row)
        print()
    print()
    print()
