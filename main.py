import pygame
import utils
import vars as v
import player


@utils.time_it
def init():
    pygame.init()
    pygame.display.set_caption('Game')
    for i in range(100):
        square = player.Player(v.window, 0, v.window.get_height() / 2, 10, 10, (255, 0, 0), i * 0.1)
        v.population.append(square)


@utils.try_catch
def draw():
    v.window.fill((0, 0, 0))
    for square in v.population:
        square.draw()
    pygame.display.update()


@utils.try_catch
def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            v.done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                v.done = True
            elif event.key == pygame.K_z:
                v.key_states[0] = True
            elif event.key == pygame.K_q:
                v.key_states[1] = True
            elif event.key == pygame.K_s:
                v.key_states[2] = True
            elif event.key == pygame.K_d:
                v.key_states[3] = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_z:
                v.key_states[0] = False
            elif event.key == pygame.K_q:
                v.key_states[1] = False
            elif event.key == pygame.K_s:
                v.key_states[2] = False
            elif event.key == pygame.K_d:
                v.key_states[3] = False


@utils.try_catch
def update(dt):
    handle_events()
    for square in v.population:
        if v.key_states[0]:
            square.move(0, -square.speed, 10)
        if v.key_states[1]:
            square.move(-square.speed, 0, 10)
        if v.key_states[2]:
            square.move(0, square.speed, 10)
        if v.key_states[3]:
            square.move(square.speed, 0, 10)


@utils.try_catch
def loop():
    clock = pygame.time.Clock()
    while not v.done:
        update(clock.tick(v.fps))
        draw()


@utils.time_it
def main():
    init()
    loop()
    pygame.quit()


if __name__ == '__main__':
    main()
