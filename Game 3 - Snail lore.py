import pygame
from sys import exit


pygame.init()

tp = 1

station = 1

metal_speed = 1

player_speed = 4

moving = 1

largada = False

game_active = 0

snail_speed = 4

largura = 100

font = pygame.font.Font('../Assets/font/Pixeltype.ttf', 50)

font2 = pygame.font.Font('../Assets/font/Pixeltype.ttf', 150)

start_button = pygame.surface.Surface((250, 50))
start_button_rect = start_button.get_rect(midbottom=(400, 250))
start_button.fill('grey')
start_button_text = font.render('Start', False, 'black')
start_button_text_rect = start_button_text.get_rect(midbottom=(400, 247))

quit_button = pygame.surface.Surface((250, 50))
quit_button_rect = quit_button.get_rect(midbottom=(400, 315))
quit_button.fill('grey')
quit_button_text = font.render('Quit', False, 'black')
quit_button_text_rect = start_button_text.get_rect(midbottom=(410, 312))

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('test game')

sky_surface = pygame.image.load('../Assets/graphics/Sky.png').convert()
ground_surface = pygame.image.load('../Assets/graphics/ground.png').convert()

sky_colour = pygame.surface.Surface((800, 400))


teleport_points = pygame.surface.Surface((10, 20))
teleport_points_rect = teleport_points.get_rect(midbottom=(500, 260))
teleport_points.fill('yellow')

snail_surface = pygame.image.load('../Assets/graphics/snail1.png')
snail_rect = snail_surface.get_rect(midbottom=(900, 300))

text = font.render('Score:', False, 'black')
text_rect = text.get_rect(midtop=(400, 50))

text_1 = font2.render('My Game', False, 'black')
text_1_rect = text_1.get_rect(midbottom=(400, 150))

here = font.render('-Here', False, 'black')
here_rect = here.get_rect(bottomleft=(10, 300))

sike = font.render('SIKE!', False, 'black')
sike_rect = sike.get_rect(bottomleft=(10, 270))

player_surface = pygame.image.load('../Assets/graphics/player_walk_1.png')
player_rect = player_surface.get_rect(midbottom=(100, 300))

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active == 0:

            screen.blit(sky_surface, (0, 0))
            screen.blit(ground_surface, (0, 300))

            screen.blit(text_1, text_1_rect)

            screen.blit(start_button, start_button_rect)
            pygame.draw.rect(screen, 'black', start_button_rect, 5)
            screen.blit(start_button_text, start_button_text_rect)

            screen.blit(quit_button, quit_button_rect)
            pygame.draw.rect(screen, 'black', quit_button_rect, 5)
            screen.blit(quit_button_text, quit_button_text_rect)

            if event.type == pygame.MOUSEBUTTONDOWN and start_button_rect.collidepoint(event.pos):
                game_active += 1

            if event.type == pygame.MOUSEBUTTONDOWN and quit_button_rect.collidepoint(event.pos):
                pygame.quit()
                exit()

    if game_active == 1:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        metal = pygame.surface.Surface((largura, 400))
        metal_rect = metal.get_rect(topleft=(-100, 0))
        metal.fill('grey')
        if largada:
            largura += metal_speed
        if moving == 1:
            snail_rect.left -= snail_speed
            if snail_rect.right <= 0:
                snail_rect.left += 900
                snail_speed += 1
        if player_rect == snail_rect:
            if player_rect.left > 0:
                screen.blit(here, here_rect)
            else:
                screen.blit(sike, sike_rect)
        screen.blit(teleport_points, teleport_points_rect)
        screen.blit(player_surface, player_rect)
        screen.blit(snail_surface, snail_rect)
        screen.blit(text, text_rect)

        if player_rect.colliderect(teleport_points_rect):
            if tp < 3:
                tp += 1
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            if player_rect.right < 700:
                if tp > 0:
                    if 200 > snail_rect.left - player_rect.left > 10:
                        player_rect.right += 200
                        tp -= 1
        if player_rect != snail_rect:
            if keys[pygame.K_DOWN]:
                if player_rect.bottom < 300:
                    player_rect.bottom += 4
            if keys[pygame.K_UP]:
                if player_rect.top > 0:
                    player_rect.top -= 4
            if keys[pygame.K_LEFT]:
                if player_rect.left > 0:
                    player_rect.left -= 4
            if keys[pygame.K_RIGHT]:
                if player_rect.right < 800:
                    player_rect.right += 4
        else:
            if keys[pygame.K_LEFT]:
                if player_rect.left > 0:
                    player_rect.left -= player_speed
            if keys[pygame.K_RIGHT]:
                player_rect.right += player_speed

        if player_rect.colliderect(snail_rect):
            player_surface = pygame.image.load('../Assets/graphics/snail2.png')
            player_rect = snail_rect
            if 10 < player_rect.left < 790:
                moving -= 1

        if station == 1:
            if player_rect.left > 810:
                player_rect.right -= 900
                sky_surface = pygame.surface.Surface((800, 400))
                here = font.render('-Here', False, 'white')
                sike = font.render('SIKE!', False, 'white')
                text_rect.left -= 150
                text = font.render('What are you doing here?', False, 'white')
                station += 1

        if station == 2:
            if player_rect.left > 810:
                player_rect.right -= 900
                sky_surface = pygame.surface.Surface((800, 400))
                text_rect.left += 150
                here = font.render('-Here', False, 'blue')
                sike = font.render('SIKE!', False, 'blue')
                sky_surface.fill('red')
                text = font.render('STOP!', False, 'blue')
                station += 1

        if station == 3:
            if player_rect.left > 810:
                player_rect.right -= 900
                sky_surface = pygame.surface.Surface((800, 400))
                here = font.render('-Here', False, 'white')
                sike = font.render('SIKE!', False, 'white')
                sky_surface.fill('blue')
                text = font.render('I warned you...', False, 'white')
                station += 1

        if station == 4:
            if player_rect.left > 810:
                player_rect.right -= 900
                sky_surface = pygame.surface.Surface((800, 400))
                here = font.render('-Here', False, 'white')
                sike = font.render('SIKE!', False, 'white')
                sky_surface.fill('black')
                text = font.render('YOU ARE GAY!!!', False, 'white')
                text_rect.left -= 50
                station += 1

        if station == 5:
            screen.blit(metal, metal_rect)
            largada = True
            if snail_rect.left < metal_rect.right:
                player_speed = 0
                snail_rect.left += 3
            else:
                player_speed = 4
            if player_rect.left > 800:
                sky_surface = pygame.image.load('../Assets/graphics/Sky.png')
                game_active = 0

    pygame.display.update()
    clock.tick(60)
