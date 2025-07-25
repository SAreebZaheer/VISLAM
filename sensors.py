import pygame
import math
import numpy as np

pygame.init()

def uncertainty_add(distance,angle,sigma):
    mean = np.array([distance,angle])
    covariance = np.diag(sigma ** 2)
    distance,angle = np.random.multivariate_normal(mean,covariance)
    distance = max(distance,0)
    angle = max(angle,0)

    return [distance,angle]

class laserSensor:
    
    def __init__(self,range,map,uncertainty):
        self.range = range
        self.speed = 4
        self.sigma = np.array([uncertainty[0],uncertainty[1]])
        self.position = (0,0)
        self.map = map
        self.w,self.h = pygame.display.get_surface().get_size()
        self.sensedObstacles = []

    def distance(self,obstaclePosition):
        px = (obstaclePosition[0] - self.position[0])**2
        py = (obstaclePosition[1] - self.position[1])**2
        return math.sqrt(px+py)
    
    def sense_obstacles(self):
        data = []
        x1,y1 = self.position[0], self.position[1]
        for angle in np.linspace(0.2*math.pi,60,False):
            x2,y2 = (x1 + self.range * math.cos(angle), y1 - self.range * math.sin(angle))
            for i in range(0,100):
                u = i/100
                x = int(x2 * u + x1 * (1-u))
                y = int(y2 * u + y1 * (1-u))
                if 0<x<self.w and 0<y<self.h:
                    color = self.map.get_at((x,y))
                    print(f"Checking pixel ({x}, {y}) - Color: {color}")
                    if ((color[0],color[1],color[2]) == (0,0,0)):
                        print(f"Obstacle detected at ({x}, {y})!")
                        distance = self.distance((x,y))
                        output = uncertainty_add(distance,angle,self.sigma)
                        output.append(self.position)
                        data.append(output)
                        break
        if len(data) > 0:
            return data
        else:
            return False