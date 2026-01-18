import pygame

pygame.init()
screen_width = 600
screen = pygame.display.set_mode((screen_width, screen_width))
pygame.display.set_caption("Вверх по лестнице")

running = True
player_coord = (screen_width/40, screen_width * 19 / 20 - screen_width/40)
while running:
    screen.fill('black')
    square = pygame.Surface((screen_width / 20, screen_width / 20))
    square.fill('white')

    for i in range(20):
        coord = (screen_width * i / 20, screen_width * (20 - i - 1) / 20)
        screen.blit(square, coord)
    pygame.draw.circle(screen, "red", (player_coord[0], player_coord[1]), screen_width/40)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()