import pygame

class CircleShape(pygame.sprite.Sprite):

    def __init__(self, x, y, raidus):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = raidus

    def draw(self, screen):
        raise NotImplementedError()
        
    def update(self, dt):
        # sub-classes must override
        raise NotImplementedError()
    

    
    def collides(self, other):
        distance = self.position.distance_to(other.position)
        return distance <= self.radius + other.radius