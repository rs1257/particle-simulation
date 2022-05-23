import pygame

from Particle import Particle
from Attractor import Attractor
import Constants

particle_array = []
attractor_array = []

def generate(number_of_particles, number_of_attractors):
    particle_index = 0
    while particle_index < number_of_particles:
        particle = Particle()
        particle_array.append(particle)
        particle_index += 1

    attractor_index = 0
    while attractor_index < number_of_attractors:
        if attractor_index >= number_of_attractors / 2:
            attractor = Attractor(True)
        else:
            attractor = Attractor()

        attractor_array.append(attractor)
        attractor_index += 1

def simulate():
    for particle in particle_array:
        particle.x += particle.vx
        particle.y += particle.vy
        if particle.x < 0:
            particle.x = 0 + 3
            particle.vx = 0
        if particle.x > Constants.SCREEN_X:
            particle.x = Constants.SCREEN_X - 3
            particle.vx = 0
        if particle.y < 0:
            particle.y = 0 + 3
            particle.vy = 0
        if particle.y > Constants.SCREEN_Y:
            particle.y = Constants.SCREEN_Y - 3
            particle.vy = 0

        for attractor in attractor_array:
            dx = (attractor.x - particle.x)
            dy = (attractor.y - particle.y)
            dsqu = (dx * dx) + (dy * dy) # keep as root as d^2 is used
            if dsqu < 250000:
                if dsqu < 1.0:
                    d = dsqu ** -1 / 2
                    xnorm = dx * attractor.g / d
                    ynorm = dy * attractor.g / d
                else:
                    xnorm = dx * attractor.g / dsqu
                    ynorm = dy * attractor.g / dsqu
                particle.vx += xnorm
                particle.vy += ynorm

def draw_all_entities(surface):
    for attractor in attractor_array:
        size = 1
        if attractor.g < 0:
            if attractor.g < -0.75:
                size = 2
            draw_attractors(surface, attractor.x, attractor.y, size, Constants.RED)
        else:
            if attractor.g > 1.5:
                size = 2
            draw_attractors(surface, attractor.x, attractor.y, size, Constants.GREEN)

    for particle in particle_array:
        draw_particles(surface, int(particle.x), int(particle.y))

def draw_particles(main_surface, x0, y0):
    for i in range(-2, 3):
        if i > -2 and i < 2:
            main_surface.set_at((x0 + i, y0 + 2), Constants.BLUE)
            main_surface.set_at((x0 + i, y0 - 2), Constants.BLUE)
        main_surface.set_at((x0 + i, y0), Constants.BLUE)
        main_surface.set_at((x0 + i, y0 - 1), Constants.BLUE)
        main_surface.set_at((x0 + i, y0 + 1), Constants.BLUE)


def draw_attractors(main_surface, x0, y0, size, color):
    if size == 1:
        for i in range(-3, 4):
            for j in range(-1, 2):
                main_surface.set_at((x0 + j, y0 + i), color)
                main_surface.set_at((x0 + i, y0 + j), color)

        main_surface.set_at((x0 - 2, y0 + 2), color)
        main_surface.set_at((x0 - 2, y0 - 2), color)
        main_surface.set_at((x0 + 2, y0 - 2), color)
        main_surface.set_at((x0 + 2, y0 + 2), color)
    else:
        for i in range(-4, 5):
            for j in range(-2, 3):
                main_surface.set_at((x0 + j, y0 + i), color)
                main_surface.set_at((x0 + i, y0 + j), color)

        main_surface.set_at((x0 - 3, y0 + 3), color)
        main_surface.set_at((x0 - 3, y0 - 3), color)
        main_surface.set_at((x0 + 3, y0 - 3), color)
        main_surface.set_at((x0 + 3, y0 + 3), color)

def main():
    """ Set up the game and run the main game loop """
    pygame.init()      # Prepare the pygame module for use

    # Create surface of (width, height), and its window.
    main_surface = pygame.display.set_mode((Constants.SCREEN_X, Constants.SCREEN_Y))
    clock = pygame.time.Clock()

    generate(Constants.NUMBER_OF_PARTICLES, Constants.NUMBER_OF_ATTRACTORS)
    count = 0
    while True:

        clock.tick(60)
        if count == 25:
            print("clock.get_fps", clock.get_fps())
            count = 0

        count += 1
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break

        # We draw everything from scratch on each frame.
        # So first fill everything with the background color
        main_surface.fill((0, 0, 0))

        try:
            simulate()
            draw_all_entities(main_surface)
        except Exception as e:
            print(e)

        # Now the surface is ready, tell pygame to display it!
        pygame.display.flip()

    pygame.quit()     # Once we leave the loop, close the window.


if __name__ == '__main__':
    main()
