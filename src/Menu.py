import pygame
from pygame.rect import Rect
from pygame.surface import Surface

from src.constants import FONT_OPTIONS, FONT_TITLE

pygame.init()
pygame.font.init()


class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.surf = pygame.image.load("./assets/title_screen.png").convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)
        self.font_title = pygame.font.Font(FONT_TITLE, size=100)
        self.font_options = pygame.font.Font(FONT_OPTIONS, size=25)
        self.font_title2 = pygame.font.Font(FONT_TITLE, size=97)

        # --- SELETOR DO MENU ---
        self.options = ["NEW GAME", "INSTRUCTIONS"]
        self.selected_index = 0

        # Controla se estamos vendo os comandos
        self.showing_instructions = False



    def run(self):
        running = True
        clock = pygame.time.Clock()
        pygame.mixer_music.load("./assets/sounds/main_theme_01.wav")
        pygame.mixer_music.play(-1)

        while running:
            clock.tick(60)



            self.screen.blit(source=self.surf, dest=self.rect)
            # SE ESTIVER NA TELA DE INSTRUÇÕES
            if self.showing_instructions:
                self.draw_background_box(350, 200, 240, (400, 355))
                self.draw_text(self.font_title, "COMANDOS", (255, 255, 255), (400, 150))

                # Lista de comandos para exibir na tela
                self.draw_text(self.font_options, "W - Mover para Cima", (255, 215, 0), (400, 280))
                self.draw_text(self.font_options, "S - Mover para Baixo", (255, 215, 0), (400, 330))
                self.draw_text(self.font_options, "A - Mover para Esquerda", (255, 215, 0), (400, 380))
                self.draw_text(self.font_options, "D - Mover para Direita", (255, 215, 0), (400, 430))

                self.draw_text(self.font_options, "Pressione ESC ou ENTER para voltar", (255, 255, 255), (400, 520))

            # SE ESTIVER NO MENU PRINCIPAL
            else:
                self.draw_text(self.font_title, "Crossing Goblin", (0, 86, 0), (400, 160))
                self.draw_text(self.font_title2, "Crossing Goblin", (255, 255, 255), (400, 150))
                self.draw_text(self.font_options, "Pressione ENTER para confirmar", (255, 255, 255), (400, 520))

                self.draw_background_box(300, 100, 240, (400, 300))
                for index, option_text in enumerate(self.options):
                    if index == self.selected_index:
                        color = (255, 215, 0)  # Dourado/Amarelo
                        text_to_render = f"> {option_text} <"

                    else:
                        color = (255, 255, 255)  # Branco
                        text_to_render = option_text

                    position_y = 280 + (index * 50)
                    self.draw_text(self.font_options, text_to_render, color, (400, position_y))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    # Se o jogador estiver vendo as instruções, tecla ENTRE ou ESC fecha a tela
                    if self.showing_instructions:
                        if event.key in (pygame.K_ESCAPE, pygame.K_RETURN):
                            self.showing_instructions = False
                        continue

                    # Navegação do menu principal
                    if event.key == pygame.K_DOWN:
                        self.selected_index = (self.selected_index + 1) % len(self.options)

                    if event.key == pygame.K_UP:
                        self.selected_index = (self.selected_index - 1) % len(self.options)

                    if event.key == pygame.K_RETURN:
                        if self.selected_index == 0:  # NEW GAME
                            running = False
                        elif self.selected_index == 1:  # INSTRUCTIONS
                            self.showing_instructions = True  # Altera o estado para exibir a tela

            pygame.display.flip()

    def draw_text(self, font, text, color, position):
        text_surf: Surface = font.render(text, True, color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=position)
        self.screen.blit(source=text_surf, dest=text_rect)

    def draw_background_box(self, width, height, alpha, position):
        """Cria e desenha uma caixa retangular semitransparente na tela"""
        box_surf = Surface((width, height)).convert_alpha()
        box_surf.fill((40, 86, 10))
        box_surf.set_alpha(alpha)
        box_rect = box_surf.get_rect(center=position)
        self.screen.blit(box_surf, box_rect)