import random
import pygame
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface

from src.Entity import Entity
from src.EntityFactory import EntityFactory
from src.Score import Score
from src.constants import SCREEN_WIDTH, SCREEN_HEIGHT, OBSTACLE_EVENT, OBSTACLE_LIST, SPAWN_TIME, OBSTACLE_SPEED


class Game:
    def __init__(self, highscore):
        pygame.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.entity_list: list[Entity] = []
        self.obstacle_list: list[Entity] = []

        self.entity_list.append(EntityFactory.get_entity("Road001"))
        self.player = EntityFactory.get_entity("Player")
        self.entity_list.append(self.player)
        self.hud_font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=20)
        self.game_over_font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=50)

        self.game_over = False
        # SOLUÇÃO: Guardamos a velocidade atual em um atributo global do Game
        self.current_obstacle_speed = OBSTACLE_SPEED



        self.score = 0
        self.level = 1
        self.last_player_y = self.player.rect.y
        self.highscore = highscore
        self.score_system = Score(highscore)
        self.last_player_y = self.player.rect.y

        pygame.time.set_timer(OBSTACLE_EVENT, SPAWN_TIME)

    def reset_game(self):
        print("Reiniciando o jogo...")
        # 1. Limpa os obstáculos antigos das listas
        self.obstacle_list.clear()

        # 2. Reconstrói a lista de entidades apenas com a estrada e o player
        self.entity_list = []
        self.entity_list.append(EntityFactory.get_entity("Road001"))

        # 3. Reseta a posição do jogador para o início
        self.player.rect.bottom = SCREEN_HEIGHT - 20
        self.player.rect.centerx = SCREEN_WIDTH // 2
        self.entity_list.append(self.player)

        # 4. Reseta a velocidade dos obstáculos para o padrão
        self.current_obstacle_speed = OBSTACLE_SPEED

        # 5. Desativa o estado de Game Over
        self.game_over = False

    def draw_hud(self):

        score_surf = self.hud_font.render(f"SCORE: {self.score}", True, "White")
        self.screen.blit(score_surf, (20, 20))  # Desenha no canto superior esquerdo

        display_highscore = max(self.score, self.highscore)
        hscore_surf = self.hud_font.render(f"HIGHSCORE: {display_highscore}", True, "Red")
        self.screen.blit(hscore_surf, (SCREEN_WIDTH // 2 - 70, 20))
        # Texto da Fase/Level
        level_surf = self.hud_font.render(f"STAGE: {self.level}", True, "Yellow")
        # Desenha no canto superior direito (largura da tela menos o tamanho do texto)
        self.screen.blit(level_surf, (SCREEN_WIDTH - 150, 20))

    def check_win_condition(self):
        # Se o topo do retângulo do jogador passar do topo da tela (0)
        if self.player.rect.top <= 0:
            # 1. Retorna o jogador para o início
            self.player.rect.bottom = SCREEN_HEIGHT - 20
            self.player.rect.centerx = SCREEN_WIDTH // 2
            self.last_player_y = self.player.rect.y
            # 2. Incrementa a velocidade global do jogo permanentemente
            self.current_obstacle_speed += 2

            self.score_system.advance_level()

            # 3. Atualiza os obstáculos que JÁ estão na tela
            for obstacle in self.obstacle_list:
                obstacle.speed = self.current_obstacle_speed

    def run(self):
        running = True
        clock = pygame.time.Clock()

        while running:
            clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    return

                if event.type == pygame.KEYDOWN:
                    # Se o jogo acabou e o jogador apertou ENTER
                    if self.game_over and event.key == pygame.K_RETURN:
                        self.reset_game()
                        return self.score_system.current_score


                if event.type == OBSTACLE_EVENT and not self.game_over:
                    choice = random.choice(OBSTACLE_LIST)
                    new_obstacle = EntityFactory.get_entity(choice)
                    # SOLUÇÃO: Injeta a velocidade atualizada no novo obstáculo criado
                    new_obstacle.speed = self.current_obstacle_speed
                    self.entity_list.append(new_obstacle)
                    self.obstacle_list.append(new_obstacle)

            # 1. LIMPAR A TELA
            self.screen.fill((0, 0, 0))

            # 2. ATUALIZAR E DESENHAR ENTIDADES
            for entity in self.entity_list:
                self.screen.blit(entity.surf, entity.rect)
                if not self.game_over:
                    entity.move()

            if not self.game_over and self.player.rect.y < self.last_player_y:
                # Se ele subiu mais que a altura de um "passo" (ex: 20 pixels)
                if self.last_player_y - self.player.rect.y >= 25:
                    self.score_system.add_points(25)
                    self.last_player_y = self.player.rect.y

            # CORREÇÃO: Tirado de dentro do loop 'for entity' para rodar apenas uma vez por frame
            if not self.game_over:
                self.check_win_condition()

            # 3. CHECAR COLISÕES
            if not self.game_over:
                for obstacle in self.obstacle_list:
                    if self.player.rect.colliderect(obstacle.rect):
                        self.game_over = True
                        if self.player in self.entity_list:
                            self.entity_list.remove(self.player)

            self.score_system.draw(self.screen)

            # 4. DESENHAR TELA DE GAME OVER
            if self.game_over:
                text_surf: Surface = self.game_over_font.render("Game Over", True, "Red").convert_alpha()
                text_rect: Rect = text_surf.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
                self.screen.blit(source=text_surf, dest=text_rect)

                restart_font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=30)
                restart_surf = restart_font.render("Pressione ENTER para reiniciar ou ESC para sair", True, "White").convert_alpha()
                restart_rect = restart_surf.get_rect(center=(SCREEN_WIDTH // 2, (SCREEN_HEIGHT // 2) + 60))
                self.screen.blit(source=restart_surf, dest=restart_rect)


            pygame.display.flip()