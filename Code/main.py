import pygame
import os
from GameEntity import Entities

image_path = "assets//Sprites"
sound_path = "assets//Sounds"

FPS = 60

(WIDTH, HEIGT) = (1280, 720)

RED = (255, 5, 5)

ICON = pygame.image.load(os.path.join(image_path, "logo.png"))
ICON = pygame.transform.scale(ICON, (32, 32))
BACKGROUND = pygame.image.load(os.path.join(image_path, "bg.jpg"))

pygame.display.set_icon(ICON)
pygame.display.set_caption("Bruhsona")
WIN = pygame.display.set_mode((WIDTH, HEIGT))

pygame.mixer.init()
pygame.mixer.music.load(os.path.join(sound_path, "river_in_desert.wav"))


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
