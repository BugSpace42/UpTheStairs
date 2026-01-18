import pygame

pygame.init()
screen_width = 600
screen = pygame.display.set_mode((screen_width, screen_width))
pygame.display.set_caption("Вверх по лестнице")

running = True
number_of_steps = 20
player_radius = screen_width/(number_of_steps*2)
player_coord = (player_radius, screen_width * (number_of_steps-1) / number_of_steps - player_radius)
while running:
    screen.fill('black')
    square = pygame.Surface((screen_width / number_of_steps, screen_width / number_of_steps))
    square.fill('white')

    for i in range(number_of_steps):
        coord = (screen_width * i / number_of_steps, screen_width * (number_of_steps - i - 1) / number_of_steps)
        screen.blit(square, coord)
    pygame.draw.circle(screen, "red", (player_coord[0], player_coord[1]), player_radius)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player_coord = (player_coord[0] + screen_width / number_of_steps, player_coord[1] - screen_width / number_of_steps)