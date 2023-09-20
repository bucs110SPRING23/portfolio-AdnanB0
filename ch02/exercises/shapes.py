import pygame
pygame.init()
window = pygame.display.set_mode()
x1 = range(5)
pygame.draw.circle(window, "white", [200, 150], 50)
pygame.display.flip()
pygame.draw.circle(window, "white", [200, 300], 100)
pygame.display.flip()
pygame.draw.circle(window, "white", [200, 550], 150)
pygame.display.flip()
pygame.time.wait(1000)

