import pygame
import random

fps = 60
window = pygame.display.set_mode((800, 600))
done = False
population = []
number_of_steps = 100
counter = 0
target = [random.randint(0, window.get_width()), random.randint(0, window.get_height())]

