
import pygame
from functions import *

import types

cell_width = 50
cell_color_fill = cell_width - 5
red_color = [250, 0, 0]
light_blue_color = [100, 100, 255]
blue_color = [0, 0, 255]
yellow_color = [255, 255, 0]
green_color = [0, 255, 0]


def draw_starting_board(screen, bonus_board):
    """
        draws the cells, with their respective colors\n
        adds the name of the bonus above, if it has one \n
        and blits the cells
    """
    for rowIndex in range(len(bonus_board)):
        for cellIndex in range(len(bonus_board[0])):
            color = None
            font = pygame.font.SysFont(None, 24)
            if bonus_board[rowIndex][cellIndex] == "MT":
                color = red_color
                cell_name = "MT"
            elif bonus_board[rowIndex][cellIndex] == "MD":
                color = yellow_color
                cell_name = "MD"
            elif bonus_board[rowIndex][cellIndex] == "LD":
                color = light_blue_color
                cell_name = "LD"
            elif bonus_board[rowIndex][cellIndex] == "LT":
                color = blue_color
                cell_name = "LT"
            else:
                color = green_color
                cell_name = ""
            cell = pygame.Rect(cell_width * cellIndex,
                               cell_width * rowIndex, cell_color_fill, cell_color_fill)

            pygame.draw.rect(screen, color, cell)

            img = font.render(cell_name, True, [0, 0, 0])
            x = int(cell_width * cellIndex + cell_width / 5)
            y = int(cell_width * rowIndex + cell_width / 3)
            screen.blit(img, (x, y))


def update_board(screen, row, column, direction, mot):
    """
        draws the cells, with their respective colors\n
        adds the name of the bonus above, if it has one \n
        and blits the cells
    """
    i = 0
    length = len(mot)
    list_of_cells_to_be_updated = []
    for times in range(length):
        if direction == 'horizontal':
            list_of_cells_to_be_updated.append([row, column + times])
        if direction == 'vertical':
            list_of_cells_to_be_updated.append([row + times, column])

    for rowIndex in range(14):
        for cellIndex in range(14):
            if [rowIndex, cellIndex] in list_of_cells_to_be_updated:
                cell = pygame.Rect(cell_width * cellIndex,
                                   cell_width * rowIndex, cell_color_fill, cell_color_fill)

                pygame.draw.rect(screen, [255, 255, 255], cell)
                font = pygame.font.SysFont(None, 35)
                img = font.render(mot[i], True, [0, 0, 0])
                x = int(cell_width * cellIndex + cell_width / 5)
                y = int(cell_width * rowIndex + cell_width / 5)
                screen.blit(img, (x, y))
                i += 1


def draw_console(screen):
    """
        fills with black the current console
    """
    dimentions = pygame.Rect(750, 250, 400, 450)
    pygame.draw.rect(screen, [0, 0, 0], dimentions)


def draw_text(screen,  x, y, text, color, text_font, text_size):
    font = pygame.font.SysFont(text_font, text_size)
    text = font.render(text, True, color)
    screen.blit(text, (x, y))


def show_button(screen, x, y, button_width, button_height,  button_color, text_font, text, text_size, text_color):
    """
        just complete the arguments, it makes sense\n
        also blits the text
    """
    font = pygame.font.SysFont(text_font, text_size)
    text = font.render(text, True, text_color)
    pygame.draw.rect(screen, button_color, [x, y, button_width, button_height])
    screen.blit(text, (x + 5, y + button_height/3))


def handle_exit(events):
    """
        key_input handler\n
        return True or False\n
    """
    Playing = True
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                Playing = False
        elif event.type == pygame.QUIT:
            Playing = False
    return Playing


def draw_hand(screen, x, y, hand):
    translate = 20
    for letterIndex in range(len(hand)):
        draw_text(screen, x + translate*letterIndex, y,
                  hand[letterIndex], [255, 0, 0], 'Corbel', 30)


def draw_bullet_points(screen, x, y, theList):
    translate = 30
    for itemIndex in range(len(theList)):
        draw_text(screen, x, y + translate*itemIndex,
                  theList[itemIndex], [255, 0, 0], 'Corbel', 30)


def draw_buttons(screen, button_width, button_height, button_font):
    pygame.draw.rect(screen, [50, 50, 50], [750, 0, 350, 250])
    # ----------- BUTTON 2
    button2_x = 780
    button2_y = 20
    text_color = [0, 0, 0]
    show_button(screen, button2_x, button2_y, button_width,
                button_height, [100, 100, 100], button_font, 'Skip', 18, text_color)

    # ----------- BUTTON 3
    button3_x = 780
    button3_y = 90
    text_color = [0, 0, 0]
    show_button(screen, button3_x, button3_y, button_width,
                button_height, [100, 100, 100], button_font, 'Exchange', 18, text_color)

    # ----------- BUTTON 4
    button4_x = 780
    button4_y = 150
    text_color = [0, 0, 0]
    show_button(screen, button4_x, button4_y, button_width,
                button_height, [100, 100, 100], button_font, 'Place horizontal', 18, text_color)

    # ----------- BUTTON 5
    button5_x = 780
    button5_y = 200
    text_color = [0, 0, 0]
    show_button(screen, button5_x, button5_y, button_width,
                button_height, [100, 100, 100], button_font, 'Place vertical', 18, text_color)

    return [[button2_x, button2_y], [button3_x, button3_y], [button4_x, button4_y], [button5_x, button5_y]]


def player_console(screen, playerName, playerHand, playerScore, best_words):
    """
        takes the current player Name, and shows the current Players console
    """

    # name
    draw_text(screen, 760, 260, "Player Name: ", [255, 255, 255], "Corbel", 30)
    draw_text(screen, 950, 260, playerName, [255, 0, 0], "Corbel", 30)
    # hand
    draw_text(screen, 760, 360, "Player Hand: ", [255, 255, 255], "Corbel", 30)
    draw_hand(screen, 920, 360, playerHand)

    draw_text(screen, 760, 460, "Best Option: ",
              [255, 255, 255], "Corbel", 30)
    draw_bullet_points(screen, 920, 460, best_words)


def is_button_pressed(events, btn_x, btn_y, btn_width, btn_height):
    """
        if the user presses the button, return True
    """
    coords = pygame.mouse.get_pos()
    if coords[0] > btn_x and coords[0] < btn_x + btn_width \
            and coords[1] > btn_y and coords[1] < btn_y + btn_height:
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    return True
    return False


def get_cell_pressed(events):
    """
        returns the cellX_index and cellY_index, \n
        based on the position of the mouse
    """
    coords = pygame.mouse.get_pos()
    if coords[0] < 700:
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    print('coords: ', coords[0], coords[1])
                    cellX_index = (coords[0]+1) // 50
                    cellY_index = (coords[1]+1) // 50
                    print("returning: ", cellX_index, cellY_index)
                    return cellX_index, cellY_index
    return -1, -1
