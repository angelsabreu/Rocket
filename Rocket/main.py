import pygame
from pygame import QUIT

pygame.init()

HEIGHT = 500
WIDTH = 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))

img = pygame.image.load("galaxy_bg.png")
image = pygame.transform.scale(img,(WIDTH, HEIGHT))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("rocket.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (70,100))
        self.rect = self.image.get_rect()

    def update(self, pressed_keys):
        if pressed_keys[pygame.K_UP]:
            self.rect.move_ip(0,-5)
        if pressed_keys[pygame.K_DOWN]:
            self.rect.move_ip(0,5)
        if pressed_keys[pygame.K_LEFT]:
            self.rect.move_ip(-5,0)
        if pressed_keys[pygame.K_RIGHT]:
            self.rect.move_ip(5,0)
        
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT

sprites = pygame.sprite.Group()

def startgame():
    player = Player()
    sprites.add(player)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
        
        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)

        screen.blit(image,(0,0))

        sprites.draw(screen)

        pygame.display.update()

startgame()