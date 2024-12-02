import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = radius

    
    def draw(self, surface):
        pygame.draw.circle(surface, (255, 255, 255), self.position, self.radius, width=2)

    def update(self, dt):
        self.position = (self.velocity * dt) + self.position

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            velocity1 = self.velocity.rotate(random_angle) * 1.2
            velocity2 = self.velocity.rotate(-random_angle) * 1.2
            old_radius = self.radius
            new_radius = old_radius - ASTEROID_MIN_RADIUS
            asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid.velocity = velocity1
            asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid.velocity = velocity2
