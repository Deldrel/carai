import pygame
import utils
import vars as v


class Player:
    def __init__(self, x=0, y=0, width=0, height=0, color=(255, 0, 0), speed=1, neuralnetwork=None, state=1):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.speed = speed
        self.neuralnetwork = neuralnetwork
        self.state = state

    @utils.try_catch
    def update(self, nn):
        self.neuralnetwork = nn

    @utils.try_catch
    def draw(self):
        pygame.draw.rect(v.window, self.color, (self.x, self.y, self.width, self.height))

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
    def move(self, dx, dy):
        if self.check_collisions(dx, dy):
            self.x += dx
            self.y += dy
        else:
            self.state = 0

    @utils.try_catch
    def fitness(self):
        if self.state == 0:
            return 0
        val = utils.distance(self.x, self.y, v.target[0], v.target[1])
        return utils.map_range(val, v.window.get_width(), 0, 0, 1)

    @utils.try_catch
    def check_collisions(self, dx, dy):
        if self.x + dx < 0 or self.x + dx > v.window.get_width() - self.width:
            return 0
        if self.y + dy < 0 or self.y + dy > v.window.get_height() - self.height:
            return 0
        return 1
