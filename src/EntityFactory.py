import random

from src.Background import Background
from src.Obstacle import Obstacle
from src.Player import Player
from src.constants import SCREEN_HEIGHT, POSITION_LIST


class EntityFactory:
    @staticmethod
    def get_entity(entity_name: str):
        match entity_name:
            case "Player":
                return Player("Player", (350, SCREEN_HEIGHT - 100))
            case "Car01":
                return Obstacle("Car01", random.choice(POSITION_LIST))
            case "Car02":
                return Obstacle("Car02", random.choice(POSITION_LIST))
            case "Car03":
                return Obstacle("Car03", random.choice(POSITION_LIST))
            case "Road01":
                return Background("Road01", (0,0))
