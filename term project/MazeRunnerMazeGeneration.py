#Ashley Kim
#15-112 F19 Term Project 
#Maze Runner
#maze generation algorithm: recursive division
    #http://weblog.jamisbuck.org/2011/1/12/maze-generation-recursive-division-algorithm

#refernce docs
    #https://www.pygame.org/docs/ref/pygame.html
    #http://www.cs.cmu.edu/~112/notes/term-project.html#tp2del

#11/24 (5hr)

import math, random

def generateMaze(widthStart,widthEnd,heightStart,heightEnd):
    wN = widthEnd - widthStart
    hN = heightEnd - heightStart
    pathWidth = 3

    #base case: when the field can't be divided any further
    if (wN < 6) and (hN < 6):
        return []

    #when width cannot be divided any further but height can
    elif (wN < 6):
        wallY = random.randint(heightStart+pathWidth,heightEnd-pathWidth)
        try:
            wallX = random.randint(widthStart,widthEnd-pathWidth)
        except:
            wallX = widthStart
        newSection = ([(x,wallY) for x in range(widthStart,wallX)]+
                    [(x,wallY) for x in range(wallX+pathWidth,widthEnd)])
        return (newSection
                + generateMaze(widthStart,widthEnd,heightStart,wallY)
                + generateMaze(widthStart,widthEnd,wallY+1,heightEnd))
    
    #vice-versa 
    elif (hN < 6):
        wallX = random.randint(widthStart+pathWidth,widthEnd-pathWidth)
        try:
            wallY = random.randint(heightStart,heightEnd-pathWidth)
        except:
            wallY = heightStart
        newSection = ([(wallX,y) for y in range(heightStart,wallY)]+
                    [(wallX,y) for y in range(wallY+pathWidth,heightEnd)])
        return (newSection
                + generateMaze(widthStart,wallX,heightStart,heightEnd)
                + generateMaze(wallX+1,widthEnd,heightStart,heightEnd))
    
    #when both width&height can be divided, divide whatever side that's longer
    else:
        if (wN > hN):
            wallX = random.randint(widthStart+pathWidth,widthEnd-pathWidth)
            try:
                wallY = random.randint(heightStart,heightEnd-pathWidth)
            except:
                wallY = heightStart
            newSection = ([(wallX,y) for y in range(heightStart,wallY)]+
                    [(wallX,y) for y in range(wallY+pathWidth,heightEnd)])
            return (newSection
                    + generateMaze(wallX+1,widthEnd,heightStart,heightEnd)
                    + generateMaze(widthStart,wallX,heightStart,heightEnd))
        else:
            wallY = random.randint(heightStart+pathWidth,heightEnd-pathWidth)
            try:
                wallX = random.randint(widthStart,widthEnd-pathWidth)
            except:
                wallX = widthStart
            newSection = ([(x,wallY) for x in range(widthStart,wallX)]+
                        [(x,wallY) for x in range(wallX+pathWidth,widthEnd)])
            return (newSection
                    + generateMaze(widthStart,widthEnd,wallY+1,heightEnd)
                    + generateMaze(widthStart,widthEnd,heightStart,wallY))   

