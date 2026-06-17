import pygame
from src.Entity import Entity
from src.constants import PLAYER_SPEED


class Player(Entity):
    def __init__(self, name, position):
        super().__init__(name, position)


    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.rect.top > 0:
            self.rect.centery -= PLAYER_SPEED
        elif keys[pygame.K_s] and self.rect.bottom < 600:
            self.rect.centery += PLAYER_SPEED
        elif keys[pygame.K_a] and self.rect.left > 0:
            self.rect.centerx -= PLAYER_SPEED
        elif keys[pygame.K_d] and self.rect.right < 800:
            self.rect.centerx += PLAYER_SPEED

    def has_collide(self, sprite):
        return self.rect.colliderect(sprite.rect)

    def return_to_start(self):
        pass