import pygame

from screen import MainScreen

# Decorator to control the main loop
def loop(f):
    def func():
        while True:
            f()
    return func

@loop
def core_function():
    pass

def main():
    main_screen = MainScreen(800, 600)
    core_function()

if __name__ == '__main__':
    main()
