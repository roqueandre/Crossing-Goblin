
import pygame


class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.surf = pygame.image.load("./assets/title_screen.png").convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)


    def run(self):
        running = True
        while running:
            self.screen.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "Crossing Goblin", (255,255,255), (380,280))

            self.menu_text(25, "NEW GAME", (255, 255, 255), (380, 380))
            self.menu_text(25, "SCORE", (255, 255, 255), (380, 340))
            self.menu_text(25, "INSTRUCTIONS", (255, 255, 255), (380, 340))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()


                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        pass




    def menu_text(self, text_size, text, color, position):
        text_font = pygame.font.SysFont(name="Comic Sans", size=text_size)
        text_surf = text_font.render(text, True, color).convert_alpha()
        text_rect = text_surf.get_rect(center=position)
        self.screen.blit(source=text_surf, dest=text_rect)

pygame.init()
screen = pygame.display.set_mode((800, 600))


menu = Menu(screen)