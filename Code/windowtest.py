import pygame

(WIDTH, HEIGT) = (1280, 720)

RED = (255, 5, 5)

WIN = pygame.display.set_mode((WIDTH, HEIGT))


pygame.display.set_caption("Bruh moment")
FPS = 60

test1 = pygame.Rect(600, 200, 40, 75)


class GameEntity():
    def __init__(self):
        pass


def draw_characters():
    pygame.draw.rect(WIN, (100, 100, 100), test1)
    test1.x += 1


def main():
    run = True
    clock = pygame.time.Clock()

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
