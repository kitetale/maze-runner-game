#Ashley Kim
#15-112 F19 Term Project 
#Maze Runner
#object classes

import pygame, sys, math, copy, decimal

#11/25 (3.5hr)
#TP 2 11/27 9:37pm-1am... 11/28 1pm-3pm
#12/4 (4.5hr)

def rotate2d(position,radian):
    x,y = position
    s,c = math.sin(radian),math.cos(radian)
    return x*c-y*s,y*c+x*s

class Camera:
    cubes = set()
    def __init__(self,position=(0,0,0),rotation=(0,0)):
        self.pos = list(position)
        self.rot = list(rotation)
        
    @staticmethod
    def setCubePos(cubePos):
        Camera.cubes = set(cubePos)

    def events(self,event):
        if event.type == pygame.MOUSEMOTION:
            # event.rel = amount/distance mouse moved 
            x,y = event.rel
            x /= 200
            y /= 200
            #self.rot[0] += y
            self.rot[1] += x
            
    def roundRotation(self,rotation):
        degrees = [0,math.pi/2,math.pi,math.pi*3/2]
        diff = []
        for degree in degrees:
            diff.append(abs(degree-(self.rot[1]%(math.pi*2))))
        return degrees[diff.index(min(diff))]

    @staticmethod
    def getTime(time):
        Camera.time = time

    def update(self,dt,key):
        s = .1
        #degree = self.roundRotation(self.rot[1])
        degree = self.rot[1]%(math.pi*2)
        x,y = s*math.sin(degree),s*math.cos(degree)
        around = [(0,-1),(-1,1),(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1)]
        if degree>10 and degree<math.PI/2-10:
            posList = around[0:3]
        elif degree>=math.pi/2-10 and degree<=math.pi/2+10:
            posList = around[1:4]
        elif degree>math.pi/2+10 and degree<math.pi-10:
            posList = around[2:5]
        elif degree>=math.pi-10 and degree<=math.pi+10:
            posList = around[3:6]
        elif degree>math.pi+10 and degree<math.pi*3/2-10:
            posList = around[4:7]
        elif degree>=math.pi*3/2-10 and degree<=math.pi*3/2+10:
            posList = around[5:8]
        elif degree>math.pi*3/2+10 and degree<math.pi*2-10:
            posList = around[6:8]+around[0]
        else:
            posList = around[-1]+around[0:2]
            
        
        # z direction
        #up & down
        if key[pygame.K_a]:
            if self.pos[1] == -.3:
                self.pos[1] = -1
            
        elif key[pygame.K_d]:
            if self.pos[1] == -1:
                self.pos[1] = -.3
            
        # x/y direction
        #forward & backward
        
        elif key[pygame.K_w]:
            if self.pos[1] != -0.30 and self.pos[1] != -1:
                return 'lost'
            elif self.pos[1] == -.3:
                self.pos[0] += x
                self.pos[2] += y
                tempX = roundHalfUp(self.pos[0])
                tempY = roundHalfUp(self.pos[2])
                if (tempX,tempY) in Camera.cubes:
                    self.pos[0] -= x
                    self.pos[1] -= y
            
                    
                '''
                if self.pos[1] > -.5 and\
                    (self.pos[0]//1+posList[1][0],
                    self.pos[2]//1+posList[1][1]) not in Camera.cubes:
                    self.pos[0],self.pos[2] = (self.pos[0]//1+posList[1][0],
                                                self.pos[2]//1+posList[1][1])
                for i in {0,2}:
                    position = (self.pos[0]//1+posList[i][0],
                                self.pos[2]//1+posList[i][1])
                    if self.pos[1] > -.5 and position in Camera.cubes:
                        print(position)
                        self.pos[0] -= x
                        self.pos[2] -= y
                        break
                '''
            
        elif key[pygame.K_s]:
            if self.pos[1] != -0.30 and self.pos[1] != -1:
                return 'lost'
            elif self.pos[1] == -.3:
                self.pos[0] -= x
                self.pos[2] -= y
                tempX = roundHalfUp(self.pos[0])
                tempY = roundHalfUp(self.pos[2])
                if (tempX,tempY) in Camera.cubes:
                    self.pos[0] += x
                    self.pos[1] += y
                
                
        if (self.pos[0] <= 0 and self.pos[2] >= 8) and\
           (self.pos[0] <= 0 and self.pos[2] <= 11):
            return 'end'
        elif self.pos[1] != -1 and self.pos[1] != -.3:
            return 'lost'

        elif key[pygame.K_h]:
            return 'no'
        
        
#from 15-112 hw files (hw4.py)
def almostEqual(d1, d2, epsilon=10**-7):
# note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) <= epsilon)

def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))
                            

class Cube:
    cubeAllPos = []
    vertices = (-1,-1,-1),(1,-1,-1),(1,1,-1),(-1,1,-1),\
               (-1,-1,1),(1,-1,1),(1,1,1),(-1,1,1)
    faces = (0,1,2,3),(4,5,6,7),(0,1,5,4),(2,3,7,6),(0,3,7,4),(1,2,6,5)
    colors = (102,204,0),(102,255,102),(0,102,0),(0,0,0),\
             (255,128,0),(255,255,0)

    def __init__ (self, pos=(0,0,0), colors = colors):
        x,y,z = pos
        self.verts = [(x+X/2,y+Y/2,z+Z/2) for X,Y,Z in self.vertices]
        Cube.cubeAllPos += [(x,y,z)]
        self.colors = colors

