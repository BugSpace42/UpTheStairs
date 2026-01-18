import pygame

pygame.init()
screen_width = 600
screen = pygame.display.set_mode((screen_width, screen_width))
pygame.display.set_caption("Вверх по лестнице")

square = pygame.Surface((screen_width/20, screen_width/20))
square.fill('white')

running = True
while running:
    for i in range(20):
        coord = (screen_width*i/20, screen_width*(20-i-1)/20)
        screen.blit(square, coord)

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()