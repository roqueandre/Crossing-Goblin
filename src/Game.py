import pygame

from src.Entity import Entity
from src.EntityFactory import EntityFactory
from src.constants import SCREEN_WIDTH, SCREEN_HEIGHT


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.entity_list: list[Entity] = []
        self.entity_list.append(EntityFactory.get_entity("Player"))



    def run(self):
        running = True
        clock = pygame.time.Clock()
        dt = 0
        position = pygame.Vector2(self.screen.get_width() / 2, self.screen.get_height() - 25)

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
            self.screen.fill("navy blue")

            for entity in self.entity_list:
                self.screen.blit(entity.surf, entity.rect)
                entity.move()


            pygame.display.flip()
            #dt = clock.tick(60) /1000



game = Game()
game.run()