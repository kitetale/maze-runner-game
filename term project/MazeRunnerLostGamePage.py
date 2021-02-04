#Ashley Kim
#15-112 F19 Term Project 
#Maze Runner
#lost game page

#12/3 9:50pm - 10:50pm

import pygame, sys, os

def lostGamePage():
    #init
    pygame.init()
    w,h = 800,600
    screen = pygame.display.set_mode((w,h))
    lost = True
    pygame.mouse.get_rel()
    pygame.mouse.set_visible(True)
    pygame.event.set_grab(False)
    
    #penguin sprite!
    penguin = []
    for i in range(21):
        sprite = pygame.image.load(f'encouragePenguin-{i+1} (dragged).tiff')
        penguin.append(sprite)

    while lost:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        #mouse positions in tuple
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        
        #background screen color       
        screen.fill((230,236,253))

        #game over text
        pygame.font.init()
        fontSize = 110
        font = pygame.font.SysFont('',fontSize)
        fontX,fontY = 150,70
        title = font.render('   Game Over    ', True, (136,155,208))
        screen.blit(title,(fontX,fontY))

        #maybe next round text
        pygame.font.init()
        fontSize = 40
        font = pygame.font.SysFont('',fontSize)
        fontX,fontY = 280,190
        title = font.render('Maybe next round!', True, (127,82,252))
        screen.blit(title,(fontX,fontY))

        #encourage penguin
        #from https://imgur.com/gallery/G7UWo
        spriteCounter = (pygame.time.get_ticks()//200) % 21
        penguinSlide = penguin[spriteCounter]
        penguinSlide = pygame.transform.scale(penguinSlide,(250,240))
        screen.blit(penguinSlide,(280,240))

        #restart game button
    #button rect & function
        x1,y1,buttonW,buttonH = 250,520,120,50
        if (x1+buttonW > mouse[0] and x1 < mouse[0]) and\
           (y1+buttonH > mouse[1] and y1 < mouse [1]):
            pygame.draw.rect(screen, (18,156,77),(x1,y1,buttonW,buttonH))
            if click[0] == True:
                return 'replay'
        else:
            pygame.draw.rect(screen, (74,211,133),(x1,y1,buttonW,buttonH))

    #button text
        buttonTextSize = 20
        margin = 10
        font = pygame.font.SysFont('yuantittc',buttonTextSize)
        startText = font.render('Play Again',True,(230,236,253))
        screen.blit(startText,(x1+margin,y1+margin/2))

    #quit button
    #button rect & function
        x3,y3 = 430,520
        if (x3+buttonW > mouse[0] and x3 < mouse[0]) and\
           (y3+buttonH > mouse[1] and y3 < mouse [1]):
            pygame.draw.rect(screen, (187,27,14),(x3,y3,buttonW,buttonH))
            if click[0] == True:
                pygame.quit()
                sys.exit()
        else:
            pygame.draw.rect(screen, (255,75,60),(x3,y3,buttonW,buttonH))

    #button text
        font = pygame.font.SysFont('yuantittc',buttonTextSize)
        quitText = font.render('Quit',True,(230,236,253))
        screen.blit(quitText,(x3+margin*4,y3+margin/2))


        pygame.display.flip()


