#Ashley Kim
#15-112 F19 Term Project 
#Maze Runner
# end page

#11/25 

import pygame, sys, os

##################################################
#from 'getFileNum.py' from Katja Brackelmanns-Puig
def readFile(path):
    with open(path, "rt") as f:
        return f.read()

def writeFile(path, contents):
    with open(path, "wt") as f:
        f.write(contents)
        
#with some changes
def getContent(path,score):
    cont = readFile(path)
    newCont = []
    content = ''
    added = False
    for num in cont.splitlines():
        if num == '':
            continue
        elif score<=int(num) and added == False:
            newCont.append(str(score))
            newCont.append(num)
            added = True
        else:
            newCont.append(num)
    for num in newCont:
        content += num+'\n'
    content.strip()
    writeFile(path,content)
    return newCont
        
##################################################
def endPage(time,level):
    pygame.init()
    w,h = 800,600
    margin = 10
    screen = pygame.display.set_mode((w,h))
    
    end = True
    
    pygame.mouse.get_rel()
    pygame.mouse.set_visible(True)
    pygame.event.set_grab(False)

    scoreList = getContent(f'scoreboard{level}.txt',time)
    
    while end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        #mouse positions in tuple
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        #background screen       
        screen.fill((255,193,111))

        #congratulation text
        pygame.font.init()
        fontSize = 100
        font = pygame.font.SysFont('',fontSize)
        fontX,fontY = 80,80
        title = font.render('Congratulations!!!', True, (247,93,40))
        screen.blit(title,(fontX,fontY))

        #you escaped the maze
        fontSize = 30
        font = pygame.font.SysFont('',fontSize)
        fontX,fontY = 205,170
        title = font.render('You escaped the maze :D Good job.', True, (53,148,52))
        screen.blit(title,(fontX,fontY))

        #scoreboard
        fontSize = 40
        font = pygame.font.SysFont('',fontSize)
        fontX,fontY = 100,230
        title = font.render('Fastest Record', True, (38,181,203))
        screen.blit(title,(fontX,fontY))
        fontSize = 25
        font = pygame.font.SysFont('',fontSize)
        fontX,fontY = 145,260
        title = font.render(f'<{level} mode>', True, (38,181,203))
        screen.blit(title,(fontX,fontY))

        fontSize = 35
        font = pygame.font.SysFont('',fontSize)
        fontX,fontY = 180,290
        for score in scoreList:
            title = font.render(score, True, (97,145,238))
            screen.blit(title,(fontX,fontY))
            fontY += margin*4
            if fontY > 460:
                break

        #your score!
        fontSize = 30
        font = pygame.font.SysFont('',fontSize)
        fontX,fontY = 380,340
        title = font.render('Time you took:                    seconds', True, (38,181,203))
        screen.blit(title,(fontX,fontY))
        fontSize = 70
        font = pygame.font.SysFont('',fontSize)
        fontX,fontY = 540,320
        score = font.render(str(time), True, (10,10,10))
        screen.blit(score,(fontX,fontY))
        
        

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
        startText = font.render('Play Again',True,(255,255,255))
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
        quitText = font.render('Quit',True,(0,0,0))
        screen.blit(quitText,(x3+margin*4,y3+margin/2))
    

        pygame.display.flip()


