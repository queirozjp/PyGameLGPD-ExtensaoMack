import pygame
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
story1 = pygame.image.load("Images\story1.png").convert()
story1 = pygame.transform.scale(story1,
                                    (story1.get_width() * 0.697350,
                                     story1.get_height() * 0.78125))
story2 = pygame.image.load("Images\story2.png").convert()
story2 = pygame.transform.scale(story2,
                                    (story2.get_width() * 0.697350,
                                     story2.get_height() * 0.78125))
decision1 = pygame.image.load("Images\game1.png").convert()
decision1 = pygame.transform.scale(decision1,
                                    (decision1.get_width() * 0.697350,
                                     decision1.get_height() * 0.78125))
decision2 = pygame.image.load("Images\game2.png").convert()
decision2 = pygame.transform.scale(decision2,
                                    (decision2.get_width() * 0.697350,
                                     decision2.get_height() * 0.78125))
decision3 = pygame.image.load("Images\game3.png").convert()
decision3 = pygame.transform.scale(decision3,
                                    (decision3.get_width() * 0.697350,
                                     decision3.get_height() * 0.78125))
decision4 = pygame.image.load("Images\game4.png").convert()
decision4 = pygame.transform.scale(decision4,
                                    (decision4.get_width() * 0.697350,
                                     decision4.get_height() * 0.78125))
decision5 = pygame.image.load("Images\game5.png").convert()
decision5 = pygame.transform.scale(decision5,
                                    (decision5.get_width() * 0.697350,
                                     decision5.get_height() * 0.78125))
decision6 = pygame.image.load("Images\game6.png").convert()
decision6 = pygame.transform.scale(decision6,
                                    (decision6.get_width() * 0.697350,
                                     decision6.get_height() * 0.78125))
decision7 = pygame.image.load("Images\game7.png").convert()
decision7 = pygame.transform.scale(decision7,
                                    (decision7.get_width() * 0.697350,
                                     decision7.get_height() * 0.78125))
decision8 = pygame.image.load("Images\game8.png").convert()
decision8 = pygame.transform.scale(decision8,
                                    (decision8.get_width() * 0.697350,
                                     decision8.get_height() * 0.78125))
decision9 = pygame.image.load("Images\game9.png").convert()
decision9 = pygame.transform.scale(decision9,
                                    (decision9.get_width() * 0.697350,
                                     decision9.get_height() * 0.78125))
decision10 = pygame.image.load("Images\game10.png").convert()
decision10 = pygame.transform.scale(decision10,
                                    (decision10.get_width() * 0.697350,
                                     decision10.get_height() * 0.78125))
# -------- Historia ---------
stories = [story1, story2]

# -------- Decisões ---------
decisions = [decision1, decision2, decision3, decision4, decision5, decision6, decision7, decision8, decision9, decision10]

# -------- Botões ---------
startAnimation = 200
startTimer = pygame.time.get_ticks()
buttonRect = pygame.Rect(145, 668, 210, 86)
continueRect = pygame.Rect(290, 700, 180, 86)

# -------- Animação do Personagem ---------
anSpeed = 300
anDur = 2000
frames = [player1, player2]
currentFrame = 0
chrtTimer = pygame.time.get_ticks()


running = True
started = False
clicked = False
animating = False

def buttonAnimation(currentTime, timer, start):
    if clicked and currentTime - timer > start:
            return False
    

def characterAnimation(startAn, anDur, anSpeed, chrtTimer, currentFrame, animating):
    currentTime = pygame.time.get_ticks()
    if currentTime - chrtTimer > anSpeed:
        currentFrame = (currentFrame + 1) % len(frames)
        chrtTimer = currentTime
    if currentTime - startAn > anDur:
        animating = False
    screen.blit(frames[currentFrame], (20,160))     
    return currentFrame, chrtTimer, animating 
    
story = False
storyIndex = 0

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if buttonRect.collidepoint(event.pos):
                print("Click")
                startTimer = pygame.time.get_ticks()
                started = True
                clicked = True
                animating = True
                startAn = pygame.time.get_ticks()
                story = True
            if continueRect.collidepoint(event.pos):
                story = True
                clicked = True 
                animating = True
                storyIndex += 1
                startAn = pygame.time.get_ticks()
            
    screen.blit(background, (0,0))
    screen.blit(startbutton, (130,650))
    currentTime = pygame.time.get_ticks()
    if started:
        if story:
            clicked = buttonAnimation(currentTime, startTimer, startAnimation)
            screen.blit(startan, (130,650))
            screen.blit(stories[storyIndex],(0,0)) 
            if animating: 
                currentFrame, chrtTimer, animating = characterAnimation(startAn, anDur, anSpeed, chrtTimer, currentFrame, animating)
            else: 
                screen.blit(player2, (20,160))          
    pygame.display.flip()
    clock.tick(60)