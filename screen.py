
import pygame
import os
from game import bonus_board
from screen_helpers import *
pygame.init()
pygame.display.set_caption("Scrabble")
os.environ['SDL_VIDEO_CENTERED'] = '1'
width = 1100
height = 700
screen = pygame.display.set_mode((width, height))
screen.fill((50, 50, 50))

draw_starting_board(screen, bonus_board)
draw_console(screen)
draw_text(screen, 760, 260, 'CONSOLE', [255, 255, 255], 'Corbel', 26)
draw_text(screen, 760, 360, 'CONSOLE', [255, 255, 255], 'Corbel', 26)
draw_text(screen, 760, 460, 'CONSOLE', [255, 255, 255], 'Corbel', 26)
# draw_text(x, y, text, color, text_font, size)
# 750, 250, 400, 450

button_width = 130
button_height = 40
button_font = "Corbel"
# ----------- BUTTON 1
button1_x = 780
button1_y = 10
text_color = [0, 0, 0]
show_button(screen, button1_x, button1_y, button_width,
            button_height, [100, 100, 100], button_font, 'hello guys', 18, text_color)

# ----------- BUTTON 2
button2_x = 780
button2_y = 70
text_color = [0, 0, 0]
show_button(screen, button2_x, button2_y, button_width,
            button_height, [100, 100, 100], button_font, 'Skip', 18, text_color)

# ----------- BUTTON 3
button3_x = 780
button3_y = 130
text_color = [0, 0, 0]
show_button(screen, button3_x, button3_y, button_width,
            button_height, [100, 100, 100], button_font, 'Exchange', 18, text_color)

# ----------- BUTTON 3
button4_x = 780
button4_y = 190
text_color = [0, 0, 0]
show_button(screen, button4_x, button4_y, button_width,
            button_height, [100, 100, 100], button_font, 'Place', 18, text_color)

pygame.display.flip()


Playing = True
while Playing:
    Playing = handle_exit()
    if not Playing:
        break
    if is_button_pressed(button1_x, button1_y, button_width, button_height):
        print("don't touch me, ")
