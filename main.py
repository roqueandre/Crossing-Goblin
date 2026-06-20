import pygame

from src.Game import Game
from src.Menu import Menu

# Configuração da tela
tela = pygame.display.set_mode(size=(800, 600))
menu = Menu(tela)

# Loop Principal do Jogo
while True:
    # 1. Roda o menu. O código vai ficar preso aqui até você apertar ENTER
    print("Abrindo o Menu")
    menu.run()

    # 2. Quando o ENTER for apertado, o menu fecha e o código vem para cá.
    # Instanciamos o jogo para começar do zero:
    print("Menu fechou")
    game = Game()

    # 3. Roda o jogo. O código fica preso aqui até o jogo fechar ou dar Game Over
    print("Rodou o Game")
    game.run()