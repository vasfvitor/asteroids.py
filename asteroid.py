import pygame
import random
from constants import *
from circleshape import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        vectorA = self.velocity.rotate(angle)
        vectorB = self.velocity.rotate(-angle)

        newRadius = self.radius - ASTEROID_MIN_RADIUS

        chunkA = Asteroid(self.position.x, self.position.y, newRadius)
        chunkB = Asteroid(self.position.x, self.position.y, newRadius)

        chunkA.velocity = vectorA * 1.2
        chunkB.velocity = vectorB * 1.2
