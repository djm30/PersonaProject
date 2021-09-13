import pygame
import os
from GameEntity import Entities

(WIDTH, HEIGT) = (1280, 720)

RED = (255, 5, 5)

WIN = pygame.display.set_mode((WIDTH, HEIGT))

pygame.mixer.init()
pygame.mixer.music.load(os.path.join("assets", "river_in_desert.wav"))


pygame.display.set_caption("Bruh moment")
FPS = 60

BACKGROUND = pygame.image.load(os.path.join("assets", "bg.jpg"))
BACKGROUND = pygame.transform.scale(BACKGROUND, (1280, 720))
print(os.getcwd())


# Draws every object on the screen


def draw_characters():
    WIN.blit(BACKGROUND, (0, 0))

    for entity in Entities:
        WIN.blit(entity.current_image, (entity.x, entity.y))


def main():
    run = True
    clock = pygame.time.Clock()
    pygame.mixer.music.play(loops=-1)

    while run:
        clock.tick(FPS)
        # Checking pygame events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        WIN.fill(RED)
        draw_characters()
        pygame.display.update()


if __name__ == '__main__':
    main()
