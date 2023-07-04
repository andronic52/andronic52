import pygame
from sys import exit

pygame.init()

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('1 Hour Challenge!')

speed = 4

font = pygame.font.Font('../Assets/font/Pixeltype.ttf', 50)

game_name = font.render('Water Jump', False, 'white')
game_name = pygame.transform.scale2x(game_name)

play_buttton = font.render('PLAY', False, 'White')
play = pygame.surface.Surface((300, 50))
play_rect = play.get_rect(midbottom=(400, 250))
play.fill('grey')
running = 0

water = pygame.image.load('../Assets/graphics/WATER.png').convert_alpha()
sand = pygame.image.load('../Assets/graphics/sand.png').convert_alpha()
sand = pygame.transform.scale(sand, (800, 100))
fish = pygame.image.load('../Assets/graphics/2023-05-14 (3).png').convert_alpha()
fish = pygame.transform.scale(fish, (100, 50 ))
fish_rect = fish.get_rect(midbottom=(100, 400))

obstacle = pygame.surface.Surface((50, 400))
obstacle_rect = obstacle.get_rect(midbottom=(900, 400))

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if running == 0:
            screen.blit(water, (0, 0))
            screen.blit(game_name, (250, 50))
            screen.blit(play, play_rect)
            screen.blit(play_buttton, (350, 220))
        if event.type == pygame.MOUSEBUTTONDOWN:
            if play_rect.collidepoint(event.pos):
                running += 1
    if running == 1:
        screen.blit(water, (0, 0))
        screen.blit(sand, (0, 300))
        screen.blit(fish, fish_rect)
        screen.blit(obstacle, obstacle_rect)
        obstacle_rect.left -= speed
        if obstacle_rect.right <= 0:
            obstacle_rect.left += 900
            speed += 1

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            if obstacle_rect.left - 100 <= fish_rect.right <= obstacle_rect.left:
                fish_rect.left += 400
        if keys[pygame.K_LEFT]:
            fish_rect.left -= 4
        if keys[pygame.K_RIGHT]:
            fish_rect.right += 4
        if keys[pygame.K_UP]:
            fish_rect.bottom -= 4
        if keys[pygame.K_DOWN]:
            fish_rect.bottom += 4
        if fish_rect.left <= 0:
            fish_rect.left = 0
        if fish_rect.right >= 800:
            fish_rect.right = 800
        if obstacle_rect.colliderect(fish_rect):
            exit()

    pygame.display.update()
    clock.tick(60)
