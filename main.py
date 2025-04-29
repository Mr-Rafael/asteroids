import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    game_display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable)

    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT /2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for updatable_object in updatable:
            updatable_object.update(dt)

        for asteroid in asteroids:
            if asteroid.check_collision(player):
                print("Game over!")
                return
            
            for shot in shots:
                if asteroid.check_collision(shot):
                    asteroid.kill()
                    shot.kill()

        game_display.fill("black")
        for drawable_object in drawable:
            drawable_object.draw(game_display)
        pygame.display.flip()
        dt = game_clock.tick(30)


if __name__ == "__main__":
    main()