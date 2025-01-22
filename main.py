import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()

    player = Player( (SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) )
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for updatee in updatable:
            updatee.update(dt)
        for asteroid in asteroids:
            if player.collision(asteroid):
                print("Game over!")
                sys.exit()
        for drawee in drawable:
            drawee.draw(screen)
        pygame.display.flip()
        dt = (clock.tick(60)) / 1000

if __name__ == "__main__":
    main()