import random

import pygame
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface

from src.Entity import Entity
from src.EntityFactory import EntityFactory
from src.constants import SCREEN_WIDTH, SCREEN_HEIGHT, OBSTACLE_EVENT, OBSTACLE_LIST, SPAWN_TIME


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.entity_list: list[Entity] = []
        self.obstacle_list: list[Entity] = []
        self.entity_list.append(EntityFactory.get_entity("Road001"))
        self.player = EntityFactory.get_entity("Player")
        self.entity_list.append(self.player)
        pygame.time.set_timer(OBSTACLE_EVENT, SPAWN_TIME)



    def run(self):
        running = True
        clock = pygame.time.Clock()
        clock.tick(60)

        while running:



            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

                if event.type == OBSTACLE_EVENT:
                    choice = random.choice(OBSTACLE_LIST)
                    new_obstacle = EntityFactory.get_entity(choice)
                    self.entity_list.append(new_obstacle)
                    self.obstacle_list.append(new_obstacle)



            for entity in self.entity_list:
                self.screen.blit(entity.surf, entity.rect)
                entity.move()

            for obstacle in self.obstacle_list:
                if self.player.rect.colliderect(obstacle.rect):
                    text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=24)
                    text_surf: Surface = text_font.render("Game Over", True, "White").convert_alpha()
                    text_rect: Rect = text_surf.get_rect(left=400,top=300)
                    self.screen.blit(source=text_surf, dest=text_rect)
                    self.player.kill()







            pygame.display.flip()




