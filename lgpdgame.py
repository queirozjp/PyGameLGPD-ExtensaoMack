import pygame
import time

pygame.init()

screen = pygame.display.set_mode((500,800))
clock = pygame.time.Clock()
background = pygame.image.load("Images\menubackground.png").convert()
background = pygame.transform.scale(background,
                                    (background.get_width() * 0.27901,
                                     background.get_height() * 0.3125))
startbutton = pygame.image.load("Images\start.png").convert()
startbutton = pygame.transform.scale(startbutton,
                                    (startbutton.get_width() / 8,
                                     startbutton.get_height() / 8))
startan = pygame.image.load("Images\startan.png").convert()
startan = pygame.transform.scale(startan,
                                    (startan.get_width() / 8,
                                     startan.get_height() / 8))
game = pygame.image.load("Images\gameplay.png").convert()
game = pygame.transform.scale(game,
                                    (game.get_width() * 0.697350,
                                     game.get_height() * 0.78125))
player1 = pygame.image.load("Images\player.png").convert_alpha()
player1 = pygame.transform.scale(player1,
                                    (player1.get_width() / 3,
                                     player1.get_height() / 3))
player2 = pygame.image.load("Images\player2.png").convert_alpha()
player2 = pygame.transform.scale(player2,
                                    (player2.get_width() / 3,
                                     player2.get_height() / 3))
text1 = pygame.image.load("Images\\text1.png").convert_alpha()
text1 = pygame.transform.scale(text1,
                                    (text1.get_width() / 4.5,
                                     text1.get_height() / 4.5))

frames = [player1, player2]

start_button_animation = 150
vel_an = 200
dur_an = 12000

button_rect = pygame.Rect(145, 668, 210, 86)


current_frame = 0
running = True
started = False
last_timer = pygame.time.get_ticks()
while running:
    clicked = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if button_rect.collidepoint(event.pos):
                started = True
                clicked = True
                timer = pygame.time.get_ticks()
                animating = True
                start_animation = pygame.time.get_ticks()
    screen.blit(background, (0,0))
    screen.blit(startbutton, (130,650))
    current_time = pygame.time.get_ticks()
    if clicked and current_time - timer > start_button_animation:
        clicked = False
    if clicked:
        screen.blit(startan, (130,650))
    elif started:
        screen.blit(game, (0,0)) 
        if animating:
            current_time = pygame.time.get_ticks()
            if current_time - last_timer > vel_an:
                current_frame = (current_frame + 1) % len(frames)
                last_timer = current_time
            if current_time - start_animation > dur_an:
                animating = False
            screen.blit(frames[current_frame], (20,160))
            screen.blit(text1, (150,60))
        else:
            screen.blit(text1, (150,60))
            screen.blit(player2, (20,160))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
