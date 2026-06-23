import pygame

from src.Game import Game
from src.Menu import Menu

screen = pygame.display.set_mode(size=(800, 600))
menu = Menu(screen)

highscore = 0

while True:
    menu.run()
    game = Game(highscore)

    last_score = game.run()

    if last_score is not None and last_score > highscore:
        highscore = last_score