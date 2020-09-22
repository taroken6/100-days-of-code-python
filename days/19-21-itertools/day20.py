import itertools
import time
import random


class App():
    def __init__(self):
        pass

    def run(self):
        tl = itertools.cycle(reversed(['Red', 'Yellow', 'Green']))
        timer = {'Red': 10, 'Yellow': 3, 'Green': 10}  # Seconds 'til next light
        for _ in range(12):
            curr = next(tl)
            start = time.process_time()
            busy = random.choice([True, False])
            print(f'{curr}, Busy = {busy}')

            while time.process_time() - start < timer[curr]:
                if not busy and curr == 'Green':
                    curr = next(tl)
