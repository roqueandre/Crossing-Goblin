from src.Player import Player
from src.constants import SCREEN_WIDTH, SCREEN_HEIGHT


class EntityFactory:
    @staticmethod
    def get_entity(entity_name: str):
        match entity_name:
            case "Player":
                return Player("Player", (350, SCREEN_HEIGHT - 100))