import sys
import pygame

from constants import *
from player import *
from circleshape import *
from asteroidfield import *
from shot import *


def main():
    pygame.init()
    pygame.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    clock = pygame.time.Clock()
    dt = 0
    all_asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    all_shots = pygame.sprite.Group()
    Player.containers = (updatable,drawable)
    Asteroid.containers = (all_asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (all_shots, drawable, updatable)

    main_player = Player((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2))
    field = AsteroidField()
        
    while pygame.get_init():

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)

        for asteroid_object in all_asteroids:
            if asteroid_object.is_colliding(main_player):
                print("Game Over!")
                sys.exit()

        for asteroid_object in all_asteroids:
            for shot_bullet in all_shots:
                if asteroid_object.is_colliding(shot_bullet):
                    asteroid_object.split()
                    shot_bullet.kill()

        pygame.screen.fill("#000000")
        for element in drawable:
            element.draw(pygame.screen)
        pygame.display.flip() 

        

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
