import copy
from random import randint
from random import choice

cases_MT = [[0, 0], [0, 7], [0, 14], [7, 0],
            [7, 14], [14, 0], [14, 7], [14, 14]]
cases_MD = [[1, 1], [1, 13], [2, 2], [2, 12], [3, 3], [3, 11], [4, 4], [4, 10], [
    7, 7], [10, 4], [10, 10], [11, 3], [11, 11], [12, 2], [12, 12], [13, 1], [13, 13]]
cases_LT = [[1, 5], [1, 9], [5, 1], [5, 5], [5, 9], [5, 13],
            [9, 1], [9, 5], [9, 9], [9, 13], [13, 5], [13, 9]]
cases_LD = [[0, 3], [0, 11], [2, 6], [2, 8], [3, 0], [3, 7], [3, 14], [6, 2], [6, 6], [6, 8], [6, 12], [7, 3], [
    7, 11], [8, 2], [8, 6], [8, 8], [8, 12], [11, 0], [11, 7], [11, 14], [12, 6], [12, 8], [14, 3], [14, 11]]


def init_bonus():
    """
        15x15 list of lists with bonuses
    """
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
    """"
        15x15 list of lists of empty cells
    """
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


def init_dico():
    """
        dictionary with the values of each letter of the alphabet
    """
    values_list = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 10, 1,
                   2, 1, 1, 3, 8, 1, 1, 1, 1, 4, 10, 10, 10, 10]
    numbers_list = [9, 2, 2, 3, 15, 2, 2, 2, 8, 1, 1,
                    5, 3, 6, 6, 2, 1, 6, 6, 6, 6, 2, 1, 1, 1, 1]
    letters_dictionary = {}
    letter = 'a'
    for i in range(26):
        letters_dictionary[chr(
            ord('a')+i)] = {"occ": numbers_list[i], "val": values_list[i]}
    letters_dictionary["?"] = {"occ": 2, "val": 0}
    return letters_dictionary


def init_pioche(dico):
    pioche_list = []
    for keys in dico:
        number_of_repetition = dico[keys]["occ"]
        for n in range(number_of_repetition):
            pioche_list.append(keys)

    return pioche_list


def piocher(number, sac):
    hand_drawn = []
    for i in range(number):
        new_letter = choice(sac)
        hand_drawn.append(new_letter)
        sac.remove(new_letter)
    return hand_drawn


def completer_main(current_hand, sac):
    # global our_hand
    hand_length = len(current_hand)
    additions_number = 7-hand_length
    if len(sac) < additions_number:
        additions = piocher(len(sac), sac)
    else:
        additions = piocher(additions_number, sac)
    current_hand = current_hand + additions
    return current_hand


def echanger(jetons, my_hand, sac):
    hand_length = len(jetons)
    additions = []
    did_exchange = False
    if(len(sac) >= 7):
        additions = piocher(hand_length, sac)
        for jeton in jetons:
            my_hand.remove(jeton)
        sac = sac + jetons
        did_exchange = True

    my_hand = my_hand + additions
    return [my_hand, sac, did_exchange]


def generer_dico(file):
    with open(file, 'r') as our_file:
        data = our_file.readlines()
        lower_case_words = [x.lower()[:-1]
                            for x in data]
    return lower_case_words


def mot_jouable(our_word, list_of_available_letters):
    jouable = True
    letters_copy = copy.copy(list_of_available_letters)
    for letter in our_word:
        if letter not in letters_copy:
            if '?' in letters_copy:
                letters_copy.remove("?")
            else:
                jouable = False
        else:
            letters_copy.remove(letter)

    return jouable


def mots_jouables(words_list, list_of_available_letters, extras):  # extras is a number
    list_of_available_letters_copy = copy.copy(list_of_available_letters)
    list_of_available_letters_copy += ['?'] * extras

    mots_jouables = []
    for word in words_list:
        if mot_jouable(word, list_of_available_letters_copy):
            mots_jouables.append(word)
    # print(mots_jouables)
    return mots_jouables


def valeur_mot(mot, dico):
    total = 0
    print(mot, ' has ', end='')
    for letter in mot:
        print(dico[letter.lower()]['val'], " + ", end='')
        total = total + dico[letter.lower()]['val']
    print(' this value`')
    if len(mot) == 7:
        total += 50

    return total


def meilleur_mot(list_of_words, list_of_letters, dico):
    playable_words = mots_jouables(list_of_words, list_of_letters, extras=0)
    if len(playable_words) == 0:
        return ""
    else:
        max_value = -1
        max_value_word = ""
        for word in playable_words:
            current_value = valeur_mot(word, dico)
            if current_value > max_value:
                max_value = current_value
                max_value_word = word

        return max_value_word


def meilleurs_mots(list_of_words, list_of_letters, dico):
    playable_words = mots_jouables(list_of_words, list_of_letters, extras=0)
    if len(playable_words) == 0:
        return ""
    else:
        max_value = -1
        max_word = ""
        max_value_words = []
        for word in playable_words:
            current_value = valeur_mot(word, dico)
            if current_value > max_value:
                max_value = current_value
                max_word = word
        for word in playable_words:
            if valeur_mot(word, dico) == max_value:
                max_value_words.append(word)

        return max_value_words


