
import pygame
import os
from screen_helpers import *
from input import TextInput
pygame.init()
pygame.display.set_caption("Scrabble")
os.environ['SDL_VIDEO_CENTERED'] = '1'
width = 1100
height = 750
screen = pygame.display.set_mode((width, height))
screen.fill((69, 72, 74))


board_list = init_jeton()
bonus_board = init_bonus_board()
# drawing parts
draw_starting_board(screen, bonus_board)

button_width = 130
button_height = 40
button_font = "Arial"
buttons_cords = draw_buttons(screen, button_width, button_height, button_font)
button2_x, button2_y = buttons_cords[0][0], buttons_cords[0][1]
button3_x, button3_y = buttons_cords[1][0], buttons_cords[1][1]
button4_x, button4_y = buttons_cords[2][0], buttons_cords[2][1]
button5_x, button5_y = buttons_cords[3][0], buttons_cords[3][1]
# drawing parts

pygame.display.flip()

# player variable
letters_dictionary = letters_dico()
list_of_all_possible_words = generer_dico('data/littre.txt')
sac = init_sac(letters_dictionary)

players_dico = {}
player1 = "Farah"
player2 = "Ronald"
hand1 = piocher(7, sac)
hand2 = piocher(7, sac)
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
        doesn't flip the screen
    """
    playerName = ''
    available_words = []
    if turn % 2 == 0:
        playerName = player1
        available_words = mots_jouables(
            list_of_all_possible_words, players_dico[playerName]['hand'], 0)
        best_words = meilleurs_mots(
            available_words, players_dico[playerName]['hand'], letters_dictionary)
        player_console(
            screen, playerName, players_dico[playerName]['hand'], players_dico[playerName]['score'], best_words)

    else:
        playerName = player2
        available_words = mots_jouables(
            list_of_all_possible_words, players_dico[playerName]['hand'], 0)
        best_words = meilleurs_mots(
            available_words, players_dico[playerName]['hand'], letters_dictionary)
        player_console(
            screen, playerName, players_dico[playerName]['hand'], players_dico[playerName]['score'], best_words)
    return playerName, available_words


playerName = generate_console()[0]
Playing = True
last_turn = False
userInput = ''
is_console_generated = False
waiting_cell = "None"
while Playing:
    events = pygame.event.get()
    Playing = handle_exit(events)

    # generate the console for the new player
    if is_console_generated == False:
        draw_console(screen)
        playerName, available_words = generate_console()
        is_console_generated = True

    # get out of the main game loop
    if not Playing:
        break

    if waiting_cell[0:4] == "True":
        direction = waiting_cell[5:]
        # all_possible_words =
        available_words = mots_jouables(
            list_of_all_possible_words, players_dico[playerName]['hand'], 0)

        cellX_index, cellY_index = get_cell_pressed(events)
        if cellX_index != -1 and cellY_index != -1:
            waiting_cell = "False"
        if waiting_cell == "False":
            column = cellX_index+1
            row = cellY_index+1

            if direction == 'Horizontal':
                is_placed = placer_mot_screen(
                    board_list, players_dico[playerName]['hand'], userInput, row, column, 'horizontal')

                if isinstance(is_placed, bool):

                    update_board(screen, row, column,
                                 'horizontal', userInput)
                    is_console_generated = False
                    user_word_value = valeur_mot_better("horizontal", userInput,
                                                        letters_dictionary, bonus_board, row, column)
                    players_dico[playerName]['score'] += user_word_value
                else:
                    draw_console(screen)
                    generate_console()
                    turn -= 1
                    draw_text(screen, 770, 600, is_placed, [
                        255, 255, 255], 'Arial', 30)

            else:
                is_placed = placer_mot_screen(
                    board_list, players_dico[playerName]['hand'], userInput, row, column, 'vertical')
                if isinstance(is_placed, bool):
                    update_board(screen, row, column,
                                 'vertical', userInput)
                    is_console_generated = False
                    user_word_value = valeur_mot_better("vertical", userInput,
                                                        letters_dictionary, bonus_board, row, column)
                    players_dico[playerName]['score'] += user_word_value
                else:
                    draw_console(screen)
                    generate_console()
                    turn -= 1
                    draw_text(screen, 770, 600, is_placed, [
                        255, 255, 255], 'Arial', 30)
            if(last_turn):
                break
            players_dico[playerName]['hand'] = completer_main(
                players_dico[playerName]['hand'], sac)

            textinput.input_string = ''
            turn += 1

    pygame.display.flip()
    # skip
    if is_button_pressed(events, button2_x, button2_y, button_width, button_height):
        if(last_turn):
            break
        turn += 1
        is_console_generated = False
        textinput.input_string = ''
    # exchange
    elif is_button_pressed(events, button3_x, button3_y, button_width, button_height):
        if(last_turn):
            break
        textinput.input_string = ''
        if userInput != '':
            selected_jetons = list(userInput)
            updated_hand, sac, did_exchange = echanger(
                selected_jetons, players_dico[playerName]['hand'], sac)
            players_dico[playerName]['hand'] = updated_hand
        if did_exchange:
            is_console_generated = False
            turn += 1
        else:
            draw_console(screen)
            generate_console()
            draw_text(screen, 800, 600, "Can't exchange hand", [
                      255, 255, 255], 'Arial', 30)

    # placement horizontal
    elif is_button_pressed(events, button4_x, button4_y, button_width, button_height):
        if userInput not in available_words:
            draw_console(screen)
            generate_console()
            draw_text(screen, 800, 600, "Word does not exist", [
                      255, 255, 255], 'Arial', 30)
            draw_text(screen, 800, 640, "Try to enter again", [
                      255, 255, 255], 'Arial', 30)
        else:
            waiting_cell = "True Horizontal"
            is_console_generated = False
            draw_text(screen, 800, 600, "Place horizontal word", [
                      255, 255, 255], 'Arial', 30)
            pygame.display.flip()
    # placement vertical
    elif is_button_pressed(events, button5_x, button5_y, button_width, button_height):
        if userInput not in available_words:
            draw_console(screen)
            generate_console()
            draw_text(screen, 800, 600, "Word does not exist", [
                      255, 255, 255], 'Arial', 30)
            draw_text(screen, 800, 640, "Try to enter again", [
                      255, 255, 255], 'Arial', 30)
        else:
            waiting_cell = "True Vertical"
            is_console_generated = False
            draw_text(screen, 800, 600, "Place vertical word", [
                      255, 255, 255], 'Arial', 30)
            pygame.display.flip()

    userInput = textinput.get_text().upper()
    textinput.update(events)

    draw_buttons(screen, button_width, button_height, button_font)
    screen.blit(textinput.get_surface(), (920, 130))

    if len(sac) == 0:
        pl1_hand = players_dico[player1]['hand']
        pl2_hand = players_dico[player2]['hand']
        p1_damage = remove_hand_points(pl1_hand, letters_dictionary)
        p2_damage = remove_hand_points(pl2_hand, letters_dictionary)
        players_dico[player1]['score'] -= p1_damage
        players_dico[player2]['score'] -= p2_damage
        last_turn = True


pygame.draw.rect(screen, [0, 0, 0], [750, 0, 350, 750])
draw_text(screen, 760, 360, f"{player1} Score: ",
          [255, 255, 255], "Arial", 30)
draw_hand(screen, 920, 360, str(players_dico[player1]['score']))
draw_text(screen, 760, 560, f"{player2} Score: ",
          [255, 255, 255], "Arial", 30)
draw_hand(screen, 920, 560, str(players_dico[player2]['score']))
pygame.display.flip()
ending = True
while ending:  # untill the game is closed
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                ending = False
        elif event.type == pygame.QUIT:
            ending = False
