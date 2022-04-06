import pygame
import numpy as np
import sys
import pygame_vkeyboard as vkboard
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


WIN = pygame.display.set_mode((WIDTH,HEIGHT))
BLACK = (0,0,0)
WHITE = (255,255,255)
input_rect = pygame.Rect(PADLEFTRIGHT,(BOX_HEIGHT*6)+PADTOP,WIDTH-20,(BOX_HEIGHT)+PADTOP)
colour = pygame.Color('lightskyblue3')

pygame.font.init()
myfont = pygame.font.SysFont('Helvetica', 80)
clock = pygame.time.Clock()



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




def guess(guess_count):
    guess_string = 'tests'
    letters = get_guess_letters_for_printing(guess_string)
    positions = get_letter_positions(guess_count)
    WIN.blit(letters[0],positions[0])
    WIN.blit(letters[1],positions[1])
    WIN.blit(letters[2],positions[2])
    WIN.blit(letters[3],positions[3])
    WIN.blit(letters[4],positions[4])



    # pygame.display.update()


def draw_window():
    WIN.fill(WHITE)
    play_counter = 1
    guess_count = 0
    for x in np.arange(PADLEFTRIGHT, (WIDTH-PADLEFTRIGHT), BOX_WIDTH):
        for y in np.arange(PADTOP, (HEIGHT-PADBOTTOM), BOX_HEIGHT):
            boxes = pygame.Rect(x, y, BOX_WIDTH, BOX_HEIGHT)
            pygame.draw.rect(WIN, BLACK, boxes,1)


    # pygame.draw.rect(WIN,colour,input_rect,5)
    #
    # text_surface = myfont.render(user_text,True,(255,255,255))
    #
    # WIN.blit(text_surface,(input_rect.x + 5,input_rect.y + 5))

    pygame.display.update()
    # while play_counter < 6:
    #     pygame.display.update()
    #     if play_counter == 6:
    #         pygame.quit()

    while guess_count < 6:
        # pygame.display.update()
        guess(guess_count)
        guess_count += 1
        pygame.display.update()
    pygame.quit()


    pygame.quit()

def main():
    game_running = True
    while game_running:
        for event in pygame.event.get():
            draw_window()
            if event.type == pygame.QUIT:
                game_running = False
                pygame.quit()

            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_BACKSPACE:
            #         user_text = user_text[:-1]
            #     else:
            #          user_text += event.unicode
            #          if event.key == pygame.K_RETURN:
            #             print_word(user_text)
            #             user_text = ''



        # pygame.draw.rect(WIN,colour,input_rect,5)
        # text_surface = myfont.render(user_text,True,(255,255,255))
        #
        # WIN.blit(text_surface,(input_rect.x + 5,input_rect.y + 5))
        # pygame.display.update()

        # pygame.display.flip()
            clock.tick(60)

if __name__ == "__main__":
    main()


# stop
#
# # firstLetter = myfont.render(list(string.upper())[0], False, (0, 0, 0))
# # secondLetter = myfont.render(list(string.upper())[1], False, (0, 0, 0))
# # thirdLetter = myfont.render(list(string.upper())[2], False, (0, 0, 0))
# # fourthLetter = myfont.render(list(string.upper())[3], False, (0, 0, 0))
# # fifthLetter = myfont.render(list(string.upper())[4], False, (0, 0, 0))
# position_array = np.zeros(shape=(6,5))
# first_position_list=[]
# second_position_list=[]
# third_position_list=[]
# fourth_position_list=[]
# fifth_position_list=[]
# for guess_no in range(0,6):
#     first_position_list.append((PADLEFTRIGHT*3,((BOX_HEIGHT * guess_no) + PADTOP*2.5)))
#     second_position_list.append((((BOX_WIDTH*1)+(PADLEFTRIGHT*3)),((BOX_HEIGHT * guess_no) + PADTOP*2.5)))
#     third_position_list.append((((BOX_WIDTH*2)+(PADLEFTRIGHT*3)),((BOX_HEIGHT * guess_no) + PADTOP*2.5)))
#     fourth_position_list.append((((BOX_WIDTH*3)+(PADLEFTRIGHT*3)),((BOX_HEIGHT * guess_no) + PADTOP*2.5)))
#     fifth_position_list.append((((BOX_WIDTH*4)+(PADLEFTRIGHT*3)),((BOX_HEIGHT * guess_no) + PADTOP*2.5)))
#
#
# def draw_window():
#     WIN.fill(WHITE)
#
#     for x in np.arange(PADLEFTRIGHT, (WIDTH-PADLEFTRIGHT), BOX_WIDTH):
#         for y in np.arange(PADTOP, (HEIGHT-PADBOTTOM), BOX_HEIGHT):
#             boxes = pygame.Rect(x, y, BOX_WIDTH, BOX_HEIGHT)
#             pygame.draw.rect(WIN, BLACK, boxes,1)
#
#
#     for guess in range(0,6):
#         WIN.blit(firstLetter,first_position_list[guess])
#         WIN.blit(secondLetter,second_position_list[guess])
#         WIN.blit(thirdLetter,third_position_list[guess])
#         WIN.blit(fourthLetter,fourth_position_list[guess])
#         WIN.blit(fifthLetter,fifth_position_list[guess])
#
#
#
#
# def main():
#     game_running = True
#     while game_running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 game_running = False
#
#         draw_window()
#     pygame.quit()
#
# if __name__ == "__main__":
#     main()
