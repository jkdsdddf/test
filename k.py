import random
import time

class RandomNumberGenerator:
  def __init__(self, seed=None):
    self.seed = seed
    self.reset_seed()

def reset_seed(self):
  if self.seed is None:
    self.seed = int(time.time())
  random.seed(self.seed)

def randint(self, a, b):
  return random.randint(a, b)

def randrange(self, start, stop=None, step=1):
  return random.randrange(start, stop, step)
