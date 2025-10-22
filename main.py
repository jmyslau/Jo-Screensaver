import pygame
from os.path import join 

from random import randint

# general setup 
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('pygame is fun')
show_info = False
running = True
clock = pygame.time.Clock()
font1 = pygame.font.Font(None, 50)
font2 = pygame.font.Font(None, 30)

# plain surface
surf = pygame.Surface((100,200))
surf.fill ('orange')
info_page = pygame.Surface((1200, 500))
info_page.fill ('DarkGray')
x = 100
player_direction = 1

# imports 
player_surf = [
    pygame.image.load(join('images3', '1.png')).convert_alpha(),
    pygame.image.load(join('images3', '2.png')).convert_alpha(),
    pygame.image.load(join('images3', '3.png')).convert_alpha(),
    pygame.image.load(join('images3', '4.png')).convert_alpha(),
    pygame.image.load(join('images3', '5.png')).convert_alpha(),
    pygame.image.load(join('images3', '6.png')).convert_alpha(),
    pygame.image.load(join('images3', '7.png')).convert_alpha(),
    pygame.image.load(join('images3', '8.png')).convert_alpha(),
    pygame.image.load(join('images3', '9.png')).convert_alpha(),
    pygame.image.load(join('images3', '10.png')).convert_alpha(),
    pygame.image.load(join('images3', '11.png')).convert_alpha(),
    pygame.image.load(join('images3', '12.png')).convert_alpha(),
    pygame.image.load(join('images3', '13.png')).convert_alpha(),
    pygame.image.load(join('images3', '14.png')).convert_alpha(),
    pygame.image.load(join('images3', '15.png')).convert_alpha(),
    pygame.image.load(join('images3', '16.png')).convert_alpha(),
    pygame.image.load(join('images3', '17.png')).convert_alpha(),
    pygame.image.load(join('images3', '18.png')).convert_alpha(),
]
current_icon = 0
player_rect = player_surf[current_icon].get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
player_direction = pygame.math.Vector2(1, 1)
player_speed = 300

star_surf = pygame.image.load(join('images3', 'star.png')).convert_alpha()
star_positions = [(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)) for i in range(20)]

pochacco1 = pygame.transform.scale(pygame.image.load(join('images3', 'pochacco1.png')).convert_alpha(), (300,250))
pochacco1_rect = pochacco1.get_frect(bottomleft = (10, WINDOW_HEIGHT - 20))


while running: 
    dt = clock.tick() / 1000
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                current_icon = (current_icon + 1) % len(player_surf)  # Switch between icons
            if event.key == pygame.K_TAB:
                show_info = not show_info  # Toggle info page visibility
            
    #draw the game
    custom_pink_color = (212, 96, 162)
    display_surface.fill(custom_pink_color)
    for pos in star_positions:
        display_surface.blit(star_surf, pos)

    #player movement
    new_position = pygame.math.Vector2(player_rect.center) + player_direction * player_speed * dt
    player_rect.center = new_position
    if player_rect.right >= WINDOW_WIDTH or player_rect.left <= 0:
        player_direction.x *= -1
    if player_rect.bottom >= WINDOW_HEIGHT or player_rect.top <= 0:
        player_direction.y *= -1

    # to prevent player from going beyond display surface
    if player_rect.bottom > WINDOW_HEIGHT: 
        player_rect.bottom = WINDOW_HEIGHT
        player_direction.y *= -1
    if player_rect.top < 0: 
        player_rect.top = 0 
        player_direction.y *= -1
    if player_rect.right > WINDOW_WIDTH:
        player_rect.right = WINDOW_WIDTH
        player_direction.x *= -1
    if player_rect.left < 0: 
        player_rect.left = 0 
        player_direction.x *= -1

    
    display_surface.blit(pochacco1, pochacco1_rect)
    text = font2.render("Press SPACE to change image, Press TAB for info", True, (200, 200, 200))
    display_surface.blit(text, (WINDOW_WIDTH / 2, WINDOW_HEIGHT - 100))
    display_surface.blit(player_surf[current_icon], player_rect)

    if show_info:
        display_surface.blit(info_page, (40, 100))
        text1 = font1.render("Bit of info, press tab to continue", True, (255, 255, 255))
        display_surface.blit(text1, (80, 150))
        text2 = font2.render("This took so much time to make. My first actual Python project and first time using Pygame module.", True, (255, 255, 255))
        display_surface.blit(text2, (80, 220))
        text3 = font2.render("Every component you see on this page is written by python code. I believe it is unusual for anyone to make", True, (255, 255, 255))
        display_surface.blit(text3, (80, 250))
        text4 = font2.render("something like this with pygame or python. All cutouts of my girlfriend are done in Adobe Illustrator.", True, (255, 255, 255))
        display_surface.blit(text4, (80, 280))
        text5 = font2.render("Will try to put this on a webpage using webassembly, pygbag, and bluehost web server as a gift for my gf.", True, (255, 255, 255))
        display_surface.blit(text5, (80, 310))
        text6 = font2.render("I got the inspiration to make this project while learning pygame, this experience has taught me a lot.", True, (255, 255, 255))
        display_surface.blit(text6, (80, 340))

    pygame.display.update()

pygame.quit()

