import random

import pygame

from src.Entity import Entity
from src.EntityFactory import EntityFactory
from src.constants import SCREEN_WIDTH, SCREEN_HEIGHT, OBSTACLE_EVENT, OBSTACLE_LIST


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.entity_list: list[Entity] = []
        self.entity_list.append(EntityFactory.get_entity("Player"))



    def run(self):
        running = True
        clock = pygame.time.Clock()
        clock.tick(60)

        while running:
            self.screen.fill("navy blue")


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()

                if event.type == OBSTACLE_EVENT:
                    choice = random.choice(OBSTACLE_LIST)
                    self.entity_list.append(EntityFactory.get_entity(choice))

            for entity in self.entity_list:
                self.screen.blit(entity.surf, entity.rect)
                entity.move()



                pygame.display.flip()





game = Game()
game.run()