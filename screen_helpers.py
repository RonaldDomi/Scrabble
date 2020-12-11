
import pygame

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


def draw_console(screen):
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


def handle_exit():
    """
        key_input handler\n
        return True or False\n
    """
    Playing = True
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                Playing = False
        elif event.type == pygame.QUIT:
            Playing = False
    return Playing


def is_button_pressed(btn_x, btn_y, btn_width, btn_height):
    """
        if the user presses the button, return True
    """

    coords = pygame.mouse.get_pos()

    if coords[0] > btn_x and coords[0] < btn_x + btn_width \
            and coords[1] > btn_y and coords[1] < btn_y + btn_height:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    return True
    return False
