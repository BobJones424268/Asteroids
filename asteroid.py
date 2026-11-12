import circleshape
import constants
import pygame
from logger import log_state, log_event
import random

class Asteroid(circleshape.CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            new_veolicty = self.velocity.rotate(angle)
            newer_veolicty = self.velocity.rotate(-angle)
            new_rad = self.radius - constants.ASTEROID_MIN_RADIUS
            asteroid_one = Asteroid(self.position.x, self.position.y, new_rad)
            asteroid_two = Asteroid(self.position.x, self.position.y, new_rad)
            asteroid_one.velocity = new_veolicty * 1.2
            asteroid_two = newer_veolicty * 1.2

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, constants.LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt