#Ashley Kim
#15-112 F19 Term Project 
#Maze Runner
#help page

#11/25
#12/3 (1hr)
import pygame, sys, os, math, copy

def helpPage(level):
    pygame.init()
    w,h = 800,600
    margin = 20
    screen = pygame.display.set_mode((w,h))

    pygame.mouse.get_rel()
    pygame.event.set_grab(False)
    pygame.mouse.set_visible(True)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        #mouse positions in tuple
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        #initiate screen        
        screen.fill((255,237,192))

        #help page text
        pygame.font.init()
        fontSize = 55
        font = pygame.font.SysFont('bigcaslonttf',fontSize)
        fontX,fontY = w/3-margin*2,margin
        settingText = font.render('HELP PAGE',True,(122,232,108))
        screen.blit(settingText,(fontX,fontY))

        #moves
        fontSize = 30
        font = pygame.font.SysFont('yuantittc',fontSize)
        fontX,fontY = w/2-margin*2,margin*5.5
        moveText = font.render('Moves',True,(33,163,210))
        screen.blit(moveText,(fontX,fontY))
        
        #Tips
        fontX,fontY = w/2-margin*2,h*2/5+margin
        moveText = font.render('  Tips',True,(111,151,252))
        screen.blit(moveText,(fontX,fontY))
        
        #short description of the game
        text = "YOU got 5 minutes."
        fontX,fontY = w/3,h*4/5-margin*2
        desText = font.render(text,True,(246,143,143))
        screen.blit(desText,(fontX,fontY))
        fontSize = 25
        font = pygame.font.SysFont('yuantittc',fontSize)
        text = 'Escape the maze before the time runs out!'
        desText = font.render(text,True,(255,144,91))
        fontX,fontY = w/5,h*4/5
        screen.blit(desText,(fontX,fontY))
    
        #keys & mouse input
        fontSize = 20
        font = pygame.font.SysFont('yuantittc',fontSize)
        fontX,fontY = w/4-margin,margin*8
        text = "    'W' - move forward      'S' - move backward"
        moveText = font.render(text,True,(27,58,161))
        screen.blit(moveText,(fontX,fontY))
        
        text = "        'A' - peak up        'D' - go back down"
        fontX,fontY = w/4,margin*9.5
        moveText = font.render(text,True,(27,58,161))
        screen.blit(moveText,(fontX,fontY))

        text = "MOUSE - look around (rotation)"
        fontX,fontY = w/3,margin*11
        moveText = font.render(text,True,(27,58,161))
        screen.blit(moveText,(fontX,fontY))

        #visit setting
        text = "        Visit 'Setting' to choose the difficulty of the maze!"
        fontX,fontY = w/6,h*3/5-margin*3
        settingText = font.render(text,True,(150,111,245))
        screen.blit(settingText,(fontX,fontY))
        text = "                      Avoid the walls: they're gluttonous."
        fontX,fontY = w/6,h*3/5-margin*1.5
        settingText = font.render(text,True,(220,111,245))
        screen.blit(settingText,(fontX,fontY))
        text = "The walls will warn you by flickering if you get too close to them."
        fontX,fontY = w/6,h*3/5
        settingText = font.render(text,True,(255,120,200))
        screen.blit(settingText,(fontX,fontY))

        #button to go back to the starting page
        x1,y1,buttonW,buttonH = w/2-margin*2,h-margin*3,100,50
        if (x1+buttonW > mouse[0] and x1 < mouse[0]) and\
           (y1+buttonH > mouse[1] and y1 < mouse [1]):
            pygame.draw.rect(screen,(183,94,218),(x1,y1,buttonW,buttonH))
            if click[0] == True:
                return 'no'
        else:
            pygame.draw.rect(screen,(201,139,226),(x1,y1,buttonW,buttonH))

        font = pygame.font.SysFont('yuantittc',fontSize)
        returnText = font.render('Return',False,(255,237,192))
        screen.blit(returnText,(x1+margin,y1+margin/2))       

        pygame.display.flip()

