from abc import ABC, abstractmethod
import pygame

class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.speed = 0
        self.surf= pygame.image.load("./assets/"+name+".png").convert_alpha()
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        

    @abstractmethod
    def move(self):
        pass

    def has_collide(self, rect):
        pass

