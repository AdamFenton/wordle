import pygame as pg
import numpy as np
import sys
WIDTH,HEIGHT = (500,800)
PADLEFTRIGHT = 10
PADTOP = 10
PADBOTTOM = 240
BOX_WIDTH = (WIDTH - 2*(PADLEFTRIGHT))/5
BOX_HEIGHT = (HEIGHT -(PADBOTTOM+PADTOP))/6
KEYBOARD_PADDING = 5
KEY_WIDTH = 50
KEY_HEIGHT = 60
TB_HEIGHT, TB_WIDTH = (480,BOX_HEIGHT)
user_text = ''
pg.font.init()
myfont = pg.font.SysFont('Helvetica', 80)



WIN = pg.display.set_mode((WIDTH,HEIGHT))
BLACK = (0,0,0)
WHITE = (255,255,255)
def get_guess_letters_for_printing(guess_string):
    firstLetter = myfont.render(list(guess_string.upper())[0], False, (0, 0, 0))
    secondLetter = myfont.render(list(guess_string.upper())[1], False, (0, 0, 0))
    thirdLetter = myfont.render(list(guess_string.upper())[2], False, (0, 0, 0))
    fourthLetter = myfont.render(list(guess_string.upper())[3], False, (0, 0, 0))
    fifthLetter = myfont.render(list(guess_string.upper())[4], False, (0, 0, 0))
    return firstLetter, secondLetter, thirdLetter, fourthLetter, fifthLetter

def get_letter_positions(guess_count):
    first_position = ((PADLEFTRIGHT*3,((BOX_HEIGHT * guess_count) + PADTOP*2.5)))
    second_position = ((((BOX_WIDTH*1)+(PADLEFTRIGHT*3)),((BOX_HEIGHT * guess_count) + PADTOP*2.5)))
    third_position = ((((BOX_WIDTH*2)+(PADLEFTRIGHT*3)),((BOX_HEIGHT * guess_count) + PADTOP*2.5)))
    fourth_position = ((((BOX_WIDTH*3)+(PADLEFTRIGHT*3)),((BOX_HEIGHT * guess_count) + PADTOP*2.5)))
    fifth_position = ((((BOX_WIDTH*4)+(PADLEFTRIGHT*3)),((BOX_HEIGHT * guess_count) + PADTOP*2.5)))
    return first_position, second_position, third_position, fourth_position, fifth_position


def draw_window():
    WIN.fill(WHITE)
    play_counter = 1
    guess_count = 0
    for x in np.arange(PADLEFTRIGHT, (WIDTH-PADLEFTRIGHT), BOX_WIDTH):
        for y in np.arange(PADTOP, (HEIGHT-PADBOTTOM), BOX_HEIGHT):
            boxes = pg.Rect(x, y, BOX_WIDTH, BOX_HEIGHT)
            pg.draw.rect(WIN, BLACK, boxes,1)

    # pg.display.update()
def guess(guess_count,guess_string):

    letters = get_guess_letters_for_printing(guess_string)
    positions = get_letter_positions(guess_count)
    WIN.blit(letters[0],positions[0])
    WIN.blit(letters[1],positions[1])
    WIN.blit(letters[2],positions[2])
    WIN.blit(letters[3],positions[3])
    WIN.blit(letters[4],positions[4])

def test_function(guess_count,text):
    letters = get_guess_letters_for_printing(text)
    positions = get_letter_positions(guess_count)
    WIN.blit(letters[0],positions[0])

    if guess_count > 5:
        sys.exit()
    print(guess_count)





def main():
    font = pg.font.Font(None, 119)
    clock = pg.time.Clock()
    input_box = pg.Rect(PADLEFTRIGHT, (BOX_HEIGHT * 6) + (2* PADTOP), (WIDTH-PADLEFTRIGHT), BOX_HEIGHT)

    # input_box = pg.Rect(PADLEFTRIGHT,(BOX_HEIGHT),50000,BOX_HEIGHT)
    color_inactive = pg.Color(BLACK)
    color_active = pg.Color(BLACK)
    color = color_inactive
    active = False
    text = ''
    done = False
    guess_count = 0

    game_running = True
    while game_running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                game_running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
            if event.type == pg.KEYDOWN:
                if active:
                    if event.key == pg.K_RETURN:
                        guess_count += 1
                        test_function(guess_count,text)
                        
                        text = ''
                    elif event.key == pg.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
        draw_window()
        # Render the current text.
        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(480, txt_surface.get_width()+10)
        input_box.w = width
        # Blit the text.
        WIN.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Blit the input_box rect.
        pg.draw.rect(WIN, color, input_box, 2)

        pg.display.flip()
        clock.tick(30)





if __name__ == "__main__":
    main()
