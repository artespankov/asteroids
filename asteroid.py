from circleshape import CircleShape
import pygame
from constants import ASTEROID_MIN_RADIUS
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y, radius)
        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, "white", (self.radius, self.radius), self.radius, width=2)
        self.rect = self.image.get_rect(center=(x, y))

    def update(self, dt):
        self.position += self.velocity * dt
        self.rect.center = self.position


    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(20, 50)

        self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_velocity = self.velocity.rotate(random_angle)
        
        smaller_first_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        
        # make it faster by sx
        smaller_first_asteroid.velocity = new_velocity * 1.2

        smaller_second_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        smaller_second_asteroid.velocity = -new_velocity * 1.2