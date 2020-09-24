from functools import wraps
import time


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f' -- Timing (timer)')
        start = time.perf_counter()
        func(*args, **kwargs)
        end = time.perf_counter()
        print(f' -- {func.__name__} took {int(end - start)}s to run. (timer)')

    return wrapper


def timer2(func):
    def wrapper(*args, **kwargs):
        print(f' -- Timing (timer2)')
        start = time.perf_counter()
        func(*args, **kwargs)
        end = time.perf_counter()
        print(f' -- {func.__name__} took {int(end - start)}s to run. (timer2)')

    return wrapper


class App:

    def run(self):
        self.function1()
        self.function2()
        self.function3()

    @timer
    def function1(self):
        print("Doing stuff...")
        time.sleep(2)
        print("Finished...")

    @timer2
    def function2(self):
        print("Doing stuff...")
        time.sleep(2)
        print("Finished...")

    @timer2
    @timer
    def function3(self):
        print("Doing stuff...")
        time.sleep(2)
        print("Finished...")
