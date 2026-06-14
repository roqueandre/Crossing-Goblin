from abc import ABC, abstractmethod
import pygame

class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.position = position
        self.surf= pygame.image.load("./assets/"+name+".png").convert_alpha()
        #self.surf = pygame.transform.scale(self.original_image, (100,100))
        self.rect = self.surf.get_rect(left=position[0], top=position[1])

    @abstractmethod
    def move(self):
        pass