from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN
import pygame
from shot import Shot

class Player(CircleShape):

    def __init__(self, x, y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0
        self.image = pygame.Surface((PLAYER_RADIUS * 3, PLAYER_RADIUS * 3), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=(x, y))
        self.update_image()
        self.timer = 0

    def update_image(self):
        """Redraws the player triangle on the image surface"""
        self.image.fill((0, 0, 0, 0))  # Clear the surface
        pygame.draw.polygon(self.image, "white", self.triangle(), 2)

    def triangle(self):
        center = pygame.Vector2(self.image.get_width()/2, self.image.get_height()/2)
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = center + forward * self.radius
        b = center - forward * self.radius - right
        c = center - forward * self.radius + right
        return [a, b, c]
    

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
        self.update_image()

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)

        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_w]:
            self.move(dt)

        if keys[pygame.K_s]:
            self.move(-dt)

        if keys[pygame.K_SPACE]:
            self.shot()
        

        self.rect.center = (self.position.x, self.position.y)
        self.timer -= dt



    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shot(self):
        if self.timer <= 0 :
            shot = Shot(self.position.x, self.position.y)
            shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
            self.containers[0].add(shot)
            self.timer = PLAYER_SHOOT_COOLDOWN