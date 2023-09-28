import pygame
import random
import math
pygame.init()
window = pygame.display.set_mode()
screen_width = 400
screen_height = 400
screen = pygame.display.set_mode([screen_width,screen_height])
window.fill('pink')
pygame.draw.circle(window, 'orange', [200,200], 200)
pygame.draw.line(window, 'black', [200,0], [200,400])
pygame.draw.line(window, 'black', [0,200], [400,200])



for i in range(10):
    x = random.randrange(0,400)
    y = random.randrange(0,400)
    pygame.draw.circle(window, 'red', [x,y], 5)
    distance_from_center = math.hypot(200-x, 200-y)
    is_in_circle = distance_from_center <=400/2
    if is_in_circle :
        pygame.draw.circle(window, 'red', [x,y], 5)
    else :
        pygame.draw.circle(window, 'green', [x,y], 5)

            
pygame.display.flip()
pygame.time.wait(1000)









