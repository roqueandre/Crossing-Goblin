import random

from src.Background import Background
from src.Obstacle import Obstacle
from src.Player import Player
from src.constants import  POSITION_LIST, START_POSITION_PLAYER


class EntityFactory:
    @staticmethod
    def get_entity(entity_name: str):
        match entity_name:
            case "Player":
                return Player("Player", START_POSITION_PLAYER)
            case "Car01":
                return Obstacle("Car01", random.choice(POSITION_LIST))
            case "Car02":
                return Obstacle("Car02", random.choice(POSITION_LIST))
            case "Car03":
                return Obstacle("Car03", random.choice(POSITION_LIST))
            case "Road001":
                return Background("Road001", (0,0))
        return None
