import pygame
import random

small_rect = (300, 200, 150, 90)
some_color = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
some = (255, 255, 0)
red = (255, 0, 0)
particle_array = []
attractor_array = []
# wall_array = []
SCREEN_X = 1000
SCREEN_Y = 600
np = 2500
na = 10
# nw = 3


def drawline(surface, x0, y0, x1, y1, another_color):
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    if x0 < x1:
        sx = 1
    else:
        sx = -1

    if y0 < y1:
        sy = 1
    else:
        sy = -1
    err = dx - dy

    while True:
        if x0 == x1 and y0 == y1:
            return

        e2 = 2 * err
        if e2 > -dy:
            # overshot in the y direction
            err = err - dy
            x0 = x0 + sx
        if e2 < dx:
            # overshot in the x direction
            err = err + dx
            y0 = y0 + sy
        surface.set_at((x0, y0), another_color)


class Particle:
    def __init__(self):
        self.x = random.randint(0 + 2, SCREEN_X - 2)
        self.y = random.randint(0 + 2, SCREEN_Y - 2)
        self.vx = 0
        self.vy = 0


class Attractor:
    def __init__(self, neg=False):
        self.x = random.randint(0 + 7, SCREEN_X - 7)
        self.y = random.randint(0 + 7, SCREEN_Y - 7)
        if neg:
            self.g = -1 * random.uniform(0.5, 1.0)
        else:
            self.g = random.uniform(1.0, 2.0)


'''
class Wall:
    def __init__(self):
        self.x = random.randint(0 + 2, SCREEN_X - 2)
        self.y = random.randint(0 + 2, SCREEN_Y - 2)
        orientation = random.randint(0,1)
        if (orientation):
            self.thickness = random.randint(40, 200)
            self.length = random.randint(20, 100)
        else:
            self.thickness = random.randint(20, 100)
            self.length = random.randint(40, 200)
'''


def generate(nop, noa):
    i = 0
    while i < nop:
        p = Particle()
        particle_array.append(p)
        i = i + 1

    i = 0
    while i < noa:
        if i >= noa/2:
            a = Attractor(True)
        else:
            a = Attractor()
        attractor_array.append(a)
        i = i + 1

    '''
    i = 0
    while (i < now):
        w = wall()
        warray.append(w)
        i = i + 1
    '''


def simulate():
    for p in particle_array:
        # lastx = p.x
        # lasty = p.y
        p.x += p.vx
        p.y += p.vy
        if p.x < 0:
            p.x = 0 + 3
            p.vx = 0
        if p.x > SCREEN_X:
            p.x = SCREEN_X - 3
            p.vx = 0
        if p.y < 0:
            p.y = 0 + 3
            p.vy = 0
        if p.y > SCREEN_Y:
            p.y = SCREEN_Y - 3
            p.vy = 0
        '''for w in warray:
         #top and bottom now work
         if ((p.x >= w.x and p.x <= w.x + w.thickness) and (p.y >= w.y and p.y <= w.y + w.length)):
             if (lastx >= w.x and lastx <= w.x + w.thickness and lasty >= w.y):
                     p.y = w.y + w.length
                     p.vy = 0
             elif (lastx >= w.x and lastx <= w.x + w.thickness and lasty <= w.y + w.length):
                     p.y = w.y
                     p.vy = 0
             elif ((lasty >= w.y and lasty <= w.y + w.length)):
                 if (lasty >= w.y):
                     p.x = w.x + w.thickness
                     p.vx = 0
                 else:
                     p.x = w.x
                     p.vx = 0
                '''  # x in so x never changes but y does
        for a in attractor_array:
            dx = (a.x - p.x)
            dy = (a.y - p.y)
            dsqu = (dx * dx) + (dy * dy) # keep as root as d^2 is used
            if dsqu < 250000: 
                if dsqu < 1.0:
                    d = dsqu ** -1 / 2
                    xnorm = dx * a.g / d
                    ynorm = dy * a.g / d
                else:
                    xnorm = dx * a.g / dsqu
                    ynorm = dy * a.g / dsqu
                p.vx += xnorm
                p.vy += ynorm


def draw_all(surface):
    """
    for w in warray:
        draw_walls(surface, w.x, w.y, w.thickness, w.length, some)
    """

    for a in attractor_array:
        size = 1
        if a.g < 0:
            if a.g < -0.75:
                size = 2
            smalldraw_2(surface, a.x, a.y, size, red)
        else:
            if a.g > 1.5:
                size = 2
            smalldraw_2(surface, a.x, a.y, size, green)

    for p in particle_array:
        smalldraw(surface, int(p.x), int(p.y))
        # pygame.draw.circle(surface, some_color, (int(p.x), int(p.y)), 3)


def draw_walls(main_surface, x0, y0, x1, y1,  color):
    for i in range(x0, x0 + x1):
        for j in range(y0, y0 + y1):
            main_surface.set_at((i, j), color)


def smalldraw(main_surface, x0, y0):
    for i in range(-2, 3):
        if i > -2 and i < 2:
            main_surface.set_at((x0 + i, y0 + 2), blue)
            main_surface.set_at((x0 + i, y0 - 2), blue)
        main_surface.set_at((x0 + i, y0), blue)
        main_surface.set_at((x0 + i, y0 - 1), blue)
        main_surface.set_at((x0 + i, y0 + 1), blue)


def smalldraw_2(main_surface, x0, y0, size, color):
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


def drawcircle(surface, x0, y0, r, another_color):
    x = r - 1
    y = 0
    dx = 1
    dy = 1
    err = dx - (r << 1)

    while x >= y:
        surface.set_at((x0 + x, y0 + y), another_color)
        surface.set_at((x0 - x, y0 + y), another_color)

        surface.set_at((x0 + y, y0 + x), another_color)
        surface.set_at((x0 - y, y0 + x), another_color)

        surface.set_at((x0 - y, y0 - x), another_color)
        surface.set_at((x0 + y, y0 - x), another_color)

        surface.set_at((x0 + x, y0 - y), another_color)
        surface.set_at((x0 - x, y0 - y), another_color)

        drawline(surface, x0 - x, y0 + y, x0 + x, y0 + y, another_color)
        drawline(surface, x0 + y, y0 + x, x0 - y, y0 + x, another_color)
        drawline(surface, x0 - y, y0 - x, x0 + y, y0 - x, another_color)
        drawline(surface, x0 + x, y0 - y, x0 - x, y0 - y, another_color)

        if err <= 0:
            y = y + 1
            err = err + dy
            dy = dy + 2

        if err > 0:
            x = x - 1
            dx = dx + 2
            err = (err + dx) - (r << 1)


def main():
    """ Set up the game and run the main game loop """
    pygame.init()      # Prepare the pygame module for use

    # Create surface of (width, height), and its window.
    main_surface = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
    clock = pygame.time.Clock()

    generate(np, na)
    count = 0
    while True:

        clock.tick(60)
        if count == 25:
            print("clock.get_fps", clock.get_fps())
            count = 0

        count += 1
        ev = pygame.event.poll()    # Look for any event
        if ev.type == pygame.QUIT:  # Window close button clicked?
            break                   # leave game loop

        # We draw everything from scratch on each frame.
        # So first fill everything with the background color
        main_surface.fill((0, 0, 0))

        try:
            simulate()
            draw_all(main_surface)
        except Exception as e:
            print(e)

        # Now the surface is ready, tell pygame to display it!
        pygame.display.flip()

    pygame.quit()     # Once we leave the loop, close the window.


if __name__ == '__main__':
    main()
