import pygame
import constants
from logger import log_state, log_event
import player
import circleshape
import asteroid
import asteroidfield
import sys
import shot

def main():
    pygame.init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    asteroid.Asteroid.containers = (asteroids, updatable, drawable)
    player.Player.containers = (updatable, drawable)
    asteroidfield.AsteroidField.containers = (updatable)
    shot.Shot.containers = (shots, drawable, updatable)

    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    time = pygame.time.Clock()
    dt = 0.0
    field_obj = asteroidfield.AsteroidField()
    player_obj = player.Player(constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2)
    

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for thing in drawable:
            thing.draw(screen)
        updatable.update(dt)
        for thing in asteroids:
            if thing.collides_with(player_obj):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for stuff in shots:
                if stuff.collides_with(thing):
                    log_event("asteroid_shot")
                    stuff.kill()
                    thing.split()
        
        dt = time.tick(60) / 1000
        pygame.display.flip()
        

if __name__ == "__main__":
    main()
