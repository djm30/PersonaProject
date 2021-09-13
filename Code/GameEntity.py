import pygame
import os
from Personas import personas


class GameEntity():

    # images is a dictionary of images, they key corresponding to an image state, i.e being damaged, standard or selected

    def __init__(self, x, y, persona, images):

        self.x = x
        self.y = y
        self.persona = persona
        self.images = images
        self.current_image = "standard"

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    @property
    def persona(self):
        return self._persona

    @persona.setter
    def persona(self, value):
        self._persona = value

    @property
    def current_image(self):
        return self._current_image

    @current_image.setter
    def current_image(self, value):
        self._current_image = self.images[f"{value}"]


Std1 = pygame.image.load(os.path.join("assets", "jacklantern_std.png"))
Damage1 = pygame.image.load(os.path.join("assets", "jacklantern_damage.png"))
Select1 = pygame.image.load(os.path.join("assets", "jacklantern_select.png"))

Enemy1 = GameEntity(520, 200, personas["Pixie"], {
    "standard": Std1, "damage": Damage1, "select": Select1})


Entities = []
Entities.append(Enemy1)

if __name__ == '__main__':
    print(Enemy1.persona)
