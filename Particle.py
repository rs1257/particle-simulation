import random
import Constants

class Particle:
    def __init__(self):
        self.x = random.randint(0 + 2, Constants.SCREEN_X - 2)
        self.y = random.randint(0 + 2, Constants.SCREEN_Y - 2)
        self.vx = 0
        self.vy = 0