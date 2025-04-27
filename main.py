import pygame
from constants import *
from player import *

def main():
    pygame.init()
    game_display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT /2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        player.update(dt)
        game_display.fill("black")
        player.draw(game_display)
        pygame.display.flip()
        dt = game_clock.tick(30)


if __name__ == "__main__":
    main()