from src.Entity import Entity

class Obstacle(Entity):
    def __init__(self, name, position):
        super().__init__(name, position)

    def move(self):
        self.rect.centerx += 9
