import pygame
from src.Entity import Entity

class Player(Entity):
    def __init__(self, name, position):
        super().__init__(name, position)


    def move(self):
        dt = 0
        events = pygame.event.get()


        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.rect.top > 0:
            self.rect.centery -= 1
        elif keys[pygame.K_a] and self.rect.left > 0:
            self.rect.centerx -= 1
        elif keys[pygame.K_d] and self.rect.right < 780:
            self.rect.centerx += 1
