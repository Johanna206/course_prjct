# used for creating game
import pygame
from pygame.locals import *
# copy all the functions i wrote from soitaire.py into display thing
from solitaire import *

# Initialize a window or screen for display with captions 
pygame.init()
surface = pygame.display.set_mode((1300, 800))
pygame.display.set_caption('Tarot Solitaire Game')
black = (0,0,0)
white = (255,255,255)

# Draw rectangles for each empty card pile
# card image dimensions
width_height = (200, 333)
# card pile locations
xy_draw = (50, 433)
draw_rec = pygame.Rect(xy_draw, width_height)
xy_t1 = (50, 50)
t1_rec = pygame.Rect(xy_t1, width_height)
pygame.draw.rect(surface, white, t1_rec, 2)
xy_t2 = (300,50)
t2_rec = pygame.Rect(xy_t2, width_height)
pygame.draw.rect(surface, white, t2_rec, 2)
xy_t3 = (550,50)
t3_rec = pygame.Rect(xy_t3, width_height)
pygame.draw.rect(surface, white, t3_rec, 2)
xy_t4 = (800,50)
t4_rec = pygame.Rect(xy_t4, width_height)
pygame.draw.rect(surface, white, t4_rec, 2)
xy_t5 = (1050,50)
t5_rec = pygame.Rect(xy_t5, width_height)
pygame.draw.rect(surface, white, t5_rec, 2)
xy_discard = (1050,433)
dis_rec = pygame.Rect(xy_discard, width_height)
pygame.draw.rect(surface, white, dis_rec, 2)

# Draw text and back of draw pile
back = pygame.image.load('processed/back.jpg')
surface.blit(back, xy_draw)
font = pygame.font.Font('font/AlexBrush-Regular.ttf', 32)
txt_draw = font.render('<- Click to Draw', True, white, black)
surface.blit(txt_draw, (270, 575))
score = 0
txt_score = font.render(str(score), True, white, black)
surface.blit(txt_score, (860, 555))
txt_discarded = font.render('Cards Discarded  ->', True, white, black)
surface.blit(txt_discarded, (800, 595))

# display the depths of each tableau card piles, written above each pile
font2 = pygame.font.Font('font/FiraSans-Bold.otf', 18)
d1_xy = (146, 15)
d2_xy = (396, 15)
d3_xy = (646, 15)
d4_xy = (896, 15)
d5_xy = (1146, 15)
pygame.display.flip()

