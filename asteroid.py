import pygame
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y , radius):
        super().__init__(x, y, radius)

    def draw(self, surface):
        pygame.draw.circle(surface, "white", self.position, self.radius)

    def update(self, dt):
        forward = pygame.Vector2(0, 1)
        self.position += forward * ASTEROID_MOVE_SPEED * dt
