import pygame
from pygame.rect import Rect
from pygame.surface import Surface

pygame.init()
pygame.font.init()


class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.surf = pygame.image.load("./assets/title_screen.png").convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

        self.font_title = pygame.font.SysFont(name="Lucida Sans Typewriter", size=120)
        self.font_options = pygame.font.SysFont(name="Lucida Sans Typewriter", size=25)

        # --- NOVA LOGICA DE SELEÇÃO ---
        # Lista com os textos das opções
        self.options = ["NEW GAME", "SCORE", "INSTRUCTIONS"]
        # Índice da opção atualmente selecionada (0 = NEW GAME)
        self.selected_index = 0

    def run(self):
        running = True
        clock = pygame.time.Clock()

        while running:
            clock.tick(60)

            # Desenha o fundo
            self.screen.blit(source=self.surf, dest=self.rect)

            # Desenha o título do jogo
            self.draw_text(self.font_title, "Crossing Goblin", (255, 255, 255), (400, 150))

            # --- DESENHO DINÂMICO DAS OPÇÕES ---
            # Vamos passar por cada opção e verificar se ela é a selecionada
            for index, option_text in enumerate(self.options):
                # Se o índice for o atual selecionado, pinta de Amarelo (ou a cor que preferir)
                if index == self.selected_index:
                    color = (255, 215, 0)  # Dourado/Amarelo
                    text_to_render = f"> {option_text} <"  # Opcional: adiciona setinhas
                else:
                    color = (255, 255, 255)  # Branco para as outras
                    text_to_render = option_text

                # Calcula a altura (Y) dinamicamente para cada opção não ficar em cima da outra
                position_y = 300 + (index * 50)

                self.draw_text(self.font_options, text_to_render, color, (150, position_y))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    # Seta para BAIXO: avança no menu
                    if event.key == pygame.K_DOWN:
                        self.selected_index = (self.selected_index + 1) % len(self.options)

                    # Seta para CIMA: volta no menu
                    if event.key == pygame.K_UP:
                        self.selected_index = (self.selected_index - 1) % len(self.options)

                    # ENTER: Executa a ação baseada no que está selecionado
                    if event.key == pygame.K_RETURN:
                        if self.selected_index == 0:  # NEW GAME
                            print("Iniciando o Jogo...")
                            running = False  # Fecha o menu para o main.py abrir o Game()
                        elif self.selected_index == 1:  # SCORE
                            print("Abrindo placar (Ainda não implementado)")
                        elif self.selected_index == 2:  # INSTRUCTIONS
                            print("Abrindo instruções (Ainda não implementado)")

            pygame.display.flip()

    def draw_text(self, font, text, color, position):
        text_surf: Surface = font.render(text, True, color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=position)
        self.screen.blit(source=text_surf, dest=text_rect)