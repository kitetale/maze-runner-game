#Ashley Kim
#15-112 F19 Term Project 
#Maze Runner
#intro page

#reference docs
    #https://www.pygame.org/docs/ref/pygame.html
    #http://www.cs.cmu.edu/~112/notes/term-project.html#tp2del

#11/21 (2.5hr) - 11/22 (1hr)

import pygame, sys, os

def startPage(level = 'medium'):
    pygame.init()
    w,h = 800,600
    screen = pygame.display.set_mode((w,h))

    pygame.mouse.get_rel()
    pygame.mouse.set_visible(True)
    pygame.event.set_grab(False)
    
    start = True
    while start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        #mouse positions in tuple
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        #initiate screen (white)        
        screen.fill((255,255,255))
        
        #background
        #image from https://www.msn.com/en-us/travel/article/new-englands-largest-corn-maze-opens-for-season/ar-AAFbPBG
        image = pygame.image.load('Background.jpg')
        image = pygame.transform.scale(image,(w,h))
        screen.blit(image,(0,0))
        
        #title text
        pygame.font.init()
        fontSize = 100
        font = pygame.font.SysFont('',fontSize)
        fontX,fontY = 180,120
        title = font.render('Maze Runner', False, (255,179,26))
        screen.blit(title,(fontX,fontY))
        
        #start game button
    #button rect & function
        x1,y1,buttonW,buttonH = 600,350,100,50
        if (x1+buttonW > mouse[0] and x1 < mouse[0]) and\
           (y1+buttonH > mouse[1] and y1 < mouse [1]):
            pygame.draw.rect(screen, (18,156,77),(x1,y1,buttonW,buttonH))
            if click[0] == True:
                return 'game'
                
        else:
            pygame.draw.rect(screen, (74,211,133),(x1,y1,buttonW,buttonH))
            
    #button text
        buttonTextSize = 20
        margin = 13
        font = pygame.font.SysFont('yuantittc',buttonTextSize)
        startText = font.render('Start',False,(0,0,0))
        screen.blit(startText,(x1+margin*2,y1+margin/2))
        
        #setting button
    #button rect & function
        x2,y2 = 600,420
        if (x2+buttonW > mouse[0] and x2 < mouse[0]) and\
           (y2+buttonH > mouse[1] and y2 < mouse [1]):
            pygame.draw.rect(screen, (55,165,168),(x2,y2,buttonW,buttonH))
            if click[0] == True:
                return 'setting'
        else:
            pygame.draw.rect(screen, (131,207,209),(x2,y2,buttonW,buttonH))

    #button text
        font = pygame.font.SysFont('yuantittc',buttonTextSize)
        settingText = font.render('Setting',False,(0,0,0))
        screen.blit(settingText,(x2+margin,y2+margin/2))
        
        #quit button
    #button rect & function
        x3,y3 = 600,490
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
        quitText = font.render('Quit',False,(0,0,0))
        screen.blit(quitText,(x3+margin*2,y3+margin/2))

        #How do I play this button
    #button text & function
        x4,y4 = 50,515
        textSize = 40
        font = pygame.font.SysFont('',textSize)
        if (x4+buttonW*2 > mouse[0] and x4 < mouse[0]) and\
           (y4+buttonH > mouse[1] and y4 < mouse [1]):
            pygame.draw.rect(screen, (213,139,255),
                             (x4-margin,y4-margin,buttonW*2-margin,buttonH))
            helpText = font.render('How to play',True,(255,255,255))
            if click[0] == True:
                return 'help'
        else:
            helpText = font.render('How to play',True,(174,174,174))
        screen.blit(helpText,(x4,y4))

        

        pygame.display.flip()

