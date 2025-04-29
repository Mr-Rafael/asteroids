import pygame
from constants import *
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y, rotation):
        super().__init__(x, y, SHOT_RADIUS)
        self.rotation = rotation

    def draw(self, surface):
        pygame.draw.circle(surface, "white", self.position, self.radius)

    def update(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * SHOT_MOVE_SPEED * dt