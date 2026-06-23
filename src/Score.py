import pygame
from pygame.surface import Surface
from src.constants import SCREEN_WIDTH, FONT_OPTIONS


class Score:
    def __init__(self, highscore=0):
        # Inicializa o sistema de fontes caso não tenha sido feito antes
        pygame.font.init()
        self.hud_font = pygame.font.Font(FONT_OPTIONS, size=25)

        # Variáveis de controle de pontos
        self.current_score = 0
        self.highscore = highscore
        self.level = 1

    def add_points(self, points: int):
        """Adiciona pontos ao placar atual"""
        self.current_score += points

    def advance_level(self):
        """Avança de fase e dá o bônus de 100 pontos"""
        self.level += 1
        self.add_points(100)

    def draw(self, screen: Surface):
        """Desenha todas as informações de pontos na tela"""
        # Texto do Score Atual (Canto Esquerdo)
        score_surf = self.hud_font.render(f"SCORE: {self.current_score}", True, "Grey")
        screen.blit(score_surf, (20, 20))

        # Texto do Highscore (Centro) - Brilha em tempo real se passar o recorde antigo
        display_highscore = max(self.current_score, self.highscore)
        high_surf = self.hud_font.render(f"HI-SCORE: {display_highscore}", True, "Red")
        screen.blit(high_surf, (SCREEN_WIDTH // 2 - 70, 20))

        # Texto da Fase/Level (Canto Direito)
        level_surf = self.hud_font.render(f"STAGE: {self.level}", True, "Green")
        screen.blit(level_surf, (SCREEN_WIDTH - 150, 20))