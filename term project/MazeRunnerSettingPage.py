#Ashley Kim
#15-112 F19 Term Project 
#Maze Runner
#setting page

#11/24 (1hr) - 11/25 (1.5hr)

import pygame, sys, os, math, copy


def settingPage(selection):
    pygame.init()
    w,h = 800,600
    margin = 20
    screen = pygame.display.set_mode((w,h))

    pygame.mouse.get_rel()
    pygame.mouse.set_visible(True)
    
    setting = True

    while setting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        #mouse positions in tuple
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        #initiate screen (white)        
        screen.fill((230,253,239))
        
        #setting text
        pygame.font.init()
        fontSize = 50
        font = pygame.font.SysFont('bigcaslonttf',fontSize)
        fontX,fontY = w*2/5,margin
        settingText = font.render('Setting',False,(103,144,229))
        screen.blit(settingText,(fontX,fontY))

        #selection indicator
        outlineW,outlineH = 120,70
        x4,y4 = 350-margin/2,100-margin/2
        innerColor = (80,80,80)
        pygame.draw.rect(screen,innerColor,(x4,y4,outlineW,outlineH))
        
        #button - hard
        x1,y1,buttonW,buttonH = 600,100,100,50
        x4,y4 = x1-margin/2,y1-margin/2
        buttonTextSize = 20
        color = (236,122,102)
        innerColor = (230,253,239)
        if (x1+buttonW > mouse[0] and x1 < mouse[0]) and\
           (y1+buttonH > mouse[1] and y1 < mouse [1]):
            if click[0] == True:
                selection = 'hard'
                buttonTextSize = 23
                
        if selection == 'hard':
            color = (241,43,8)
            innerColor = (80,80,80)

        pygame.draw.rect(screen,innerColor,(x4,y4,outlineW,outlineH))
        pygame.draw.rect(screen, color ,(x1,y1,buttonW,buttonH))
        font = pygame.font.SysFont('yuantittc',buttonTextSize)
        startText = font.render('Hard',True,(0,0,0))
        screen.blit(startText,(x1+margin,y1+margin/2))

        #button - medium
        x2,y2,buttonW,buttonH = 350,100,100,50
        x5,y5 = x2-margin/2,y2-margin/2
        buttonTextSize = 20
        color = (246,250,162)
        innerColor = (230,253,239)
        if (x2+buttonW > mouse[0] and x2 < mouse[0]) and\
           (y2+buttonH > mouse[1] and y2 < mouse [1]):
            if click[0] == True:
                selection = 'medium'
                buttonTextSize = 23

        if selection == 'medium':
            color = (251,233,5)
            innerColor = (80,80,80)

        pygame.draw.rect(screen,innerColor,(x5,y5,outlineW,outlineH))
        pygame.draw.rect(screen, color ,(x2,y2,buttonW,buttonH))
        font = pygame.font.SysFont('yuantittc',buttonTextSize)
        startText = font.render('Medium',True,(0,0,0))
        screen.blit(startText,(x2+margin,y2+margin/2))
                    
        #button - easy
        x3,y3,buttonW,buttonH = 120,100,100,50
        x6,y6 = x3-margin/2,y3-margin/2
        buttonTextSize = 20
        color = (123,250,128)
        innerColor = (230,253,239)
        if (x3+buttonW > mouse[0] and x3 < mouse[0]) and\
           (y3+buttonH > mouse[1] and y3 < mouse [1]):
            if click[0] == True:
                selection = 'easy'
                buttonTextSize = 23

        if selection == 'easy':
            color = (6,234,14)
            innerColor = (80,80,80)

        pygame.draw.rect(screen,innerColor,(x6,y6,outlineW,outlineH))
        pygame.draw.rect(screen, color ,(x3,y3,buttonW,buttonH))
        font = pygame.font.SysFont('yuantittc',buttonTextSize)
        startText = font.render('Easy',True,(0,0,0))
        screen.blit(startText,(x3+margin,y3+margin/2))



        #go back to starting page
        x7,y7 = 250,530
        pygame.draw.rect(screen, (151,237,220),(x7,y7,buttonW*3,buttonH))
        fontSize = 25
        font = pygame.font.SysFont('bigcaslonttf',fontSize)
        fontX,fontY = 255,h-margin*3
        settingText = font.render('Go back to the starting page',True,
                                  (42,97,114))
        screen.blit(settingText,(fontX,fontY))

        if (x7+buttonW*3 > mouse[0] and x7 < mouse[0]) and\
           (y7+buttonH > mouse[1] and y7 < mouse [1]):
            if click[0] == True:
                return (selection,'no')


        
        
        pygame.display.flip()