def lire_coords(new_jetons_board):
    coordinate = input("Enter coordinates : ")
    is_bad_format = True
    list_of_coordinates = coordinate.split(' ')
    while is_bad_format:
        row = int(list_of_coordinates[0]) - 1
        column = int(list_of_coordinates[1]) - 1

        if row < 0 or row > 14 or column < 0 or column > 14:
            print('invalid coordinates')
            coordinate = input("Enter coordinates : ")
            list_of_coordinates = coordinate.split(' ')

        elif new_jetons_board[row][column][0] == ' ':
            is_bad_format = False
        else:
            print("that place is already filled")
            coordinate = input("Enter coordinates : ")
            list_of_coordinates = coordinate.split(' ')
    return list_of_coordinates


def tester_placement(jetons_board, row, column, direction, mot):
    '''
        returns the list of letters for the word; \n
        else returns [] \n
        row, column is position.
    '''
    list_of_letters = []
    rowIndex = row - 1
    columnIndex = column - 1
    if direction == "horizontal":
        if column + len(mot) > 14:
            print('outside boundaries')
            return []
        i = 0
        for cellIndex in range(columnIndex, columnIndex + len(mot)):
            if jetons_board[rowIndex][cellIndex][0] != 'j':
                list_of_letters.append(mot[i])
            i += 1
    elif direction == "vertical":
        if row + len(mot) > 14:
            print('outside boundaries')
            return []
        i = 0
        for cellIndex in range(rowIndex, rowIndex + len(mot)):
            if jetons_board[cellIndex][columnIndex][0] != 'j':
                list_of_letters.append(mot[i])
            i += 1
    return list_of_letters


def placer_mot(board, hand, mot, row, column, direction):
    """
        updates the hand and the board, removes the letters of the word from the hand; \n
        returns True; \n
        if not possible, nothing False \n
        row, column is position.
    """
    rowIndex = row - 1
    columnIndex = column - 1
    can_be_placed = tester_placement(
        board, row, column, direction, mot)

    if can_be_placed != []:
        if direction == "horizontal":
            for i in range(len(mot)):
                if board[rowIndex][columnIndex+i][0] != 'j':
                    board[rowIndex][columnIndex+i] = mot[i] + '  '
                    hand.remove(mot[i])

        if direction == "vertical":
            for i in range(len(mot)):
                if board[rowIndex+i][columnIndex][0] != 'j':
                    board[rowIndex+i][columnIndex] = mot[i] + '  '
                    hand.remove(mot[i])

        return True
    else:
        return False


def valeur_mot_better(direction, mot, letters_value_dico, bonuses_dico, row, column):
    """
        gets a bunch of arguments, and returns the value of the word\n
        adding all the bonuses of the table\n
        row/column are positons
    """
    multiplier = "1"
    rowIndex = row - 1
    columnIndex = column-1
    word_value = 0
    letterIndex = 0
    if direction == 'horizontal':  # -_-#
        for cell in range(columnIndex, columnIndex + len(mot)):
            if bonuses_dico[rowIndex][cell] == "MT":
                print("hitted a bonus, MT")
                multiplier = "3"
                word_value += letters_value_dico[mot[letterIndex].lower()
                                                 ]['val']
            elif bonuses_dico[rowIndex][cell] == "MD":
                print("hitted a bonus, MD")
                multiplier = "2"
                word_value += letters_value_dico[mot[letterIndex].lower()
                                                 ]['val']
            elif bonuses_dico[rowIndex][cell] == "LD":
                print("hitted a bonus, LD")
                word_value += letters_value_dico[mot[letterIndex].lower()
                                                 ]['val'] * 2
            elif bonuses_dico[rowIndex][cell] == "LT":
                print("hitted a bonus, LT")
                word_value += letters_value_dico[mot[letterIndex].lower()
                                                 ]['val'] * 3
            else:
                word_value += letters_value_dico[mot[letterIndex].lower()
                                                 ]['val']

            letterIndex += 1
    elif direction == 'vertical':
        for cell in range(rowIndex, rowIndex + len(mot)):
            if bonuses_dico[cell][columnIndex] == "MT":
                print("hitted a bonus, MT")
                multiplier = "3"
                word_value += letters_value_dico[mot[letterIndex].lower()
                                                 ]['val']
            elif bonuses_dico[cell][columnIndex] == "MD":
                print("hitted a bonus, MD")
                multiplier = "2"
                word_value += letters_value_dico[mot[letterIndex].lower()
                                                 ]['val']
            elif bonuses_dico[cell][columnIndex] == "LD":
                print("hitted a bonus, LD")
                word_value += letters_value_dico[mot[letterIndex].lower()
                                                 ]['val'] * 2
            elif bonuses_dico[cell][columnIndex] == "LT":
                print("hitted a bonus, LT")
                word_value += letters_value_dico[mot[letterIndex].lower()
                                                 ]['val'] * 3
            else:
                word_value += letters_value_dico[mot[letterIndex].lower()
                                                 ]['val']

            letterIndex += 1

    print("total: ", word_value)
    word_value = word_value * int(multiplier)
    print("total after the bonus: ", word_value)
