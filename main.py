import sensors,env
import pygame

pygame.init()

envi = env.buildEnvironment((600,1200))
originalMap = envi.map.copy()
laser = sensors.laserSensor(200,originalMap,uncertainty=(0.5,0.01))
envi.map.fill((0,0,0))
envi.infomap = envi.map.copy()
running = True

while running :
    sensorOn = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if pygame.mouse.get_focused():
            sensorOn = True
        elif not pygame.mouse.get_focused():
            sensorOn = False
    print(f"sensorOn status: {sensorOn}")
    if sensorOn:
        pos = pygame.mouse.get_pos()
        print(f"Mouse is focused. Sensor position: {pos}")
        laser.position = pos
        sensor_data = laser.sense_obstacles()
        envi.dataStorage(sensor_data)
        envi.show_sensorData()
    else:
        print("Mouse not focused or leaving window, sensor is OFF.")
    envi.map.blit(envi.infomap,(0,0))
    pygame.display.update()

pygame.quit()

""" import env,sensors
import pygame,math

envi = env.buildEnvironment((600,1200))
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.update """