def display_update():
    ''' draw updated game '''
    # update score
    msg = ''
    score = get_score()
    txt_score = font.render(str(score), True, white, black)
    pygame.draw.rect(surface, black, (860, 555, 60, 40))
    surface.blit(txt_score, (860, 555))
    # update draw pile
    if len(draw) == 0:
        pygame.draw.rect(surface, black, draw_rec)
        pygame.draw.rect(surface, white, draw_rec, 2)
    else:
        surface.blit(back, xy_draw)
    # update discard pile
    if len(discard) == 0:
        pygame.draw.rect(surface, black, dis_rec)
        pygame.draw.rect(surface, white, dis_rec, 2)
    else:
        surface.blit(back, xy_discard)
    # update t1
    if len(t1) == 0:
        pygame.draw.rect(surface, black, t1_rec)
        pygame.draw.rect(surface, white, t1_rec, 2)
    else:
        file = deck[t1[0]]['Image File']
        a = pygame.image.load('processed/'+file)
        surface.blit(a, xy_t1)
    # update t2
    if len(t2) == 0:
        pygame.draw.rect(surface, black, t2_rec)
        pygame.draw.rect(surface, white, t2_rec, 2)
    else:
        file = deck[t2[0]]['Image File']
        a = pygame.image.load('processed/'+file)
        surface.blit(a, xy_t2)
    # update t3
    if len(t3) == 0:
        pygame.draw.rect(surface, black, t3_rec)
        pygame.draw.rect(surface, white, t3_rec, 2)
    else:
        file = deck[t3[0]]['Image File']
        a = pygame.image.load('processed/'+file)
        surface.blit(a, xy_t3)
    # update t4
    if len(t4) == 0:
        pygame.draw.rect(surface, black, t4_rec)
        pygame.draw.rect(surface, white, t4_rec, 2)
    else:
        file = deck[t4[0]]['Image File']
        a = pygame.image.load('processed/'+file)
        surface.blit(a, xy_t4)
    # upate t5
    if len(t5) == 0:
        pygame.draw.rect(surface, black, t5_rec)
        pygame.draw.rect(surface, white, t5_rec, 2)
    else:
        file = deck[t5[0]]['Image File']
        a = pygame.image.load('processed/'+file)
        surface.blit(a, xy_t5)
    # update pile depths
    d1 = font2.render(str(len(t1)), True, white, black)
    pygame.draw.rect(surface, black, pygame.Rect((d1_xy), (20, 20)))
    surface.blit(d1, d1_xy)
    d2 = font2.render(str(len(t2)), True, white, black)
    pygame.draw.rect(surface, black, pygame.Rect((d2_xy), (20, 20)))
    surface.blit(d2, d2_xy)    
    d3 = font2.render(str(len(t3)), True, white, black)
    pygame.draw.rect(surface, black, pygame.Rect((d3_xy), (20, 20)))
    surface.blit(d3, d3_xy)
    d4 = font2.render(str(len(t4)), True, white, black)
    pygame.draw.rect(surface, black, pygame.Rect((d4_xy), (20, 20)))
    surface.blit(d4, d4_xy)
    d5 = font2.render(str(len(t5)), True, white, black)
    pygame.draw.rect(surface, black, pygame.Rect((d5_xy), (20, 20)))
    surface.blit(d5, d5_xy)

    # udpate display for troubleshooting
    if game_won():
        msg = 'Congratulations, you won!!'
    if game_still_going():
        msg = f'You lost but you got {score} points!'
    msg_txt = font.render(msg, True, white, black)
    surface.blit(msg_txt, (510, 700))
    pygame.display.flip()
    # print('card piles \n', t1, '\n', t2, '\n', t3, '\n', t4, '\n', t5)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            # click on Draw a card
            if draw_rec.collidepoint(x, y) and len(draw) > 0:
                deal()
                display_update()
            # click on t1 to discard
            if t1_rec.collidepoint(x, y) and can_discard(t1):
                mv_discard(t1)
                display_update()
                break
            # click on t2 to discard 
            if t2_rec.collidepoint(x, y) and can_discard(t2):
                mv_discard(t2)
                display_update()
                break
            # click on t3 to discard
            if t3_rec.collidepoint(x, y) and can_discard(t3):
                mv_discard(t3)
                display_update()
                break
            # click on t4 to discard
            if t4_rec.collidepoint(x, y) and can_discard(t4):
                mv_discard(t4)
                display_update()
                break
            # click on t5 to discard
            if t5_rec.collidepoint(x, y) and can_discard(t5):
                mv_discard(t5)
                display_update()
                break
            # click on t1 to move
            if t1_rec.collidepoint(x, y) and (len(t1) > 0):
                mv_empty(t1)
                display_update()
                break
            # click on t2 to move
            if t2_rec.collidepoint(x, y) and (len(t2) > 0):
                mv_empty(t2)
                display_update()
                break
            # click on t3 to move
            if t3_rec.collidepoint(x, y) and (len(t3) > 0):
                mv_empty(t3)
                display_update()
                break
            # click on t4 to move
            if t4_rec.collidepoint(x, y) and (len(t4) > 0):
                mv_empty(t4)
                display_update()
                break
            # click on t5 to move
            if t5_rec.collidepoint(x, y) and (len(t5) > 0):
                mv_empty(t5)
                display_update()
                break
            


