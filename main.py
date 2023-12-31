import pygame 
from constants.setting import SCREEN_WIDTH, SCREEN_HEIGHT
from game.game import Game

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Hell of Airplane")

game = Game(screen)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
   
    game.update()
    game.draw()

    pygame.display.flip()

pygame.quit()