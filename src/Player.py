import pygame
from src.Entity import Entity



class Player(Entity):
    def __init__(self, name, position):
        super().__init__(name, position)
        self.speed = 2

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.rect.top > 0:
            self.rect.centery -= self.speed
        elif keys[pygame.K_s] and self.rect.bottom < 600:
            self.rect.centery += self.speed
        elif keys[pygame.K_a] and self.rect.left > 0:
            self.rect.centerx -= self.speed
        elif keys[pygame.K_d] and self.rect.right < 800:
            self.rect.centerx += self.speed

    def has_collide(self, sprite):
        return self.rect.colliderect(sprite.rect)

    def return_to_start(self):
        pass