from pygame_widgets.slider import Slider
import pygame_widgets
import pygame
import random


pygame.init()


dims = [pygame.display.Info().current_w, pygame.display.Info().current_h]
screen = pygame.display.set_mode(dims, pygame.FULLSCREEN)
pygame.display.set_caption("Visualisation")
slider_w = Slider(screen, dims[0] - 240, dims[1] - 120, 200, 30, min=-dims[1] / 10, max=dims[1] / 10, step=0.01)
slider_b = Slider(screen, dims[0] - 240, dims[1] - 60, 200, 30, min=-dims[1] / 2, max=dims[1] / 2, step=0.01)

samples = tuple((random.randint(0, dims[0]), random.randint(0, dims[1])) for _ in range(1000))
colors = tuple(p[1] <= dims[1] - (p[0] - 400) / 1.5 for p in samples)
colors2 = tuple(p[1] <= dims[1] - (p[0] - 400) ** 2 / 500 for p in samples)

running = True
show = False
col2 = False


while running:
    screen.fill((50, 50, 50))

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            show = not show

        if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
            col2 = not col2

    pygame.draw.line(screen, "red", (0, dims[1] / 2 + 20 * slider_w.value - slider_b.value),
                     (dims[0], dims[1] / 2 - 20 * slider_w.value - slider_b.value), 10)

    if show:
        pygame.draw.polygon(screen, (50, 150, 50), ((0, 0), (0, dims[1]),
                                                    (0, dims[1] / 2 + 20 * slider_w.value - slider_b.value),
                                                    (dims[0], dims[1] / 2 - 20 * slider_w.value - slider_b.value),
                                                    (dims[0], 0)))

    for i, sample in enumerate(samples):
        if not col2:
            pygame.draw.circle(screen, "green" if colors[i] else "red", sample, 10)
        else:
            pygame.draw.circle(screen, "green" if colors2[i] else "red", sample, 10)

    pygame_widgets.update(events)
    pygame.display.flip()

pygame.quit()
