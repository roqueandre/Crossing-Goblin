from src.Entity import Entity

class Obstacle(Entity):
    def __init__(self, name, position):
        super().__init__(name, position)
        self.speed = 2

    def move(self):
        self.rect.centerx += self.speed
