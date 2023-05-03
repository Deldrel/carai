import pygame
import utils


class Player:
    def __init__(self, window, x=0, y=0, width=0, height=0, color=(255, 0, 0), speed=1):
        self.window = window
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.speed = speed

    @utils.try_catch
    def draw(self):
        pygame.draw.rect(self.window, self.color, (self.x, self.y, self.width, self.height))

    @utils.try_catch
    def move(self, dx, dy, max_depth):
        if max_depth <= 0:
            return
        if self.check_collisions(dx, dy):
            self.x += dx
            self.y += dy
        else:
            dx /= 2
            dy /= 2
            self.move(dx, dy, max_depth - 1)

    @utils.try_catch
    def check_collisions(self, dx, dy):
        if self.x + dx < 0 or self.x + dx > self.window.get_width() - self.width:
            return 0
        if self.y + dy < 0 or self.y + dy > self.window.get_height() - self.height:
            return 0
        return 1
