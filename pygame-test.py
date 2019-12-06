import pygame

pygame.init()

black = (255,255,255)

X = 640
Y = 480

display_surface = pygame.display.set_mode((X,Y))
pygame.display.set_caption('Imagem')

imagem = pygame.image.load(r'ico-x.png')

while True:
    display_surface.fill(black)
    display_surface.blit(imagem,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             quit()
    pygame.display.update()