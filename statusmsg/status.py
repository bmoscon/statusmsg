import os
from functools import wraps

from statusmsg.movement import RIGHT
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
    def __init__(self, text, success, fail, suppress=False):
        self.text = text
        self.success = success
        self.fail = fail
        self.suppress = suppress

    def __enter__(self):
        print(self.text, end='', flush=True)

    def __exit__(self, exc_type, exc_value, traceback):
        cols, _ = os.get_terminal_size(0)
        if any([exc_type, exc_value, traceback]):
            shift = cols - len(self.text) - len(self.fail) - 4
            print(RIGHT.format(shift), end='')
            print("[ " + RED + self.fail + RESET + " ]")
            
            if isinstance(self.suppress, list):
                return exc_type in self.suppress
            return self.suppress

        else:
            shift = cols - len(self.text) - len(self.success) - 4
            print(RIGHT.format(shift), end='')
            print("[ " + GREEN + self.success + RESET + " ]")
