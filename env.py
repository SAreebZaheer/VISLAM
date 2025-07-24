#Building a virtual environment for the autonomous vehicle using a floor map png file

import math
import pygame

pygame.init()

class buildEnvironment:
    def __init__(self,MapDimensions):
        pygame.init()
        self.pointCloud=[]
        self.externalMap = pygame.image.load('floor.png')
        self.maph,self.mapw = MapDimensions
        self.MapWindowName = 'RRT Path Planning'
        pygame.display.set_caption(self.MapWindowName)
        self.map = pygame.display.set_mode((self.mapw,self.maph))
        self.map.blit(self.externalMap,(0,0))

        #Colours
        self.black = (0, 0, 0)
        self.grey = (70, 70, 70)
        self.Blue = (0, 0, 255)
        self.Green = (0, 255, 0)
        self.Red = (255, 0, 0)
        self.white = (255, 255, 255)

    def AD2pos(self,distance,angle,robotPos):
        x = distance * math.cos(angle) + robotPos[0]
        y = -distance * math.sin(angle) + robotPos[1]
        return (int(x), int(y))
    
    def dataStorage(self,data):
        print(len(self.pointCloud))
        if data!=False:
            for element in data:
                point = self.AD2pos(element[0], element[1], element[2])
                if point not in self.pointCloud:
                    self.pointCloud.append(point)

    def show_sensorData(self):
        self.infomap = self.map.copy()
        for point in self.pointCloud:
            self.infomap.set_at((int(point[0]),int(point[1])),(255,0,0))