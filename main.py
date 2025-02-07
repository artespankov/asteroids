import pygame
from constants import *
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable, )
    Shot.containers = (shots, updatable, drawable)


    player = Player(x=SCREEN_WIDTH//2, y=SCREEN_HEIGHT//2)
    af = AsteroidField()

    clock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill('black')
        drawable.draw(screen)
        updatable.update(dt)


        for asteroid in asteroids:
            if asteroid.collides(player):
                print("Game over!")
                sys.exit(0)
        pygame.display.flip()
        dt = clock.tick(60) / 1000  # convert ms -> s

if __name__ == "__main__":
    main()