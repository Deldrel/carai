import pygame
import utils
import vars as v
import player
import neuralnet
import random


@utils.time_it
def init():
    pygame.init()
    pygame.display.set_caption('Game')
    for i in range(200):
        nn = neuralnet.NeuralNetwork([3, 5, 5, 4])
        square = player.Player(0, 0, 10, 10, (255, 0, 0), 5, nn)
        v.population.append(square)


@utils.try_catch
def newgen():
    avg_fitness = 0
    best_fitness = 0
    for square in v.population:
        if square.fitness() > best_fitness:
            best_fitness = square.fitness()
        avg_fitness += square.fitness()
    avg_fitness /= len(v.population)
    print('Average fitness: {}'.format(avg_fitness) + ' Best fitness: {}'.format(best_fitness))

    v.population.sort(key=lambda x: x.fitness(), reverse=True)
    new_population = []
    percent10index = len(v.population) // 10
    for i in range(percent10index):
        new_population.append(v.population[i])

    for i in range(percent10index, len(v.population) - percent10index):
        parent = random.choice(new_population)
        v.population[i].update(v.population[i].neuralnetwork.breed(parent.neuralnetwork, 0.5))
    for i in range(percent10index, len(v.population) - percent10index):
        v.population[i].neuralnetwork.mutate(0.01)
    for i in range(len(v.population)):
        v.population[i].state = 1
        v.population[i].x = random.randint(0, v.window.get_width())
        v.population[i].y = random.randint(0, v.window.get_height())


@utils.try_catch
def draw():
    v.window.fill((0, 0, 0))
    for square in v.population:
        if square.state == 1:
            square.draw()
    pygame.draw.rect(v.window, (0, 255, 0), (v.target[0], v.target[1], 10, 10))
    pygame.display.update()


@utils.try_catch
def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            v.done = True


@utils.try_catch
def update(dt):
    if v.counter >= v.number_of_steps:
        newgen()
        v.counter = 0
    for square in v.population:
        if square.state == 0:
            continue
        inputparams = [square.x / v.window.get_width(), square.y / v.window.get_height(), square.fitness()]
        output = square.neuralnetwork.feedforward(inputparams)
        if output[0] > 0.5:
            square.move(0, -square.speed)
        if output[1] > 0.5:
            square.move(0, square.speed)
        if output[2] > 0.5:
            square.move(-square.speed, 0)
        if output[3] > 0.5:
            square.move(square.speed, 0)
    v.counter += 1


@utils.try_catch
def loop():
    clock = pygame.time.Clock()
    while not v.done:
        handle_events()
        update(clock.tick(v.fps))
        draw()


@utils.time_it
def main():
    init()
    loop()
    pygame.quit()


if __name__ == '__main__':
    main()
