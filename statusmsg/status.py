import os
from functools import wraps

from statusmsg.movement import RIGHT, LEFT
from statusmsg.colors import GREEN, RED, RESET


def decorator(text, success, fail):
    def wrap(func):
        @wraps(func)
        def wrapped_f(*args, **kwargs):
            cols, _ = os.get_terminal_size(0)
            print(text, end='', flush=True)
            try:
                func(*args, **kwargs)
            except:
                shift = cols - len(text) - len(fail) - 4
                print(RIGHT.format(shift), end='')
                print("[ " + RED + fail + RESET + " ]")
                raise
            shift = cols - len(text) - len(success) - 4
            print(RIGHT.format(shift), end='')
            print("[ " + GREEN + success + RESET + " ]")
        return wrapped_f
    return wrap


class context:
    def __init__(self, text, success, fail, progress=0, suppress=False):
        self.text = text
        self.success = success
        self.fail = fail
        self.suppress = suppress
        self.count = 0
        self.end = progress
        self.ticks = 0

    def __enter__(self):
        print(self.text, end='', flush=True)
        if self.end != 0:
            self.__progress()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        cols, _ = os.get_terminal_size(0)

        if any([exc_type, exc_value, traceback]):
            shift = cols - len(self.text) - len(self.fail) - 4 - self.ticks
            print(RIGHT.format(shift), end='')
            print("[ " + RED + self.fail + RESET + " ]")
            
            if isinstance(self.suppress, list):
                return exc_type in self.suppress
            return self.suppress
        else:
            if self.end != 0:
                self.__fill()
            shift = cols - len(self.text) - len(self.success) - 4 - self.ticks
            print(RIGHT.format(shift), end='')
            print("[ " + GREEN + self.success + RESET + " ]")
    
    def __progress(self):
        cols, _ = os.get_terminal_size(0)
        self.bar_width = cols - (len(self.text) + max(len(self.fail), len(self.success)) + 4 + 4)
        self.progress_interval = self.end // self.bar_width + 1
        print(" [", end='')
        print(" " * self.bar_width, end='')
        print("] ", end='')
        print(LEFT.format(self.bar_width + 2), end='', flush=True)
        self.ticks += 2
    
    def __fill(self):
        if self.ticks - 2 != self.bar_width:
            missing = self.bar_width - (self.ticks - 2)
            self.ticks += missing
            print("*" * missing, end='')
    
    def update(self):
        self.count += 1
        if self.count % self.progress_interval == 0:
            print("*", end='', flush=True)
            self.ticks += 1
