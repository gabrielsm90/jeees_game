# -*- encoding:utf-8 -*-
import pygame
import sys

from screen import MainScreen

# Decorator to control the main loop
def loop(f):
    def func():
        while True:
            f()
    return func

@loop
def core_function():
    #FIXME: Temos que pensar numa solução melhor para controlar os eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def main():
    main_screen = MainScreen(800, 600)
    core_function()

if __name__ == '__main__':
    main()
