
import pygame
import os
from screen_helpers import *
from input import TextInput
pygame.init()
pygame.display.set_caption("Scrabble")
os.environ['SDL_VIDEO_CENTERED'] = '1'
width = 1100
height = 700
screen = pygame.display.set_mode((width, height))
screen.fill((50, 50, 50))


board_list = init_jeton()
bonus_board = init_bonus_board()
# drawing parts
draw_starting_board(screen, bonus_board)

button_width = 130
button_height = 40
button_font = "Corbel"
buttons_cords = draw_buttons(screen, button_width, button_height, button_font)
button2_x, button2_y = buttons_cords[0][0], buttons_cords[0][1]
button3_x, button3_y = buttons_cords[1][0], buttons_cords[1][1]
button4_x, button4_y = buttons_cords[2][0], buttons_cords[2][1]
button5_x, button5_y = buttons_cords[3][0], buttons_cords[3][1]
# drawing parts

pygame.display.flip()

# player variable
letters_dictionary = letters_dico()
list_of_all_possible_words = generer_dico('documents/littre.txt')
sac = init_sac(letters_dictionary)

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
players_dico[player2] = {}
players_dico[player2]['hand'] = hand2
players_dico[player2]['score'] = score2

turn = 1
textinput = TextInput(text_color=(255, 255, 255), cursor_color=(255, 255, 255))


def generate_console():
    """
        returns the current_turn playerName, and available words of the current_player\n
    """
    playerName = ''
    available_words = []
    if turn % 2 == 0:
        playerName = player1
        available_words = mots_jouables(
            list_of_all_possible_words, players_dico[playerName]['hand'], 0)
        if available_words == []:
            print("You cannot make a word with the avalable letters")
            # do something
        best_words = meilleurs_mots(
            available_words, players_dico[playerName]['hand'], letters_dictionary)
        player_console(
            screen, playerName, players_dico[playerName]['hand'], players_dico[playerName]['score'], best_words)

    else:
        playerName = player2
        available_words = mots_jouables(
            list_of_all_possible_words, players_dico[playerName]['hand'], 0)
        if available_words == []:
            print("You cannot make a word with the avalable letters")
            # do something
        best_words = meilleurs_mots(
            available_words, players_dico[playerName]['hand'], letters_dictionary)
        player_console(
            screen, playerName, players_dico[playerName]['hand'], players_dico[playerName]['score'], best_words)
    return playerName, available_words


generate_console()
Playing = True
userInput = ''
playerName = ''
is_console_generated = False
waiting_cell = "None"
while Playing:
    events = pygame.event.get()
    Playing = handle_exit(events)
    if is_console_generated == False:
        print('console generated')
        draw_console(screen)
        current_player_name, available_words = generate_console()
        is_console_generated = True

    if not Playing:
        break

    if waiting_cell[0:4] == "True":
        direction = waiting_cell[5:]
        print(direction)
        cellX_index, cellY_index = get_cell_pressed(events)
        if cellX_index != -1 and cellY_index != -1:
            waiting_cell = "False"
        if waiting_cell == "False":
            if direction == 'Horizontal':
                is_placed = placer_mot(
                    board_list, players_dico[playerName]['hand'], userInput, cellY_index+1, cellX_index +
                    1, 'horizontal')
                update_board(screen, cellY_index, cellX_index,
                             'horizontal', userInput)
            else:
                is_placed = placer_mot(
                    board_list, players_dico[playerName]['hand'], userInput, cellY_index+1, cellX_index +
                    1, 'vertical')
                update_board(screen, cellY_index, cellX_index,
                             'vertical', userInput)
            print_list(board_list)

            textinput.input_string = ''
            is_console_generated = False
            turn += 1

    pygame.display.flip()
    # skip
    if is_button_pressed(events, button2_x, button2_y, button_width, button_height):
        turn += 1
        is_console_generated = False
        textinput.input_string = ''
    # exchange
    elif is_button_pressed(events, button3_x, button3_y, button_width, button_height):

        is_console_generated = False

        textinput.input_string = ''
        playerName, _ = generate_console()
        if userInput != '':
            selected_jetons = list(userInput)
            updated_hand = echanger(
                selected_jetons, players_dico[playerName]['hand'], sac)[0]
            players_dico[playerName]['hand'] = updated_hand
        turn += 1
    # placement horizontal
    elif is_button_pressed(events, button4_x, button4_y, button_width, button_height):
        # is_console_generated = False
        playerName, available_words = generate_console()
        if userInput not in available_words:
            print("Word does not exist, try to enter again")
            turn -= 1
        else:
            print("your word is correct")

        waiting_cell = "True Horizontal"

    # placement vertical
    elif is_button_pressed(events, button5_x, button5_y, button_width, button_height):
        # is_console_generated = False
        playerName, available_words = generate_console()
        if userInput not in available_words:
            print("Word does not exist, try to enter again")
            turn -= 1
        else:
            print("your word is correct")

        waiting_cell = "True Vertical"
    userInput = textinput.get_text()
    textinput.update(events)

    draw_buttons(screen, button_width, button_height, button_font)
    screen.blit(textinput.get_surface(), (920, 130))
