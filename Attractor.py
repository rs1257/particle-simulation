import random
import Constants

class Attractor:
    def __init__(self, neg=False):
        self.x = random.randint(0 + 7, Constants.SCREEN_X - 7)
        self.y = random.randint(0 + 7, Constants.SCREEN_Y - 7)
        if neg:
            self.g = -1 * random.uniform(0.5, 1.0)
        else:
            self.g = random.uniform(1.0, 2.0)