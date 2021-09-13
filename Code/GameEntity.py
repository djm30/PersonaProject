import pygame
import os
from Personas import personas

image_path = "assets//Sprites"


class GameEntity():

    # images is a dictionary of images, they key corresponding to an image state, i.e being damaged, standard or selected

    def __init__(self, x, y, persona, images):

        self.x = x
        self.y = y
        self.persona = persona
        self.images = images
        self.current_image = "damage"

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


Entities = []

Joker_Std = pygame.image.load(os.path.join(image_path, "joker_std.png"))
Joker_Damage = pygame.image.load(os.path.join(image_path, "joker_damage.png"))

Joker = GameEntity(200, 340, personas["Pixie"], {
    "standard": Joker_Std, "damage": Joker_Damage, "select": None})

Entities.append(Joker)

Jack_Std = pygame.image.load(os.path.join(image_path, "jacklantern_std.png"))
Jack_Damage = pygame.image.load(
    os.path.join(image_path, "jacklantern_damage.png"))
Jack_Select = pygame.image.load(
    os.path.join(image_path, "jacklantern_select.png"))

JackLantern = GameEntity(520, 200, personas["JackLantern"], {
    "standard": Jack_Std, "damage": Jack_Damage, "select": Jack_Select})

Entities.append(JackLantern)


if __name__ == '__main__':
    pass
